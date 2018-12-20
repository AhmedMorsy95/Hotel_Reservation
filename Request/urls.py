from django.conf.urls import url
from . import views

urlpatterns = [
    # r is regex , ^ is start , $ is the end
    url(r'^addHotel$', views.addHotel , name='addHotel' ),
    url(r'^showHotels$', views.showHotels , name='showHotels' ),
]