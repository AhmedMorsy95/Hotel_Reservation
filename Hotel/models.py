from django.db import models
# Create your models here.

class hotel(models.Model):
    id = models.AutoField(primary_key=True , null=False)
    country = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50 , default="")
    name = models.CharField(max_length=50)
    rating = models.FloatField(null=True, blank=True, default=None)
    stars = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    rates_count = models.IntegerField(default=0)
    rates_sum = models.IntegerField(default=0)
    is_suspended = models.IntegerField(default=0)
