from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity= models.IntegerField(unique=False, max_value=100, min_value=0)
