from django.db import models

class customer(models.Model):
   user_name = models.CharField(max_length=100, blank=False) #false because required to register
   password = models.CharField(max_length=100, blank=False)
   email = models.EmailField(max_length=70 , blank=False, unique=True)
   mobile = models.CharField(max_length=80 ,blank=False)
   black_listed = models.BooleanField(default=False)