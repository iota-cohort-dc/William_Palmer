from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^r_process$', views.r_process, name='r_process'),
    url(r'^success$', views.success, name='success'),
    url(r'^l_process$', views.l_process, name='l_process'),
    url(r'^logout$', views.logout, name='logout'),

]