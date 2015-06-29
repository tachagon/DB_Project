#-*- coding: utf-8 -*-
from django.db import models
from login.models import *

# Create your models here.
class Prof2Lang(models.Model):
    # the professor ID is primary key
    profID = models.CharField(primary_key=True, max_length=10)
    # professor profile
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=80)
    shortName = models.CharField(max_length=3)

    tell = models.CharField(blank=True, max_length=15)
    email = models.EmailField(blank=True)
    sahakornAccount = models.CharField(blank=True, max_length=100)

    department = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)

    def __unicode__(self):
        return self.firstName + " " + self.lastName

class Subject(models.Model):
    subjectID = models.CharField(primary_key=True, max_length=9)
    subjectName = models.CharField(max_length=200)

    def __unicode__(self):
        return self.subjectName

class Section(models.Model):
    section = models.CharField(max_length=7)
    subject = models.ForeignKey(Subject)
    classroom = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()

    dateChoices = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('H', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday')
    )
    date = models.CharField(max_length=1, choices=dateChoices)

    def __unicode__(self):
        return self.section + " " + self.subject.subjectName

    class meta:
        unique_together = ('section', 'subject')

class Teach(models.Model):
    prof = models.ForeignKey(Prof2Lang, blank=True, null=True)
    subject = models.ForeignKey(Subject)
    section = models.ForeignKey(Section)

class HourlyEmployee(models.Model):
    user = models.OneToOneField(UserProfile)
    numberTaxpayment = models.CharField(max_length=20, blank=True, default="")  # เลขประจำตัวผู้เสียภาษี
    status = models.CharField(max_length=50, blank=True, default="")            # ตำแหน่ง
    employmentRate = models.FloatField(max_length=10, default=0.0)              # อัตรารายได้

    def __unicode__(self):
        return self.user.firstname_en + " " + self.user.lastname_en

class Work(models.Model):
    releaseDate = models.DateField(auto_now=True)   # วันที่เพิ่มข้อมูล
    startTime = models.TimeField()                      # เวลาเริ่มทำงาน
    endTime = models.TimeField()                        # เวลาเลิกงาน
    note = models.TextField(blank=True)                 # หมายเหตุ
    employee = models.ForeignKey(HourlyEmployee)        # เป็นของพนักงานคนใด
    day = models.DateTimeField(auto_now=True)
    class meta:
        unique_together = ('employee', 'id')