from django.shortcuts import render
from Hotel.models import hotel
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.



def showHotels(request):
    all = hotel.objects.all()
    return render(request,'Hotel/showHotels.html',{'hotels':all})
