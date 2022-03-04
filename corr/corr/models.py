from django.db import models
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    details = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)

    def __str__(self):
        return self.title

class Date(models.Model):
    id = models.AutoField(primary_key = True)
    day = models.IntegerField()
    month = models.CharField(max_length=200)
    year = models.IntegerField()
    startTime = models.CharField(max_length=200)
    endTime = models.CharField(max_length=200)


    class meta:
        db_table = 'Date'

