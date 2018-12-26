from django import forms
from Reservation.models import Reservations
import datetime



class Reserve_info(forms.ModelForm):
    Check_in_time = forms.DateField(required=True,)
    Check_out_time = forms.DateField(required=True)
    class Meta:
        model = Reservations
        fields = ('Check_in_time','Check_out_time',)
