from django.db import models
from Customer.models import customer
from Room.models import room

class Reservations(models.Model):
   # hotel_id = models.ForeignKey(hotel,on_delete=models.CASCADE , null=True)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    room_id =  models.ForeignKey(room, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    from_date = models.DateField('Date')
    to_date = models.DateField('Date')
