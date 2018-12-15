from django.db import models


# Create your models here.
class location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
