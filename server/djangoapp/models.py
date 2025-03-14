from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Optional additional field
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Country of origin",
    )

    def __str__(self):
        return self.name  # Returns the name of the car make (e.g., "Toyota")


class CarModel(models.Model):
    # Many-To-One relationship with CarMake
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name="models",
    )

    # Name of the car model
    name = models.CharField(max_length=100)

    # Type with choices
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    )
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SEDAN',
    )

    # Year with min and max validators
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2025),
        ],
        help_text="Year of the car model (2015-2025)",
    )

    # Optional additional field
    fuel_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="e.g., Gasoline, Electric, Hybrid",
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # e.g., "Toyota Camry (2020)"
