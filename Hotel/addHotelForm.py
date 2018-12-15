from django import forms
from Hotel.models import hotel

class HotelForm(forms.ModelForm):
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    class Meta:
        model = hotel
        fields = ('name' , 'stars','image',)