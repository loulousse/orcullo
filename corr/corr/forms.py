from django import forms
from . models import *
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image', 'details', 'price')

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
<<<<<<< HEAD
        fields = ('day', 'month', 'year')
"""

class ReservationForm(forms.ModelForm):  # Reservation Form
    class Meta:
        model = Reservation
        fields = "__all__"
=======
        fields = ('id', 'day', 'month', 'year', 'startTime', 'endTime', 'roomName',
                    'firstname', 'middlename', 'lastname')

>>>>>>> 63610305e2a54071b94f2b1c53c91dac3f6502a4
