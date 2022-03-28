from django.db import models
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

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



