from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.utils.timezone import now

from .forms import EmployeeRegistrationForm, EmployeeLoginForm, ProducePartForm
from .models import Employee, AircraftPart, TeamPartAuthorization, Part, ProducedAircraft, Aircraft, UsedPart


# Registration View
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            # User kaydını oluştur
            user = form.save()

            # Team bilgisi alınıyor
            team = form.cleaned_data['team']

            # Employee modeline kaydediliyor
            Employee.objects.create(user=user, team=team)

            login(request, user)  # Kullanıcıyı otomatik giriş yap
            return redirect('dashboard')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_employee(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Başarılı giriş sonrası yönlendirme
        else:
            # Hataları form üzerinden iletebilirsiniz
            return render(request, 'login.html', {'form': form})
    else:
        form = EmployeeLoginForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_employee(request):
    logout(request)
    return redirect('login')  # Çıkış sonrası giriş ekranına yönlendirme
@login_required
def dashboard(request):
    # Kullanıcının takım bilgisini çekiyoruz (örnek: user.team)
    print("gşrdş")
    user_team = getattr(request.user, 'team', None)  # Kullanıcının takım bilgisi
    employee = Employee.objects.get(user=request.user)
    team = employee.team.name
    if team == "Montaj Takımı":
        return redirect('montaj_page')
    print(team)
    if team:
        team_parts = {
            'Kanat Takımı': 'Kanat Parçası',
            'Gövde Takımı': 'Gövde Parçası',
            'Kuyruk Takımı': 'Kuyruk Parçası',
            'Aviyonik Takımı': 'Aviyonik Parçası',

        }
        part_to_produce = team_parts.get(team, None)
        return render(request, 'dashboard.html', {'part': part_to_produce, 'team': team})
    else:
        return render(request, 'error.html', {'message': 'Takım bilgisi bulunamadı.'})
def montaj_page(request):
    # Montaj sayfasını render et
    return render(request, 'montaj.html')
def produce_part(request):
    print("metodagirdi")
    if request.method == 'POST':
        print("girdi")
        form = ProducePartForm(request.POST)
        if form.is_valid():
            aircraft = form.cleaned_data['aircraft']
            quantity = form.cleaned_data['quantity']

            # Kullanıcının takımını al
            employee = Employee.objects.get(user=request.user)
            team = employee.team

            # TeamPartAuthorization tablosundan uygun Part nesnesini al
            authorization = get_object_or_404(TeamPartAuthorization, team=team)
            part = authorization.part  # Part nesnesi
            partid = part.id  # Part ID

            # AircraftPart tablosunda bu PartID'ye ait kaydı bul veya oluştur
            aircraft_part, created = AircraftPart.objects.get_or_create(part=part, aircraft=aircraft)
            part.stock += quantity
            part.save()
            # Stok miktarını güncelle
            aircraft_part.quantity += quantity
            aircraft_part.save()
            success_message = f"{quantity} adet {part.name} parçası {aircraft.name} için üretildi."

            return render(request, 'produce_part.html', {'form': form, 'success_message': success_message})
    else:
        form = ProducePartForm()

    return render(request, 'produce_part.html', {'form': form})

def part_list(request):
    # Geri dönüşüme atılmamış parçaları listeler
    parts = AircraftPart.objects.filter(deleted_at__isnull=True).select_related('aircraft', 'part')
    return render(request, 'part_list.html', {'parts': parts})

def decrement_part(request, part_id):
    # AircraftPart kaydını bul
    part = get_object_or_404(AircraftPart, id=part_id, deleted_at__isnull=True)

    # İlgili Part kaydını bul
    related_part = part.part  # AircraftPart ile ilişkili Part nesnesi

    # Stok miktarını azalt
    if part.quantity > 1:
        part.quantity -= 1
        part.save()

        # Part tablosundaki stoktan da düş
        if related_part.stock > 0:
            related_part.stock -= 1
            related_part.save()
    else:
        # Eğer miktar 1 ise, geri dönüşüme at
        if related_part.stock > 0:
            related_part.stock -= 1
            related_part.save()
        part.quantity = 0
        part.deleted_at = now()
        part.save()

    return redirect('part_list')  # İşlemden sonra listeleme sayfasına yönlendir
def recycled_parts(request):
    # Geri dönüşüme atılmış parçaları listeler
    parts = AircraftPart.objects.filter(deleted_at__isnull=False).select_related('aircraft', 'part')
    return render(request, 'recycled_parts.html', {'parts': parts})

def restore_part(request, part_id):
    # Geri dönüşümden çıkar
    part = get_object_or_404(AircraftPart, id=part_id, deleted_at__isnull=False)
    part.restore()
    return redirect('recycled_parts')
def delete_part(request, part_id):
    # Parçayı geri dönüşüme at
    part = get_object_or_404(AircraftPart, id=part_id, deleted_at__isnull=True)
    part.delete()
    return redirect('part_list')

def montaj_page(request):
    if not hasattr(request.user, 'employee_profile') or request.user.employee_profile.team.name != 'Montaj Takımı':
        # Eğer kullanıcı montaj takımında değilse, dashboard'a yönlendir
        return redirect('login')
    # GET isteği için tüm uçakları gönder
    aircrafts = Aircraft.objects.all()
    return render(request, 'montaj.html', {'aircrafts': aircrafts})


from django.db import transaction


def produce_aircraft(request):
    if request.method == 'POST':
        aircraft_id = request.POST.get('aircraft_id')
        selected_aircraft = get_object_or_404(Aircraft, id=aircraft_id)

        # Parçaları kontrol et
        parts = AircraftPart.objects.filter(quantity__gt=0, deleted_at__isnull=True, aircraft=selected_aircraft)
        required_parts = {
            'Kanat': 2,  # 2 kanat gerekiyor
            'Gövde': 1,
            'Kuyruk': 1,
            'Aviyonik': 1
        }

        # Mevcut parçaları ve miktarlarını kontrol et
        available_parts = {part.part.name: part.quantity for part in parts}
        missing_parts = [
            (part_name, required_qty - available_parts.get(part_name, 0))
            for part_name, required_qty in required_parts.items()
            if available_parts.get(part_name, 0) < required_qty
        ]

        # Eksik parçalar varsa hata şablonuna yönlendir
        if missing_parts:
            return render(request, 'montaj_error.html', {
                'missing_parts': missing_parts,
                'aircraft': selected_aircraft
            })

        # Parçaları azalt ve kaydet
        with transaction.atomic():
            produced_aircraft = ProducedAircraft.objects.create(name=f"{selected_aircraft.name}")

            for part_name, required_qty in required_parts.items():
                part = AircraftPart.objects.get(part__name=part_name, aircraft=selected_aircraft)

                # Kullanılan parçaları kaydet
                UsedPart.objects.create(
                    produced_aircraft=produced_aircraft,
                    part=part.part,
                    quantity=required_qty
                )

                # Stoktan düş
                part.quantity -= required_qty
                part.save()

        return render(request, 'montaj_success.html', {'aircraft': produced_aircraft})
    return redirect('montaj_page')


def produced_aircraft_list(request):
    # Tüm üretilen uçakları al
    produced_aircrafts = ProducedAircraft.objects.all()
    return render(request, 'produced_aircraft_list.html', {'produced_aircrafts': produced_aircrafts})
