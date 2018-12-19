from django.contrib import admin
from Room.models import room
from Hotel.models import hotel


class RoomAdmin(admin.ModelAdmin):
    list_display = ['get_hotelName', 'image', 'price', 'number', 'room_type', ]

    def get_hotelName(self, obj):
       return obj.hotel_id.name
    get_hotelName.short_description = 'Hotel Name'


admin.site.register(room, RoomAdmin)
