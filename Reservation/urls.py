from django.urls import path, re_path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('Interface/', views.Normal, name='Normal'),
    re_path(r'^$', RedirectView.as_view(url='admin'), name='admin'),
    re_path(r'^reserve_info/([0-9]+)/$', views.reserve_info, name='reserve_info'),
    path('Advance_Days/', views.time_advance, name='time_advance')
]
