from django.shortcuts import render, redirect
import random
import datetime




def index(request):
    # session.clear()

    return render(request, "index.html")
