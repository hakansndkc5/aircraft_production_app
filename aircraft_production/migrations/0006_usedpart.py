# Generated by Django 5.1.4 on 2024-12-11 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft_production', '0005_producedaircraft'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_in_aircrafts', to='aircraft_production.part')),
                ('produced_aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_parts', to='aircraft_production.producedaircraft')),
            ],
        ),
    ]
