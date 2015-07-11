#-*- coding: utf-8 -*-
from django.db import models
from login.models import *
import datetime, time
# Create your models here.
class Prof2Lang(models.Model):
    # the professor ID is primary key
    profID = models.CharField(primary_key=True, max_length=10)                      # 1. * profID
    # professor profile
    firstName = models.CharField(max_length=50)                                     # 2. * firstName
    lastName = models.CharField(max_length=80)                                      # 3. * lastName
    shortName = models.CharField(max_length=3)                                      # 4. * shortName

    tell = models.CharField(blank=True, max_length=15)                              # 5. tell
    email = models.EmailField(blank=True)                                           # 6. email
    sahakornAccount = models.CharField(blank=True, max_length=100, default=True)    # 7. sahakornAccount

    department = models.CharField(max_length=200, blank=True, default="")           # 8. department
    faculty = models.CharField(max_length=200, blank=True, default="")              # 9. faculty

    typeChoices = (
        ('0','อาจารย์ในภาควิชา'),
        ('1','อาจารย์นอกภาควิชา'),
        ('2','อาจารย์พิเศษ')
    )
    type = models.CharField(max_length=1, choices=typeChoices)                      # 10. * type ประเภทอาจารย์

    prefix_name_choices = (
        ('0', 'นาย'),       # Mr.
        ('1', 'นาง'),       # Mrs.
        ('2', 'นางสาว'),    # Miss.
        ('3', 'ดร.')        # Dr.
    )
    prefix_name  = models.CharField(max_length=1, choices=prefix_name_choices)      # 11. * คำนำหน้าชื่อ

    academic_position_choice = (
        ('0', ''),
        ('1', 'ผู้ช่วยศาสตราจารย์'),    # ตัวย่อไทย ผศ.  ตัวย่อแบบอเมริกา  Asst.Prof.   มาจาก Assistant Professor
        ('2', 'รองศาสตราจารย์'),     # ตัวย่อไทย รศ.  ตัวย่อแบบอเมริกา  Assoc.Prof.  มาจาก Associate Professor
        ('3', 'ศาสตราจารย์')          # ตัวย่อไทย ศ.   ตัวย่อแบบอเมริกา Prof.         มาจาก Professor
    )
    academic_position = models.CharField(max_length=1, choices=academic_position_choice)    # 12. ตำแหน่งทางวิชาการ

    def __unicode__(self):
        return self.firstName + " " + self.lastName

class Subject(models.Model):
    subjectID = models.CharField(primary_key=True, max_length=9)                # 1. รหัสวิชา
    subjectName = models.CharField(max_length=200)                              # 2. ชื่อวิชาภาษาอังกฤษ
    subjectName_th = models.CharField(max_length=200, default='')               # 3. ชื่อวิชาภาษาไทย

    def __unicode__(self):
        return self.subjectName

class Section(models.Model):
    section = models.CharField(max_length=7)                                    # 1. ชื่อ section เช่น S.1
    subject = models.ForeignKey(Subject)                                        # 2. วิชา (subject)
    classroom = models.CharField(max_length=20)                                 # 3. ห้องเรียน
    startTime = models.TimeField()                                              # 4. เวลาเริ่มเรียน
    endTime = models.TimeField()                                                # 5. เวลาเลิกเรียน

    dateChoices = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('H', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday')
    )
    date = models.CharField(max_length=1, choices=dateChoices)                  # 6. วันที่เรียน เช่น จันทร์

    def __unicode__(self):
        return self.section + " " + self.subject.subjectName

    class meta:
        unique_together = ('section', 'subject')

class Teach(models.Model):
    prof = models.ForeignKey(Prof2Lang, blank=True, null=True)                  # 1. อาจารย์ผู้สอน
    subject = models.ForeignKey(Subject)                                        # 2. วิชา
    section = models.ForeignKey(Section)                                        # 3. section
    termChoices = (
        ('', 'กรุณาเลือกภาคเรียน'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    term    = models.CharField(max_length=1, choices=termChoices, default='')   # 4. ภาคเรียน
    year    = models.CharField(max_length=4, default='')                        # 5. ปีการศึกษา

class HourlyEmployee(models.Model):
    user = models.OneToOneField(UserProfile)                                    # 1. UserProfile
    numberTaxpayment = models.CharField(max_length=20, blank=True, default="")  # 2. เลขประจำตัวผู้เสียภาษี
    status = models.CharField(max_length=50, blank=True, default="")            # 3. ตำแหน่ง
    employmentRate = models.FloatField(max_length=10, default=0.0)              # 4. อัตรารายได้

    def __unicode__(self):
        return self.user.firstname_en + " " + self.user.lastname_en

class Work(models.Model):
    releaseDate = models.DateField(auto_now=True)                               # 1. วันที่เพิ่มข้อมูล
    startTime = models.TimeField()                                              # 2. เวลาเริ่มทำงาน
    endTime = models.TimeField()                                                # 3. เวลาเลิกงาน
    note = models.TextField(blank=True)                                         # 4. หมายเหตุ
    employee = models.ForeignKey(HourlyEmployee)                                # 5. เป็นของพนักงานคนใด
    day = models.DateTimeField(auto_now=True)
    class meta:
        unique_together = ('employee', 'id')
        
    def get_time_diff(self):
        if (int(str(self.startTime.hour)) == 12) and ( int(str(self.endTime.hour)) > 12 ):
            diff_min = int(str(self.endTime.minute)) - 0    # calculate differ value of come_time
            diff_hour = int(str(self.endTime.hour)) - 13
        elif (int(str(self.startTime.hour)) < 12) and ( int(str(self.endTime.hour)) == 12 ):
            diff_min = 0 - int(str(self.startTime.minute))   # calculate differ value of come_time
            diff_hour = int(str(self.endTime.hour)) - int(str(self.startTime.hour))  # calculate differ value of back_time
        elif (int(str(self.startTime.hour)) == 12) and ( int(str(self.endTime.hour)) == 12 ):
            diff_min = 0
            diff_hour = 0
        else:
            diff_min = int(str(self.endTime.minute)) - int(str(self.startTime.minute))   # calculate differ value of come_time
            diff_hour = int(str(self.endTime.hour)) - int(str(self.startTime.hour))   # calculate differ value of back_time
        
        if diff_min < 0:
            diff_min = 60 + diff_min
            diff_hour = diff_hour - 1
        try:
            if int(str(self.endTime.hour)) > 12:
                diff_hour = diff_hour - 1
        except:
            pass
        return str(diff_hour) + ':'+str(diff_min)