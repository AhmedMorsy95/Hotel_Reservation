from django.db import models
from Hotel.models import hotel

class room(models.Model):

	hotel_id = models.ForeignKey(hotel,on_delete= models.CASCADE)
	image = models.ImageField(upload_to='media')
	price = models.IntegerField(default=0)
	number = models.IntegerField(default=0,unique=False)
	room_type = models.CharField(max_length=10)
	