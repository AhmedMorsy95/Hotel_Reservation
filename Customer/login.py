from django import forms as f
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer

class Login(f.ModelForm):
    user_name = f.CharField(max_length=70, help_text='Required a valid user name.')
    password = f.CharField(widget=f.PasswordInput, required=True, help_text='Required.')
    class Meta:
        model = User
        fields = ('user_name','password',)