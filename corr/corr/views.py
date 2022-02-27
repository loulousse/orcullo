from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *

# Create your views here.

def home(request):
    return render(request, 'corr/home.html')

def contact(request):
    return render(request, 'corr/contact.html')

def rooms(request):
    return render(request, 'corr/rooms.html')

def dashboard(request):
    return render(request, 'corr/dashboard.html')

def signin(request):
    return render(request, 'corr/signin.html')

def index(request):
    return render(request, 'corr/index.html')

def reservation(request):
    return render(request, 'corr/reservation.html')



