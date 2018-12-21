from django.contrib import admin
from django.contrib import messages
from .models import hotel
from Owner.models import owner


def SuspendThisHotel(modeladmin, request, queryset):
    for hotels in queryset:
        if hotels.is_suspended==1:
            messages.error(request,'Hotel '+hotels.name+' Already suspended')

    queryset.update(is_suspended=1)

SuspendThisHotel.short_descrption = 'Suspend this Hotel'


def unSuspendThisHotel(modeladmin, request, queryset):
    for hotels in queryset:
        if hotels.is_suspended == 0:
            messages.error(request, 'Hotel ' + hotels.name + ' Already Unsuspended')

    queryset.update(is_suspended=0)
unSuspendThisHotel_descrption = 'UnSuspend this Hotel'

class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_name','stars', 'image', 'rating','is_suspended']
    actions = [SuspendThisHotel,unSuspendThisHotel, ]

    def get_name(self, obj):
        return obj.owner_id.user.first_name
    get_name.short_description = 'Owner Name'

admin.site.register(hotel,HotelAdmin)
