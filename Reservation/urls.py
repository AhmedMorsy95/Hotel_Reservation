from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^reserve_info/([0-9]+)/$', views.reserve_info, name='reserve_info'),
]
