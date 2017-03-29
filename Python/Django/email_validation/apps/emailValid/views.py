from django.shortcuts import render, redirect
from .models import Email
# Create your views here.
def index(request):
	return render(request, 'emailValid/index.html')

def success(request):
	results = Email.objects.validate(request.POST['email'])

	if results:
		context = {
		'flash': results[1],
		'emails': Email.objects.all()
		}
		return render(request, 'emailValid/success.html', context)
	else:
		context = {
		'false': "Email is not Valid!"
		}
		return render(request, 'emailValid/index.html', context)
