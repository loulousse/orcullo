from django.db import models
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    details = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)

    def __str__(self):
        return self.title
"""
class Date(models.Model):
    day = models.IntegerField()
    month = models.CharField(max_length=200)
    year = models.IntegerField()

    class meta:
        db_table 'Date'
"""
class Reservation(models.Model):
    Reservation_id = models.BigAutoField(primary_key=True, unique=True)
    Room_Name = models.CharField(max_length=150, blank=True)
    resDate = models.CharField(max_length=150, blank=True)
    resStartTime = models.CharField(max_length=150, blank=True)
    prefix = models.CharField(max_length=150,blank=True)
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    zip_code = models.IntegerField(blank=True)
    country = models.CharField(max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    add_Inquiry = models.CharField(max_length=150, blank=True)
    payment = models.FloatField(max_length=150, blank=True)


