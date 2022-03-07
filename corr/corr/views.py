from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View
from . forms import *
from . models import *


from .forms import ImageForm

# Create your views here.

def home(request):
    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, 'corr/home.html')

def userReservationList(request):
    return render(request, 'corr/userReservationList.html')

class latestReservation(View):
    
    def get(self, request):
        book = Book.objects.all()
        context = {
            'book': book
       }
        return render(request, 'corr/latestReservation.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print ('update profile button clicked')
                did=request.POST.get("book-Id")
                date=request.POST.get("d-date")
                startTime=request.POST.get("d-startTime")
                endTime=request.POST.get("d-endTime")
                roomName=request.POST.get("d-roomName")
                firstname=request.POST.get("d-firstname")
                middlename=request.POST.get("d-middlename")
                lastname=request.POST.get("d-lastname")

                update_book = Book.objects.filter(id=did).update(date=date, startTime=startTime, 
                endTime=endTime, roomName=roomName, firstname=firstname, middlename=middlename, lastname=lastname)
                print(update_book)

                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                did=request.POST.get("bbook-id")
                book=Book.objects.filter(id=did).delete()
                print('recorded deleted')

        return redirect('latest_reservation')

def create(request):
    return render(request, 'corr/create.html')

class res(View):
    def get(self, request):
        return render(request, 'corr/res.html')
    
    def post(self, request):
        form = BookForm(request.POST)
        date = request.POST.get("date")
        print(date)
        startTime = request.POST.get("startTime")
        print(startTime)
        endTime = request.POST.get("endTime")
        print(endTime)
        roomName = request.POST.get("roomName")
        print(roomName)
        prefix = request.POST.get("prefix")
        print(prefix)
        firstname = request.POST.get("firstname")
        print(firstname)
        middlename = request.POST.get("middlename")
        print(middlename)
        lastname = request.POST.get("lastname")
        print(lastname)

        if form.is_valid():
            date = request.POST.get("date")
            startTime = request.POST.get("startTime")
            endTime = request.POST.get("endTime")
            roomName = request.POST.get("roomName")
            prefix = request.POST.get("prefix")
            firstname = request.POST.get("firstname")
            middlename = request.POST.get("middlename")
            lastname = request.POST.get("lastname")
        
        form = Book(date = date, startTime=startTime, endTime=endTime, roomName=roomName,
                    prefix = prefix, firstname=firstname, middlename=middlename, lastname=lastname)
        form.save()

        return redirect('latest_reservation')

def upload(request):
    return render(request, 'corr/upload.html')

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
