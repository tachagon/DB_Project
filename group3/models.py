#-*- coding: utf-8 -*-
from django.db import models
from login.models import *
import datetime, time
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
        
    def get_time_diff(self):
        if str(self.endTime) == '00:00:01':
            return ''
        else:
            t_start = str(self.startTime.hour)+':'+str(self.startTime.minute) # time that employee come to work.
            t_end = str(self.endTime.hour)+':'+str(self.endTime.minute) # time that employee go home
            diff_min = int(t_end.split(':')[1]) - int(t_start.split(':')[1])    # calculate differ value of come_time
            diff_hour = int(t_end.split(':')[0]) - int(t_start.split(':')[0])  # calculate differ value of back_time
            if diff_min < 0:
                diff_min = 60 - diff_min
            return str(diff_hour) + ':'+str(diff_min)