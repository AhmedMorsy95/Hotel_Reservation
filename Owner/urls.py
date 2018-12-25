from django.conf.urls import url
from . import views 

urlpatterns = [

#     url(r'^show_extension_requests/$', views.show_extension_requests, name='show_extension_requests'),
     url(r'^signup/$', views.signup, name='signup'),
     url(r'^login/$',views.login_Page, name='Login'),
     url(r'^logout/$',views.logout_Page,name='Logout'),
     url(r'^home/$', views.home, name='home'),
     url(r'^http://127.0.0.1:8000/Request/addHotel', views.direct, name='direct'),
     url(r'^http://127.0.0.1:8000/Request/showHotels', views.rdirect, name='rdirect'),
]
