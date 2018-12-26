from django import forms as f
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import customer

class Register(f.ModelForm):
    user_name = f.CharField(max_length=100, required=True, help_text='Required.')
    email = f.EmailField(max_length=70, help_text='Required a valid email address.')
    mobile = f.CharField(max_length=80, required=True, help_text='Required.')
    password = f.CharField(widget=f.PasswordInput, required=True, help_text='Required.')
    class Meta:
        model = User
        fields = ('user_name','email','mobile','password',)