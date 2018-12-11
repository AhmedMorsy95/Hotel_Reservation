from django.shortcuts import render
from Customer.models import customer

from django.http import HttpResponse
from .customerForms import CustomerForm
from django.shortcuts import render

# Create your views here.

def index(request):

    if request.method == 'POST':
        data = CustomerForm(request.POST , request.FILES)
        if data.is_valid():
            dummy = customer()
            dummy.email = data.cleaned_data['email']
            dummy.password = data.cleaned_data['password']
            dummy.username = data.cleaned_data['username']
            dummy.mobile = data.cleaned_data['mobile']
            dummy.save()
            return HttpResponse("Added Successfully!")
        else:
            return HttpResponse("error")


    form = CustomerForm()
    return render(request,'Customer/index.html',{'form' : form})
