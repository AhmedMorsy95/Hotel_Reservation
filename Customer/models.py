from django.db import models

# Create your models here.
class customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    Black_listed = models.IntegerField(default=0)