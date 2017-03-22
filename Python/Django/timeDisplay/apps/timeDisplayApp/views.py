from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    print datetime.datetime.now()
    context = {
        'currentTime': datetime.datetime.now()
    }
    return render(request,"index.html", context)
