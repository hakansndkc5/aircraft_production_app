from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from aircraft_production.models   import Employee, Aircraft, Part, AircraftPart, ProducedAircraft, Team, TeamPartAuthorization


class ViewTestCase(TestCase):
    def setUp(self):
        """
        Testler için gerekli olan örnek veri seti oluşturur.
        """
        # Kullanıcı ve takım oluştur
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.team = Team.objects.create(name="Kanat Takımı")

        # Employee oluştur
        self.employee = Employee.objects.create(user=self.user, team=self.team)

        # Parça ve uçak oluştur
        self.part = Part.objects.create(name="Kanat", stock=10)
        self.aircraft = Aircraft.objects.create(name="Boeing 747")

        # Authorization ve AircraftPart oluştur
        self.authorization = TeamPartAuthorization.objects.create(team=self.team, part=self.part)
        self.aircraft_part = AircraftPart.objects.create(part=self.part, aircraft=self.aircraft, quantity=5)

        self.client = Client()



    def test_dashboard_view(self):
        """
        Dashboard sayfasının doğru şekilde render edildiğini test eder.
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kanat Parçası")  # Doğru parçanın render edildiğini kontrol eder

    def test_produce_part(self):
        """
        Parça üretim işleminin başarılı olduğunu test eder.
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse('produce_part'), {
            'aircraft': self.aircraft.id,
            'quantity': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "5 adet Kanat parçası Boeing 747 için üretildi.")
        self.part.refresh_from_db()
        self.assertEqual(self.part.stock, 15)  # Stok artışını kontrol eder

    def test_part_list(self):
        """
        Parçaların doğru şekilde listelendiğini test eder.
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('part_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kanat")


    def test_produced_aircraft_list(self):
        """
        Üretilen uçakların doğru şekilde listelendiğini test eder.
        """
        ProducedAircraft.objects.create(name="Boeing 747 - 1")
        response = self.client.get(reverse('produced_aircraft_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Boeing 747 - 1")
