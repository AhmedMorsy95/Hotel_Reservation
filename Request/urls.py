from django.conf.urls import url
from . import views

urlpatterns = [
    # r is regex , ^ is start , $ is the end
    url(r'^addHotel$', views.addHotel , name='addHotel' ),
    url(r'^showHotels$', views.showHotels , name='showHotels' ),
    #extract the integer
    #url(r'^(?P<album_id>[0-9]+)$', views.detail , name='detail' ),
]