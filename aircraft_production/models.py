from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Part Model
class Part(models.Model):
    PART_TYPES = [
        ('KANAT', 'Kanat'),
        ('GÖVDE', 'Gövde'),
        ('KUYRUK', 'Kuyruk'),
        ('AVİYONİK', 'Aviyonik'),
    ]

    name = models.CharField(max_length=50, choices=PART_TYPES)
    stock = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f"{self.name} - Stock: {self.stock}"


# Aircraft Model
class Aircraft(models.Model):
    name = models.CharField(max_length=50)



    def __str__(self):
        return self.name


# Team Model
class Team(models.Model):
    TEAM_TYPES = [
        ('Kanat', 'Kanat Takımı'),
        ('Gövde', 'Gövde Takımı'),
        ('Kuyruk', 'Kuyruk Takımı'),
        ('Aviyonik', 'Aviyonik Takımı'),
        ('Montaj', 'Montaj Takımı'),
    ]

    name = models.CharField(max_length=50, choices=TEAM_TYPES)

    def __str__(self):
        return self.name


# Employee Model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='employees')


    def __str__(self):
        return self.user.get_full_name() 

class ProducedAircraft(models.Model):
    name = models.CharField(max_length=100)  # Üretilen uçağın adı
    produced_at = models.DateTimeField(default=now)  # Üretim tarihi
    quantity = models.IntegerField(default=1)  # Üretilen uçak adedi

    def __str__(self):
        return f"{self.name} (Üretim Tarihi: {self.produced_at})"

# Aircraft-Part Relationship
class AircraftPart(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='parts')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='aircrafts')
    quantity = models.PositiveIntegerField(default=0)  # Quantity used
    deleted_at = models.DateTimeField(null=True, blank=True)  # Geri dönüşümde mi kontrolü için

    class Meta:
        unique_together = ('aircraft', 'part')  # Her parça sadece bir uçakta kullanılabilir.

    def __str__(self):
        return f"{self.aircraft} - {self.part}"

    def update_stock(self, additional_quantity):
        self.quantity += additional_quantity
        self.save()

    def delete(self):
        """Parçayı geri dönüşüme atar."""
        self.deleted_at = now()
        self.save()

    def restore(self):
        """Parçayı geri dönüşümden çıkarır."""
        self.deleted_at = None
        self.save()


# Team-Part Authorization
class TeamPartAuthorization(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='authorizations')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='authorized_teams')

    def __str__(self):
        return f"{self.team} - {self.part}"

class UsedPart(models.Model):
    produced_aircraft = models.ForeignKey(
        'ProducedAircraft',
        on_delete=models.CASCADE,
        related_name='used_parts'
    )
    part = models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        related_name='used_in_aircrafts'
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.part.name} for {self.produced_aircraft.name}"
