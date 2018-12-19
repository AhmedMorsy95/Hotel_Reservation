from django.db import models
from Owner.models import owner

class requests(models.Model):
    #Owner_id	hotel_location_id	hotel_name	count	stars	image
    #owner_id foreign key
    owner_id = models.ForeignKey(owner, on_delete=models.CASCADE,null=False)
    country = models.CharField(max_length=100)
    city=models.CharField(max_length=100 )
    hotel_name = models.CharField(max_length=100)
    singleRoomsCount = models.IntegerField(default=0)
    doubleRoomsCount = models.IntegerField(default=0)
    singleRoomsPrice = models.IntegerField(default=0)
    doubleRoomsPrice = models.IntegerField(default=0)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='media')
    state = models.CharField(max_length=100, default='Pending')
    imageS = models.ImageField(upload_to='media',null=True)
    imageD = models.ImageField(upload_to='media',null=True)