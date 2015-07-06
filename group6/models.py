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

    def __unicode__(self):
        return self.name_eng

class CategoriesProject(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    project_catagories = models.CharField(max_length=5, null=True)
    teacher =models.ManyToManyField(Teacher) #link to Student many to many

    def __unicode__(self):
        return self.project.name_eng

class ResearchProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    numberOfPeople = models.IntegerField(default = 1)

    def __unicode__(self):
        return self.project.name_eng

class OfferProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    priceOfMaterial = models.FloatField(default=0.00)
    priceOfOther = models.FloatField(default=0.00)

    def __unicode__(self):
        return self.project.name_eng

class ApproveProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    student = models.ForeignKey(Student) #link to Student one to one
    course = models.CharField(max_length=200)
    semesterEnd = models.CharField(max_length=200)
    yearEnd = models.CharField(max_length=200)
    credit = models.IntegerField(default = 3)

    def __unicode__(self):
        return self.project.name_eng

class TimeLineForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    day = models.IntegerField(default = 1)
    month = models.CharField(max_length=200)
    year= models.IntegerField(default = 1)
    note = models.TextField()

    def __unicode__(self):
        return self.project.name_eng

class StepInTimeLine(models.Model):
    timeline = models.ForeignKey(TimeLineForm) #Link to TimeLineForm entity Many to one
    numberOfProcess = models.IntegerField(default = 1)
    processDescription = models.CharField(max_length=200)
    month1 = models.BooleanField(default=False)
    month2 = models.BooleanField(default=False)
    month3 = models.BooleanField(default=False)
    month4 = models.BooleanField(default=False)
    month5 = models.BooleanField(default=False)
    month6 = models.BooleanField(default=False)
    month7 = models.BooleanField(default=False)
    month8 = models.BooleanField(default=False)
    month9 = models.BooleanField(default=False)
    month10 = models.BooleanField(default=False)
    month11 = models.BooleanField(default=False)
    month12 = models.BooleanField(default=False)

    def __unicode__(self):
        return self.timeline.project.name_eng + " (" + self.processDescription + ")"
