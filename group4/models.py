#-*- coding: utf-8 -*-
from django.db import models
# Create your models here.
#!/usr/bin/env python
from django.db import models
from django.contrib.auth.models import User
from login.models import *

class Family(models.Model):
    user        = models.ForeignKey(UserProfile)
    firstname   = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    pid         = models.CharField( max_length=13)
    typeFamilyChoices = (
        ('1', 'พ่อ่'),
        ('2', 'แม่'),
        ('3', 'คู่สมรส'),
        ('4', 'ลูก'),
    )
    typeFamily = models.CharField(max_length=1, choices=typeFamilyChoices)
    def __unicode__(self):
        return self.firstname + " " + self.lastname + " " + self.user.firstname_en


class Withdraw(models.Model):
    user        = models.OneToOneField(UserProfile)
    account_id  = models.CharField(max_length=255)
    disease     = models.CharField(max_length=255)
    hospital    = models.CharField(max_length=255)
    hospitalOfChoices = (
        ('0', 'ของทางราชการ'),
        ('1', 'เอกชน'),
    )
    hospitalOf = models.CharField(max_length=1, choices=hospitalOfChoices)
    startDate   = models.DateField()
    stopData    = models.DateField()
    value       = models.FloatField()
    valueChar   = models.CharField(max_length=255)
    numBill     = models.IntegerField(max_length=10)
    credit      = models.FloatField()
    creditChar  = models.CharField(max_length=255)
    claimChoices = (
        ('0', ''),
        ('1', 'ตามสิทธิ'),
        ('2', 'เฉพาะส่วนที่ขาดอยู่จากสิทธิที่ได้รับจากหน่วยงานอื่น'),
        ('3', 'เฉพาะส่วนที่ขาดอยู่จากสัญญาประกันภัย'),
    )
    claim = models.CharField(max_length=1, choices=claimChoices)

    selfClaimChoices = (
        ('0', ''),
        ('1', 'ไม่มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่น'),
        ('2', 'มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นแต่เลือกใช้สิทธิจากทางราชการ'),
        ('3', 'มีสิทธิได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย'),
        ('4', 'เป็นผู้ใช้สิทธิเบิกค่ารักษาพยาบาลสำหรับบุตรแต่เพียงฝ่ายเดียว'),
    )
    selfClaim = models.CharField(max_length=1, choices=selfClaimChoices)

    familyClaimChoices = (
        ('0', ''),
        ('1', 'ไม่มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่น'),
        ('2', 'มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นแตค่ารักษาพยาบาลที่ได้รับต่ำกว่าสิทธิตามพระราชกฤษฎีกา'),
        ('3', 'มีสิทธิได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย'),
        ('4', 'มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นในฐานะเป็นผู้อาศัยสิทธิของผู้อื่น'),
    )
    familyClaim = models.CharField(max_length=1, choices=familyClaimChoices)
    typeWithdrawChoices = (
        ('0', 'ตนเอง'),
        ('1', 'พ่อ่'),
        ('2', 'แม่'),
        ('3', 'คู่สมรส'),
        ('4', 'ลูก'),
    )
    typeWithdraw = models.CharField(max_length=1, choices=typeWithdrawChoices)

class Spouse(models.Model):
    family      = models.OneToOneField(Family)
    office      = models.CharField(max_length=255)
    position    = models.CharField(max_length=255)


class Child(models.Model):
    family      = models.OneToOneField(Family)
    birthDate   = models.DateField()
    orderF      = models.IntegerField(max_length=10)
    orderM      = models.IntegerField(max_length=10)
    disableChoices = (
        ('0', ''),
        ('1', 'เป็นบุตรที่ไร้ความสามารถหรือเสมือนไร้ความสามารถ'),
    )
    disable = models.CharField(max_length=1, choices=disableChoices)

class DataFromWeb(models.Model):
    user = models.OneToOneField(UserProfile)
    date = models.DateField()
    account_id = models.CharField(max_length=50)
    price = models.FloatField()