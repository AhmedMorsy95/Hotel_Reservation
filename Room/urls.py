from django.conf.urls import url
from django.urls import path, re_path
from . import views
from Customer.views import home

urlpatterns = [
    # r is regex , ^ is start , $ is the end
    url(r'^addRoom', views.addRoom , name='addRoom' ),
    path('home/', home, name='home'),
    #extract the integer
    #url(r'^(?P<album_id>[0-9]+)$', views.detail , name='detail' ),
]