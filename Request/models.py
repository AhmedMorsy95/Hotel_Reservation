from django.db import models
from Owner.models import owner

class requests(models.Model):
    #Owner_id	hotel_location_id	hotel_name	count	stars	image
    #owner_id foreign key
    owner_id = models.ForeignKey(owner, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city=models.CharField(max_length=100 )
    hotel_name = models.CharField(max_length=100)
    singleRoomsCount = models.IntegerField(default=0)
    doubleRoomsCount = models.IntegerField(default=0)
    singelRoomsPrice = models.IntegerField(default=0)
    doubleRoomsPrice = models.IntegerField(default=0)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='media')
    state = models.CharField(max_length=100, default='Pending')
