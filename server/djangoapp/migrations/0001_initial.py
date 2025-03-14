# Generated by Django 5.1.7 on 2025-03-12 06:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                (
                    'country',
                    models.CharField(
                        blank=True,
                        help_text='Country of origin',
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                (
                    'type',
                    models.CharField(
                        choices=[
                            ('SEDAN', 'Sedan'),
                            ('SUV', 'SUV'),
                            ('WAGON', 'Wagon'),
                            ('TRUCK', 'Truck'),
                            ('COUPE', 'Coupe'),
                        ],
                        default='SEDAN',
                        max_length=10,
                    ),
                ),
                (
                    'year',
                    models.IntegerField(
                        help_text='Year of the car model (2015-2025)',
                        validators=[
                            django.core.validators.MinValueValidator(2015),
                            django.core.validators.MaxValueValidator(2025),
                        ],
                    ),
                ),
                (
                    'fuel_type',
                    models.CharField(
                        blank=True,
                        help_text='e.g., Gasoline, Electric, Hybrid',
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    'car_make',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='models',
                        to='djangoapp.carmake',
                    ),
                ),
            ],
        ),
    ]
