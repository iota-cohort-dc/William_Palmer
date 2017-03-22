from django.conf.urls import url

# def method_to_run(request):
#     print "Whatever it says to do"
#     print "It is aware"
#     print "It is capable of planning and forthought"
#     print "Beware"

from.import views
urlpatterns = [
    url(r'^$', views.index)
]
