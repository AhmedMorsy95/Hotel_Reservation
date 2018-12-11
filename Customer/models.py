from django.db import models

# Create your models here.
class customer(models.Model):
   username = models.CharField(max_length=100,blank = False) #false because required to register
   password = models.CharField(max_length=100, blank = False)
   email = models.EmailField(max_length=70 , blank = False)
   mobile = models.BigAutoField((max_length=30 , blank = False)
   blackListed = models.BooleanField(default = False)
