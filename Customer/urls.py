from django.conf.urls import url
from Customer import views


urlpatterns = [
    # r is regex , ^ is start , $ is the end
    url(r'^$', views.index , name='index' ),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^reserve([0-9]+)/$', views.reserve, name='reserve'),

    #extract the integer
    #url(r'^(?P<album_id>[0-9]+)$', views.detail , name='detail' ),
]