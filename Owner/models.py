from django.db import models

# Create your models here.
from django.db import models

class Owner(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=15)
  
