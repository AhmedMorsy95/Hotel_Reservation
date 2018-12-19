from django.contrib import admin

from .models import hotel
from Owner.models import owner



class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_name','stars', 'image', 'rating']

    def get_name(self, obj):
        return obj.owner_id.user.first_name
    get_name.short_description = 'Owner Name'

admin.site.register(hotel,HotelAdmin)