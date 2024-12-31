from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=125)
    category=models.CharField(max_length=125)
    brand=models.CharField(max_length=125)

    def __str__(self) -> str:
        return super().__str__()

