from django import forms
import datetime
from .models import Reservations


class test_form(forms.ModelForm):
    advanced_days = forms.CharField(max_length=3, required=True)
    class Meta:
        model = Reservations
        fields = ('advanced_days',)