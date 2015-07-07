#-*- coding: utf-8 -*-
from django.db import models
# Create your models here.
#!/usr/bin/env python
from django.db import models
from django.contrib.auth.models import User
from login.models import *

class WithdrawCure(models.Model):
    user        = models.ForeignKey(UserProfile)
    account_id  = models.CharField(max_length=255)
    disease     = models.CharField(max_length=255)
    hospital    = models.CharField(max_length=255)
    hospitalOfChoices = (
        ('0', 'ของทางราชการ'),
        ('1', 'เอกชน'),
    )
    hospitalOf  = models.CharField(max_length=1, choices=hospitalOfChoices)
    startDate   = models.DateField()
    stopDate    = models.DateField()
    value       = models.FloatField()
    valueChar   = models.CharField(max_length=255)
    numBill     = models.IntegerField()
    selfW       = models.CharField(max_length=1, default="")
    spouseW     = models.CharField(max_length=1, default="")
    fatherW     = models.CharField(max_length=1, default="")
    motherW     = models.CharField(max_length=1, default="")
    childW1     = models.CharField(max_length=1, default="")
    childW2     = models.CharField(max_length=1, default="")
    orderchildW1     = models.CharField(max_length=1, default="")
    orderchildW2     = models.CharField(max_length=1, default="")
    dateCommit  = models.DateTimeField(auto_now=True)

class WithdrawStudy(models.Model):
    user        = models.ForeignKey(UserProfile)
    account_id  = models.CharField(max_length=255)
    typeWithdrawChoices = (
        ('0', 'ตนเอง'),
        ('1', 'พ่อ'),
        ('2', 'แม่'),
        ('3', 'คู่สมรส'),
        ('4', 'ลูก'),
    )
    typeWithdraw    =  models.CharField(max_length=1, choices=typeWithdrawChoices)
    dateCommit      = models.DateTimeField(auto_now=True)

class Father(models.Model):
    user        = models.OneToOneField(UserProfile)
    title       = models.CharField(max_length=10)
    firstname   = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    pid         = models.CharField(max_length=20)

class Mother(models.Model):
    user        = models.OneToOneField(UserProfile)
    title       = models.CharField(max_length=10)
    firstname   = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    pid         = models.CharField(max_length=20)

class Spouse(models.Model):
    user        = models.OneToOneField(UserProfile)
    title       = models.CharField(max_length=10)
    firstname   = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    pid         = models.CharField(max_length=20)
    office      = models.CharField(max_length=255)
    position    = models.CharField(max_length=255)
    typeOfWorkChoices = (
        ('0', 'ไม่เป็นข้าราชการหรือลูกจ้าประจำ'),
        ('1', 'เป็นข้าราชการ'),
        ('2', 'ลูกจ้างประจำ'),
        ('3', 'พนักงานมหาวิทยาลัย'),
        ('4', 'เป็นพนักงานหรือลูกจ้างในรัฐวิสาหกิจ/หน่วยงานของทางราชการ ราชการส่วนท้องถิ่น กรุงเทพมหานคร องค์กรอิสระ อง์กรมหาชน หรือหน่วยงานอื่นใด'),
    )
    typeOfWork  = models.CharField(max_length=1, choices=typeOfWorkChoices, default="")
    memberWith  = models.CharField(max_length=255)

class Child(models.Model):
    user        = models.ForeignKey(UserProfile)
    title       = models.CharField(max_length=10)
    firstname   = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    pid         = models.CharField(max_length=20)
    birthDate   = models.DateField()
    orderF      = models.IntegerField()
    orderM      = models.IntegerField()
    disableChoices = (
        ('0', ''),
        ('1', 'เป็นบุตรที่ไร้ความสามารถหรือเสมือนไร้ความสามารถ'),
    )
    disable = models.CharField(max_length=1, choices=disableChoices)
    parentRelateChoices = (
        ('0', 'เป็นบิดาชอบด้วยกฎหมาย'),
        ('1', 'เป็นมารดา'),
        ('2', 'บุตรอยู่ในความปกครองของข้าพเจ้าโดยการสิ้นสุดขงการสมรส'),
        ('3', 'บุตรอยู่ในความอุปการะเลี้ยงดูของข้าพเจ้าเนื่องจากแยกกันอยู่ โดยมิได้หย่าขาดตามกฎหมาย'),
    )
    parentRelate = models.CharField(max_length=1, choices=parentRelateChoices)

class EditPresident (models.Model):
    presidentName   = models. CharField(max_length=255)
    position        = models. CharField(max_length=255)

class DataFromWeb(models.Model):
    user        = models.ForeignKey(UserProfile)
    date        = models.CharField(max_length=255)
    account_id  = models.CharField(max_length=50)
    price       = models.FloatField()
    priceChar   = models.CharField(max_length=255)

class Olddate(models.Model):
    date = models.CharField(max_length=255)