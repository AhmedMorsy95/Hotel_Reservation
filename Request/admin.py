from django.contrib import admin
from django.contrib import messages

from .models import requests
from Hotel.models import hotel

newhotel=hotel()

def accept_request(modeladmin, request, queryset):
    for requests in queryset:
    	if hotel.objects.filter(name=requests.hotel_name).exists():
    		messages.error(request,'Hotel '+requests.hotel_name+' Already Exists')
    	else:
    		newhotel=hotel(name=requests.hotel_name,country=requests.country,city=requests.city,image=requests.image,stars=requests.stars)
    		newhotel.save()
    		requests.state='Accepted'
    		messages.add_message(request, messages.INFO, 'Hotel '+requests.hotel_name+ ' is Successfully Accepted')
    		requests.save()
  
accept_request.short_description = 'Accept Selected Requests'

def reject_request(modeladmin, request, queryset):
    for requests in queryset:
        requests.state='Rejected'
        requests.save()
        messages.add_message(request, messages.INFO, 'Hotel '+requests.hotel_name+ ' is Successfully Rejected')
reject_request.short_description = 'Reject Selected Requests'

class RequestAdmin(admin.ModelAdmin):
    list_display = ['get_name','hotel_name', 'stars', 'image', 'singleRoomsCount','singelRoomsPrice','doubleRoomsCount','doubleRoomsPrice','country','city','state',]
    actions = [accept_request, reject_request, ] 

    def get_name(self, obj):
        return obj.owner_id.user.first_name
    get_name.short_description = 'Owner Name'

admin.site.register(requests,RequestAdmin)