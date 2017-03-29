from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# import bcrypt


# Create your views here.
def index(request):
    return render(request, 'index.html')
    pass

def r_process(request):
    data ={
        "first_name":request.POST['fname'],#the name in [] is the same as the name= in the input.
        "last_name":request.POST['lname'],
        "email":request.POST['email'],
        "pass":request.POST['pass'],
        "cpass":request.POST['cpass']
    }
    result = User.objects.validate(data)

    # this will pass the data above to the models.py file and since the objects = UserManager() was added to the User class, the UseManager class take the data and run the validate function. this now goes to the app level users.py file and runds the validate function in the UserManager class.
    #*******************************************
    # after the validate in the models.py file has run, we need to see what was returned, True will the user info, the tuple (True, user) adn False will return the tuple (False, errors). The result in the if/else statement below is the same result as above. The value of result is what is returned from the validate method in the UserManager class in models.py.
    if result[0]:
        request.session['user_id']=result[1].id
        #the result[1] is looking at the tuple of the (True, user) where [1] is the user, the second item in the list and [0] is the first value.
        return redirect("/success")
    else:
        for errors in result[1]:
            messages.error(request, errors)
        return redirect("/")
    #the "print return" prints the value True in the terminal and redirects the page to the index.html page.

def l_process(request):
    data = {
    'email':request.POST['email'],
    'pass':request.POST['pass'],
    }
    result = User.objects.l_process(data)
    # the l_process needs to be the same as function listed in the models.py file.

    if result[0]:
        request.session['user_id']=result[1].id
        return redirect("/success")
    else:
        for errors in result[1]:
            messages.error(request, errors)
        return redirect("/")

def success(request):
    try:
        user_obj = User.objects.get(id=request.session['user_id'])
        context = {"user": user_obj}
        return render(request, "success.html", context)
    except:
        return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")
