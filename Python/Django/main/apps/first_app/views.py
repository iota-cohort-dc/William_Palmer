from django.shortcuts import render, HttpResponse

def index(request):
    print "Hello, I am Dr. Frankenfurtter"
    return render(request, "first_app/index.html")

# Create your views here.
