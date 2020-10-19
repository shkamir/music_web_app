from django.conf.urls import url
from . import views 

app_name='music'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<id>[0-9]{1,})/$', views.ahang_detail, name='detail'),
]
