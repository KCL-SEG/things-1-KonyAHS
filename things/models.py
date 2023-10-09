from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity= models.PositiveIntegerField(unique=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
