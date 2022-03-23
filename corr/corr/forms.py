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
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"





