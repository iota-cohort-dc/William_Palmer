from django.conf.urls import url, include #the inlcude after the comma needs to be added
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.randomWordApp.urls')),#the include in the parenthesis needs to be surrounded by quotes
]
