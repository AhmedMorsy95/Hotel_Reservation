from django.db import models


class owner(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    mobileNumber = models.CharField(max_length=15)
