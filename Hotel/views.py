from django.shortcuts import render
from Hotel.models import hotel
from django.http import HttpResponse
from .addHotelForm import HotelForm
from django.shortcuts import render
from Location.models import location
from django.contrib.auth.models import User


def addHotel(request):

    if request.method == 'POST':
        data = HotelForm(request.POST , request.FILES)
        if data.is_valid():
            dummy = hotel()
            dummy.name = data.cleaned_data['name']
            dummy.stars = data.cleaned_data['stars']
            dummy.image = data.cleaned_data['image']

            getLocationID = location.objects.filter(country=data.cleaned_data['country'],city=data.cleaned_data['city'])
            # insert a new location
            if not getLocationID:
                newLocation = location()
                newLocation.country=data.cleaned_data['country']
                newLocation.city=data.cleaned_data['city']
                newLocation.save()
             #get thisn location id
            getLocationID = location.objects.get(country=data.cleaned_data['country'], city=data.cleaned_data['city'])
            dummy.location_id = getLocationID
            dummy.save()
            return HttpResponse("Added Successfully!")
        else:
            return HttpResponse("error")

    name = User.objects.get(username=request.user.username)
    form = HotelForm()
    return render(request,'Hotel/addHotel.html',{'form' : form,'fullname':name})

def showHotels(request):
    all = hotel.objects.all()
    name = User.objects.get(username=request.user.username)
    return render(request,'Hotel/showHotels.html',{'hotels':all,'fullname':name})
