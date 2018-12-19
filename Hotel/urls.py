from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addHotel$', views.addHotel , name='addHotel' ),
    url(r'^showHotels$', views.showHotels , name='showHotels' ),
]