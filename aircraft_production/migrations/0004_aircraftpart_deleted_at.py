# Generated by Django 5.1.4 on 2024-12-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft_production', '0003_remove_aircraft_assembly_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftpart',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]