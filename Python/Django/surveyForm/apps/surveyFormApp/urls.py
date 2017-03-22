from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # if you don't put a dollar sign here, it will accept anything! You have to put ^$ to accept nothing between the start and end of the url, e.g. if you want just localhost:8000/ use ^$, if you want ...:8000/abe use ^abe$
    url(r'^process$', views.process),
    url(r'^surveyDone$', views.surveyDone),
    url(r'^index$', views.index)
]
