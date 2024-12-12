
from django.test import TestCase
from aircraft_production.models import Part, Aircraft, Team

class PartModelTestCase(TestCase):
    def setUp(self):
        """
        Test öncesinde örnek Part verilerini oluşturur.
        """
        self.part = Part.objects.create(name="WING", stock=10)

    def test_part_creation(self):
        """
        Part modelinin doğru şekilde oluşturulmasını test eder.
        """
        self.assertEqual(self.part.name, "WING")
        self.assertEqual(self.part.stock, 10)

    def test_part_update_stock(self):
        """
        Part modelinde stok güncellemesini test eder.
        """
        self.part.stock += 5
        self.part.save()
        self.assertEqual(self.part.stock, 15)

    def test_part_str_representation(self):
        """
        Part modelinin __str__ metodunu test eder.
        """
        self.assertEqual(str(self.part), "WING - Stock: 10")


class AircraftModelTestCase(TestCase):
    def setUp(self):
        """
        Test öncesinde örnek Aircraft verilerini oluşturur.
        """
        self.aircraft = Aircraft.objects.create(name="Boeing 747")

    def test_aircraft_creation(self):
        """
        Aircraft modelinin doğru şekilde oluşturulmasını test eder.
        """
        self.assertEqual(self.aircraft.name, "Boeing 747")

    def test_aircraft_str_representation(self):
        """
        Aircraft modelinin __str__ metodunu test eder.
        """
        self.assertEqual(str(self.aircraft), "Boeing 747")


class TeamModelTestCase(TestCase):
    def setUp(self):
        """
        Test öncesinde örnek Team verilerini oluşturur.
        """
        self.team = Team.objects.create(name="WING")

    def test_team_creation(self):
        """
        Team modelinin doğru şekilde oluşturulmasını test eder.
        """
        self.assertEqual(self.team.name, "WING")

    def test_team_str_representation(self):
        """
        Team modelinin __str__ metodunu test eder.
        """
        self.assertEqual(str(self.team), "WING")
