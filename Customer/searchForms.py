from django import forms

class searchForm(forms.Form):
     country = forms.CharField(max_length=50)
     city = forms.CharField(max_length=50,required=False)
     stars = forms.IntegerField(required=False)