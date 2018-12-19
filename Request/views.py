from django.shortcuts import render
from Request.models import requests
from Owner.models import owner
from django.http import HttpResponse
from .addHotelForm import HotelForm
from django.shortcuts import render
from Hotel.models import hotel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/Owner/login/')
def addHotel(request):

    if request.method == 'POST':
        data = HotelForm(request.POST , request.FILES)
        if data.is_valid():
            dummy = requests()
            dummy.hotel_name = data.cleaned_data['hotel_name']
            dummy.stars = data.cleaned_data['stars']
            dummy.image = data.cleaned_data['image']
            dummy.country = data.cleaned_data['country']
            dummy.city = data.cleaned_data['city']
            current_user= request.user
            dummy.owner_id = owner.objects.get(user=current_user)

            dummy.save()
            return HttpResponse("Added Successfully!")
        else:
            return HttpResponse("error")
    form = HotelForm()
    return render(request,'Request/addHotel.html',{'form' : form})

def showHotels(request):
     current_user= request.user
     current_owner=owner.objects.get(user=current_user)
     all = requests.objects.filter(owner_id=current_owner)
     return render(request,'Request/showHotels.html',{'hotels':all})




