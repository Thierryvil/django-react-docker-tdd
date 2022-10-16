from django.db import models


class PersonModel(models.Model):
    class Meta:
        db_table = "persons"

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
