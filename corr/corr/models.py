from django.db import models
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.

class Image(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="media")
    details = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)

#    def __str__(self):
#        return self.title
    class meta:
        db_table = 'Image'

class Book(models.Model):
    id = models.AutoField(primary_key = True)
#    day = models.IntegerField()
#    month = models.CharField(max_length=200)
#    year = models.IntegerField()
    date =  models.DateField(blank=True, null=True)
    startTime = models.CharField(max_length=200)
    endTime = models.CharField(max_length=200)
    title = models.ForeignKey(
        Image, on_delete=models.CASCADE, null=True)
    prefix = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    class meta:
        db_table = 'Book'

class Continue(models.Model):
    id = models.AutoField(primary_key = True)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    class meta:
        db_table = 'Continue'






