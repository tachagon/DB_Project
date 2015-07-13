from django.db import models
from login.models import *

#model to store project data
class ProjectG6(models.Model):
    student = models.ManyToManyField(Student) #link to Student many to many
    teacher = models.ForeignKey(Teacher) #link to Teacher entity one to one
    name_thai = models.CharField(max_length=200) #name of project thai languages
    name_eng = models.CharField(max_length=200) #name of project english languages
    yearOfEducation = models.IntegerField(default = 1) #year of education for project
    objective = models.TextField() #objective of project
    reason = models.TextField() #reason of project
    scope = models.TextField() #scope of project
    benefit = models.TextField() #benefit of project

    def __unicode__(self): #pattern of data to show in admin page
        return self.name_eng

class CategoriesProject(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    project_catagories = models.CharField(max_length=5) #categories of project
    number = models.CharField(max_length=2) #number of project
    year = models.CharField(max_length=2) #year of education project
    semester = models.IntegerField(default=1) #semester of project
    teacher = models.ManyToManyField(Teacher) #link to Teacher many to many (Teacher that tester for this project)

    def __unicode__(self): #pattern of data to show in admin page
        return self.project.name_eng

class ResearchProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    numberOfPeople = models.IntegerField(default = 1) #number of student in project

    def __unicode__(self): #pattern of data to show in admin page
        return self.project.name_eng

class OfferProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    priceOfMaterial = models.FloatField(default=0.00) #price of material in project
    priceOfOther = models.FloatField(default=0.00) #price of other in project

    def __unicode__(self): #pattern of data to show in admin page
        return self.project.name_eng

class ApproveProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    student = models.ForeignKey(Student) #link to Student one to one
    course = models.CharField(max_length=200) #course of this project
    semesterEnd = models.CharField(max_length=200) #semester to end this project
    yearEnd = models.CharField(max_length=200) #year of education to end this project
    credit = models.IntegerField(default = 3) #credit of course

    def __unicode__(self): #pattern of data to show in admin page
        return self.project.name_eng

class TimeLineForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    day = models.IntegerField(default = 1) #start project day
    month = models.CharField(max_length=200) #start project month
    year= models.IntegerField(default = 1) #start project year
    note = models.TextField() #forms note

    def __unicode__(self): #pattern of data to show in admin page
        return self.project.name_eng

class StepInTimeLine(models.Model):
    timeline = models.ForeignKey(TimeLineForm) #Link to TimeLineForm entity Many to one
    numberOfProcess = models.IntegerField(default = 1) #number of process in forms timeline
    processDescription = models.CharField(max_length=200) #process description
    month1 = models.BooleanField(default=False) #month1 check box
    month2 = models.BooleanField(default=False) #month2 check box
    month3 = models.BooleanField(default=False) #month3 check box
    month4 = models.BooleanField(default=False) #month4 check box
    month5 = models.BooleanField(default=False) #month5 check box
    month6 = models.BooleanField(default=False) #month6 check box
    month7 = models.BooleanField(default=False) #month7 check box
    month8 = models.BooleanField(default=False) #month8 check box
    month9 = models.BooleanField(default=False) #month9 check box
    month10 = models.BooleanField(default=False) #month10 check box
    month11 = models.BooleanField(default=False) #month11 check box
    month12 = models.BooleanField(default=False) #month12 check box

    def __unicode__(self): #pattern of data to show in admin page
        return self.timeline.project.name_eng + " (" + self.processDescription + ")"

class NotificationProject(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity Many to one
    officer = models.ForeignKey(Officer) #link to Officer entity one to one (Officer that create notification)

    def __unicode__(self): #pattern of data to show in admin page
        return self.project.name_eng

class Message(models.Model):
    text = models.TextField() #message field
    user = models.ForeignKey(UserProfile) #user create message
    noti = models.ForeignKey(NotificationProject) #Link to NotificationProject entity Many to one
    pub_date = models.DateTimeField('date published') #first time create message
    pub_date_last = models.DateTimeField('last edit') #last time to edit message

    def __unicode__(self): #pattern of data to show in admin page
        return self.noti.project.name_eng + " (" + self.pub_date + ")"
