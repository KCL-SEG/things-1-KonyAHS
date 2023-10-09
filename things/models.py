from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    quantity= models.PositiveIntegerField()
