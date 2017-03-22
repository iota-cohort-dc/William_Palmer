from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
        return  render(request, 'index.html')

def ninjas(request):
        context = {
            'allNinjas' : True
        }
        return render(request, 'theNinjas.html', context)

def show(request, color):
        context = {
            'allNinjas': False,
            'color': color
        }
        return render(request, 'theNinjas.html', context)
