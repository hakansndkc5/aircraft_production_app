# Generated by Django 5.1.4 on 2024-12-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft_production', '0002_part_team_remove_aircraft_manufacturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='assembly_completed',
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]