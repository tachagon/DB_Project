from django.db import models
from login.models import *

class ProjectG6(models.Model):
    student = models.ManyToManyField(Student) #link to Student many to many
    teacher = models.ForeignKey(Teacher) #link to Teacher entity one to one
    name_thai = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    yearOfEducation = models.IntegerField(default = 1)
    objective = models.TextField()
    reason = models.TextField()
    scope = models.TextField()
    benefit = models.TextField()

class ResearchProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    numberOfPeople = models.IntegerField(default = 1)

class OfferProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    priceOfMaterial = models.FloatField(default=0.00)
    priceOfOther = models.FloatField(default=0.00)

class ApproveProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    student = models.ForeignKey(Student) #link to Student one to one
    course = models.CharField(max_length=200)
    semesterEnd = models.CharField(max_length=200)
    yearEnd = models.CharField(max_length=200)
    credit = models.IntegerField(default = 3)
