from django.conf.urls import url
from . import views 

app_name='music'
urlpatterns = [
    url(r'^$', views.index, name='home'),
]
