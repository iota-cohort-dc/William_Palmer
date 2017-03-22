from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^process$', views.process),
    # url(r'^surveyDone$', views.surveyDone),
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas/(?P<color>\w+)$',views.show)
]
