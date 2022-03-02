from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *


from .forms import ImageForm

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

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'corr/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'corr/upload.html', {'form': form})

