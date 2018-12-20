from django.shortcuts import render
from Hotel.models import hotel
from django.http import HttpResponse
from .addHotelForm import HotelForm
from django.shortcuts import render
from Location.models import location
# Create your views here.

def addHotel(request):

    if request.method == 'POST':
        data = HotelForm(request.POST , request.FILES)
        if data.is_valid():
            dummy = hotel()
            dummy.name = data.cleaned_data['name']
            dummy.stars = data.cleaned_data['stars']
            dummy.image = data.cleaned_data['image']
            dummy.country = data.cleaned_data['country']
            dummy.city = data.cleaned_data['city']
            # getLocationID = location.objects.filter(country=data.cleaned_data['country'],city=data.cleaned_data['city'])
            # # insert a new location
            # if not getLocationID:
            #     newLocation = location()
            #     newLocation.country=data.cleaned_data['country']
            #     newLocation.city=data.cleaned_data['city']
            #     newLocation.save()
            #  #get thisn location id
            # getLocationID = location.objects.get(country=data.cleaned_data['country'], city=data.cleaned_data['city'])
            # dummy.location_id = getLocationID
            # dummy.save()
            dummy.save()
            return HttpResponse("Added Successfully!")
        else:
            return HttpResponse("error")
    form = HotelForm()
    return render(request,'Hotel/addHotel.html',{'form' : form})

def showHotels(request):
    all = hotel.objects.all()
    return render(request,'Hotel/showHotels.html',{'hotels':all})
