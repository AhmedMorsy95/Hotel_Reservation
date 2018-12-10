from django.db import models
from Location.models import location
# Create your models here.

class request(models.Model):
    #Owner_id	hotel_location_id	hotel_name	count	stars	image
    #owner_id foreign key
    hotel_location_id = models.ForeignKey(location,on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    singleRoomsCount = models.IntegerField(default=0)
    doubleRoomsCount = models.IntegerField(default=0)
    singelRoomsPrice = models.IntegerField(default=0)
    doubleRoomsPrice = models.IntegerField(default=0)
    stars = models.IntegerField
    image = models.ImageField(upload_to=None)