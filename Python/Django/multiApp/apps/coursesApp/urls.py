from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^process$', views.process),
    # url(r'^surveyDone$', views.surveyDone),
    url(r'^$', views.index, name='index'),
    url(r'^AddCourse$', views.AddCourseProcess, name='AddCourse'),
    url(r'^removeCourse/(?P<id>\d+)$', views.removeCourse, name='removeCourse'),
    url(r'^dontdelete$', views.dontdelete, name='dontdelete'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^usersCourses$', views.usersCourses, name='usersCourses'),
    url(r'^registerUser$', views.registerUser, name='registerUser'),
]
