from django.db import models
from Hotel.models import hotel

class room(models.Model):

	TYPES = (
    (0, 'Single'),
    (1, 'Double'),
    (2, 'Triple'),
	)
	hotel_id = models.ForeignKey(hotel,on_delete= models.CASCADE)
	image = models.ImageField(upload_to='media')
	price = models.IntegerField(default=0)
	number = models.IntegerField(default=0,unique=True)
	room_type = models.CharField(max_length=1, choices=TYPES)
	