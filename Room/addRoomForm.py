from django import forms
from Room.models import room

class RoomForm(forms.ModelForm):
    class Meta:
        model =  room
        fields = ('hotel_id', 'price','room_type','number','image')