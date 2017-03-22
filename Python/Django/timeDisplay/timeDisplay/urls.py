"""timeDisplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include #the inlcude after the comma needs to be added
# from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.timeDisplayApp.urls')),#the include in the parenthesis needs to be surrounded by quotes
]
#the above line is making a reference to the urls.py file in timeDisplay/apps/timeDsiplayApp folder
