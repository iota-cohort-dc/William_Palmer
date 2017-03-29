from django.shortcuts import render, redirect
from . models import AddCourse
# Create your views here.
def index(request):
    context = {
    'courses': AddCourse.objects.all(),
    }
    # print AddCourse.objects.all(),
    return  render(request, 'index.html',context)



def AddCourseProcess(request):
    AddCourse.objects.create(name = request.POST['courseName'],description = request.POST['description'])
    print "+ "*20
    # print AddCourse.objects.all()

    return redirect('/')

def removeCourse(request, id):
    print id
    context = {
    'courses': AddCourse.objects.get(id=id)
    }
    return  render(request, 'delete.html',context)

def delete(request,id):
    AddCourse.objects.get(id=id).delete()
    return redirect('/')

def dontdelete(request):
    return redirect('/')
