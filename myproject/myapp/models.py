from django.db import models
# Create your models here.
class Doctors(models.Model):
    image=models.URLField()
    name=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    experience=models.IntegerField(default=0)
    hospitalname=models.CharField(max_length=200)
    fee=models.IntegerField(default=0)
    rating=models.FloatField(default=0.0)
    email=models.EmailField(default='yellumahanthysaipavan@gmail.com')
class Blood(models.Model):
    image=models.URLField()
    bloodgroup=models.CharField(max_length=200)
    no_of_units_available=models.IntegerField(default=0)
    contact=models.IntegerField(default=0)
    email=models.EmailField(default='govardhansathvik83@gmail.com')
class Appointment(models.Model):
    username=models.CharField(max_length=200)
    Date_of_appointment=models.DateField()
    Docname=models.CharField(max_length=100)


