from django.shortcuts import render
from Customer.models import customer
from Hotel.models import hotel
from django.http import HttpResponse
from .customerForms import CustomerForm
from django.shortcuts import render
from Room.models import room
from Customer.customerForms import forms
from Request.addHotelForm import HotelForm
from .searchForms import searchForm
from Location .models import  location

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

def home(request):
    all = hotel.objects.all()
    search = searchForm()
    if request.method == 'POST':
        data = searchForm(request.POST, request.FILES)
        if data.is_valid():
            countryfield = data.cleaned_data['country']
            all = hotel.objects.filter(country = countryfield)

            cityfield = data.cleaned_data['city']
            if cityfield:
                all = all.filter(city = cityfield)

            starsfield = data.cleaned_data['stars']
            if starsfield:
                all = all.filter(stars = starsfield)

            return render(request, 'Customer/home.html', {'hotels': all})

    return render(request,'Customer/home.html',{'hotels' : all, 'search' : search})

def reserve(request,id):
    all = hotel.objects.filter(pk=id)
    #all_rooms = room.objects.filter(hotel_id =id)
    #rooms = all_rooms[0]
    types = {'0':'single' , '1':"Double"}
    return render(request,'Customer/reserve.html',{'hotels' : all ,  'types':types})

    #return render(request,'Customer/reserve.html',{'hotels' : all , 'rooms' : rooms, 'types':types})


