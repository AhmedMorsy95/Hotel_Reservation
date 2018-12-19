from django.contrib import admin

from .models import hotel


class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'image']

admin.site.register(hotel,HotelAdmin)