from django.contrib import admin
from django.contrib import messages

from .models import requests
from Hotel.models import hotel
from Room.models import room
newhotel=hotel()
newroom=room()

admin.site.site_header ='BROKER'
def accept_request(modeladmin, request, queryset):
    for requests in queryset:

        if hotel.objects.filter(name=requests.hotel_name).exists():
            messages.error(request,'Hotel '+requests.hotel_name+' Already Exists')
        else:
            newhotel=hotel(owner_id=requests.owner_id,name=requests.hotel_name,country=requests.country,city=requests.city,image=requests.image,stars=requests.stars)
            newhotel.save()
            numberofrooms=1
            for x in range(requests.singleRoomsCount):
                newroom=room(hotel_id=newhotel,image=requests.imageS,price=requests.singleRoomsPrice,number=numberofrooms,room_type='Single')
                numberofrooms+=1
                newroom.save()
            for x in range(requests.doubleRoomsCount):
                newroom = room(hotel_id=newhotel, image=requests.imageS, price=requests.doubleRoomsPrice, number=numberofrooms, room_type='Double')
                numberofrooms+=1
                newroom.save()
            requests.state='Accepted'
            messages.add_message(request, messages.INFO, 'Hotel '+requests.hotel_name+ ' is Successfully Accepted')
            requests.save()  
accept_request.short_descrption = 'Accept Selected Requests'

def reject_request(modeladmin, request, queryset):
    for requests in queryset:
        requests.state='Rejected'
        requests.save()
        messages.add_message(request, messages.INFO, 'Hotel '+requests.hotel_name+ ' is Successfully Rejected')
reject_request.short_description = 'Reject Selected Requests'

class RequestAdmin(admin.ModelAdmin):
    list_display = ['get_name','hotel_name', 'stars', 'image', 'singleRoomsCount','singleRoomsPrice','doubleRoomsCount','imageS','imageD','doubleRoomsPrice','country','city','state',]
    actions = [accept_request, reject_request, ]

    def get_name(self, obj):
        return obj.owner_id.user.first_name
    get_name.short_description = 'Owner Name'

admin.site.register(requests,RequestAdmin)