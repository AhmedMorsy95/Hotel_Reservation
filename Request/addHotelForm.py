from django import forms
from Request.models import requests
from Owner.models import owner

class HotelForm(forms.ModelForm):
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)

    class Meta:
        model = requests
        fields = ('hotel_name', 'stars', 'image', 'singleRoomsCount','singleRoomsPrice','doubleRoomsCount','doubleRoomsPrice','imageS','imageD','country','city',)