from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *


from .forms import ImageForm

# Create your views here.

def home(request):
    date = Date.objects.all()
    context = {
        'date': date
    }
    return render(request, 'corr/home.html')

def userReservationList(request):
    return render(request, 'corr/userReservationList.html')

class latestReservation(View):
    
    def get(self, request):
        date = Date.objects.all()
        context = {
            'date': date
       }
        return render(request, 'corr/latestReservation.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                did=request.POST.get("date-Id")
                day=request.POST.get("d-day")
                month=request.POST.get("d-month")
                year=request.POST.get("d-year")
                startTime=request.POST.get("d-start")
                update_date = Date.objects.filter(id=did).update(day=day, month=month, year=year, startTime=startTime, endTime=endTime)
                print(update_date)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                did=request.POST.get("ddate-id")
                date=Date.objects.filter(id=did).delete()
                print('recorded deleted')

        return redirect('latest_reservation')

def create(request):
    return render(request, 'corr/create.html')

class res(View):
    def get(self, request):
        return render(request, 'corr/res.html')
    
    def post(self, request):
        form = DateForm(request.POST)
        day = request.POST.get("day")
        print(day)
        month = request.POST.get("month")
        print(month)
        year = request.POST.get("year")
        print(year)
        startTime = request.POST.get("startTime")
        print(startTime)
        endTime = request.POST.get("endTime")
        print(endTime)

        if form.is_valid():
            day = request.POST.get("day")
            month = request.POST.get("month")
            year = request.POST.get("year")
        
        form = Date(day = day, month = month, year = year, startTime=startTime, endTime=endTime)
        form.save()

        return redirect('reservation_info')

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
