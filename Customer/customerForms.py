
from django import forms
from  Customer.models import customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('username' , 'email' , 'password', 'mobile' ,)