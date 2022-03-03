from django import forms
from . models import *
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image', 'details', 'price')
"""
class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ('day', 'month', 'year')
"""