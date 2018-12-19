from django.conf.urls import url
from . import views 

urlpatterns = [
   
     url(r'^signup/$', views.signup, name='signup'),
     url(r'^login/$',views.login_Page, name='Login'),
     url(r'^logout/$',views.logout_Page,name='Logout')
]