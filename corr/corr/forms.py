from django import forms
from . models import *
from .models import Image

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image', 'details', 'price')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('date', 'startTime', 'endTime', 'roomName', 'prefix', 'firstname', 'middlename', 'lastname')

class ContinueForm(forms.ModelForm):
    class Meta:
        model = Continue
        fields = ('gender', 'age', 'address', 'email', 'number')





