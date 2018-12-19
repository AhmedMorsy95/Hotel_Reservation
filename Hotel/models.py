from django.db import models
from Location.models import location
# Create your models here.

class hotel(models.Model):
    # owner id foreign key
    location_id = models.ForeignKey(location,on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    rating = models.FloatField(null=True, blank=True, default=None)
    stars = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    rates_count = models.IntegerField(default=0)
    rates_sum = models.IntegerField(default=0)
