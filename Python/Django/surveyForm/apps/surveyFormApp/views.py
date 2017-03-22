# from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# from django.utils.crypto import get_random_string

# 1 tab indentation please!

def index(request):
    print "Louisiana"
    return render(request,'index.html')

def process(request):
    print "*"*10

    if 'count' in request.session:
        pass
    else:
        request.session['count']=0



    if request.method == 'POST': # method, not methods
        request.session['name']=request.POST['name']
        request.session['location']=request.POST['location']
        request.session['language']=request.POST['language']
        request.session['comments']=request.POST['comments']
        print request.session['name']
        print request.session['location']
        # request.session.['count']=0
        request.session['count'] += 1
        # request.session['count'] += 1 # you cannot += to count if count isn't set first
        # print request.session['count']
        return redirect('/surveyDone')

def surveyDone(request):
    return render(request, 'result.html')
