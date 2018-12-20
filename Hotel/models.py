from django.db import models
from Owner.models import owner
# Create your models here.

class hotel(models.Model):
    owner_id = models.ForeignKey(owner, on_delete=models.CASCADE)
    country=models.CharField(max_length=50, null=True)
    city=models.CharField(max_length=50, null=True)
    id = models.AutoField(primary_key=True , null=False)
    name = models.CharField(max_length=50)
    rating = models.FloatField(null=True, blank=True, default=None)
    stars = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    rates_count = models.IntegerField(default=0)
    rates_sum = models.IntegerField(default=0)
