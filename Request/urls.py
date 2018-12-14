from django.conf.urls import url
from Request import views

urlpatterns = [
    # r is regex , ^ is start , $ is the end
    url(r'^$', views.index , name='index' ),
    #extract the integer
    #url(r'^(?P<album_id>[0-9]+)$', views.detail , name='detail' ),
]