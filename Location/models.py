from django.db import models

from Hotel.models import hotel

# Create your models here.
class location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
