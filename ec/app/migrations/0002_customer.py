# Generated by Django 5.0.4 on 2024-05-11 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('AMA', 'Amazonas'), ('ANT', 'Antioquia'), ('ARA', 'Arauca'), ('ATL', 'Atlántico'), ('BOL', 'Bolívar'), ('BOY', 'Boyacá'), ('CAL', 'Caldas'), ('CAQ', 'Caquetá'), ('CAS', 'Casanare'), ('CAU', 'Cauca'), ('CES', 'Cesar'), ('CHO', 'Chocó'), ('COR', 'Córdoba'), ('CUN', 'Cundinamarca'), ('DC', 'Distrito Capital de Bogotá'), ('GUA', 'Guainía'), ('GUV', 'Guaviare'), ('HUI', 'Huila'), ('GUV', 'La Guajira'), ('MAG', 'Magdalena'), ('MET', 'Meta'), ('NAR', 'Nariño'), ('NSA', 'Norte de Santander'), ('PUT', 'Putumayo'), ('QUI', 'Quindío'), ('RIS', 'Risaralda'), ('SAP', 'San Andrés y Providencia'), ('SAN', 'Santander'), ('SUC', 'Sucre'), ('TOL', 'Tolima'), ('VAC', 'Valle del Cauca'), ('VAU', 'Vaupés'), ('VID', 'Vichada')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
