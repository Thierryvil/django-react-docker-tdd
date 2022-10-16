from django.db import models
from persons.models import PersonModel


class CarModel(models.Model):
    class Meta:
        db_table = "cars"
        verbose_name_plural = "Cars"

    YELLOW = 1
    BLUE = 2
    GRAY = 3

    COLORS = (
        (YELLOW, "yellow"),
        (BLUE, "blue"),
        (GRAY, "gray"),
    )

    HATCH = 1
    SEDAN = 2
    CONVERTIBLE = 3

    TYPES = (
        (HATCH, "hatch"),
        (SEDAN, "sedan"),
        (CONVERTIBLE, "convertible"),
    )

    color = models.CharField(max_length=255, choices=COLORS)
    type = models.CharField(max_length=255, choices=TYPES)
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE, related_name="cars")
