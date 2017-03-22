from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# 1 tab indentation please!

def index(request):
    print "Louisiana"
    return render(request,'index.html')

def rWord(request):
    print "*"*10

    if 'count' not in request.session:
        request.session['count']=1
        return render(request, "index.html")

    if request.method == 'POST': # method, not methods
        request.session['aRandomWord'] = get_random_string(length=14)
        print request.session['aRandomWord']
        # request.session.['count']=0
        request.session['count'] += 1
        # request.session['count'] += 1 # you cannot += to count if count isn't set first

        # print request.session['count']

        return redirect('/')
