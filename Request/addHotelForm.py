from django import forms
from Request.models import request
from Owner.models import owner

class HotelForm(forms.ModelForm):
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)

    class Meta:
        model = request
        fields = ('hotel_name' , 'stars','image',)