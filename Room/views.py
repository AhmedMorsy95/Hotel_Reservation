from django.shortcuts import render
from Room.models import room
from django.http import HttpResponse
from .addRoomForm import RoomForm
from django.shortcuts import render

def addRoom(request):

     if request.method == 'POST':
         data = RoomForm(request.POST , request.FILES)
         if data.is_valid():
             dummy = room()
             dummy.image = data.cleaned_data['image']
             dummy.price = data.cleaned_data['price']
             dummy.hotel_id = data.cleaned_data['hotel_id']
             dummy.room_type = data.cleaned_data['room_type']
             dummy.number = data.cleaned_data['number']
             dummy.save()
             return HttpResponse("Added Successfully!")
         else:
             return HttpResponse("error")

     form = RoomForm()
     return render(request,'Room/addRoom.html',{'form' : form})
