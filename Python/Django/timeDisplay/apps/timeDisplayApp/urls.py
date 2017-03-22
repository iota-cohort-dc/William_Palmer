
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^', views.index),
]
#the above line is making a reference to the urls.py file in timeDisplay/apps folder
