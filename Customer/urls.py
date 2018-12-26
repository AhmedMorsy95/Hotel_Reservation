"""Hotel_Reservation_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url,include
from . import views
from Hotel.views import showHotels, addHotel
from Reservation.views import reserve_info

urlpatterns = [

    re_path(r'^confirm([0-9]+)/$', views.confirm, name='confirm'),
    path('show_reservations/', views.show_reservations, name='show_reservations'),
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('show/', showHotels, name='showHotels'),
    re_path(r'^Room/', include('Room.urls')),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^reserve([0-9]+)/$', views.reserve, name='reserve'),
    re_path(r'^reserve_room([0-9]+)/$', views.reserve_room, name='reserve_room'),
    re_path(r'^Reservation/', include('Reservation.urls')),
    # re_path(r'^Room/', include('Room.urls')),
    path('reserve_info/', reserve_info, name='reserve_info')
]
