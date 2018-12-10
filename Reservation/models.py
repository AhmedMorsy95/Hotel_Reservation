from django.db import models

class Reservations(models.Model):
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # room_id =  models.ForeignKey(Rooms, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    from_date = models.DateTimeField('Date')
    to_date = models.DateTimeField('Date')
