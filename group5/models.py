from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class studentG5(models.Model):
    studentID = models.CharField(primary_key=True, max_length=13)
    studentYear = models.IntegerField(default=0)

class Internship(models.Model):
    name_Internship = models.CharField(primary_key=True,max_length=50)
    add_Internship = models.CharField(max_length=200)
    Tel = models.CharField(max_length=20)
    Fax = models.CharField(max_length=20)

#2Table(student,Internship)
class StatusPetition(models.Model):
    NoPetition = models.IntegerField(primary_key=True,default=0)
    studentG5 = models.ForeignKey(studentG5)
    StatusPetition = models.CharField(max_length=50)
    Date= models.DateField()
    Date2= models.DateField()
    Internship = models.ForeignKey(Internship)
    send = models.CharField(max_length=20)
    to = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

class Estimate(models.Model):
    studentID = models.CharField(primary_key=True,max_length=13)
    image_estimate = models.ImageField(upload_to = "group5/image_estimate")
    image_time = models.ImageField(upload_to = "group5/image_time")
class Date(models.Model):
    studentID = models.CharField(primary_key=True,max_length=13)
    DateEnd = models.DateField();