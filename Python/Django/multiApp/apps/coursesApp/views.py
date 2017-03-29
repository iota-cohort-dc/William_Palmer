from django.shortcuts import render, redirect
from . models import AddCourse
from . models import UsersCourses
from django.core.urlresolvers import reverse
from ..logRegApp.models import User
from django.db.models import Count

# Create your views here.
def index(request):
    context = {
    'courses': AddCourse.objects.all(),
    }
    # print AddCourse.objects.all(),
    return  render(request, 'coursesApp/index.html',context)



def AddCourseProcess(request):
    AddCourse.objects.create(name = request.POST['courseName'],description = request.POST['description'])
    print "+ "*20
    # print AddCourse.objects.all()

    return redirect(reverse('courses:index'))

def removeCourse(request, id):
    print id
    print "^^@@"*25
    context = {
    'courses': AddCourse.objects.get(id=id)
    }
    print "==+"*25
    print id
    return  render(request, 'coursesApp/delete.html',context)

def delete(request,id):
    AddCourse.objects.get(id=id).delete()
    return redirect(reverse('courses:index'))

def dontdelete(request):
    return redirect(reverse('courses:index'))

def usersCourses(request):
    User.objects.all()
    AddCourse.objects.all().annotate(num_users=Count('all_courses')),
    context ={
        'users':User.objects.all(),
        'courses': AddCourse.objects.all(),
    }
    print"="*22
    # print courses
    # print users
    return render(request, 'coursesApp/userCourses.html', context)

# def choose(request):


def registerUser(request):
	user = User.objects.get(id = request.POST['Users'])
	course = AddCourse.objects.get(id = request.POST['Courses'])
	login = UsersCourses.objects.create(user = user, course = course)
    # print "%"*25
    # print user
    # print course
    # print login
	return redirect(reverse('courses:usersCourses'))
