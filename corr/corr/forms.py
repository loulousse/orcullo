from django import forms
from . models import *
from .models import Image
from django.contrib.auth import authenticate
from django.forms import fields, models
from django.forms.widgets import PasswordInput
from .models import  NewUser


class AccountAuthenticationForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid Login')

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image', 'details', 'price')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class ContinueForm(forms.ModelForm):
    class Meta:
        model = Continue
        fields = ('gender', 'age', 'address', 'email', 'number')





