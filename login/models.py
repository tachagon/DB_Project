#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    firstname_th = models.CharField(max_length=100)
    lastname_th = models.CharField(max_length=100)
    firstname_en = models.CharField(max_length=100)
    lastname_en = models.CharField(max_length=100)
    address = models.TextField()
    office = models.TextField()
    tel = models.CharField(max_length=20)
    departmentChoices = (
        ('0', 'วิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    )
    department = models.CharField(max_length=1, choices=departmentChoices)

    facultyChoices = (
        ('0', 'วิศวกรรมศาสตร์')
    )
    faculty = models.CharField(max_length=1, choices=facultyChoices)

    typeChoices = (
        ('0', 'Student'),
        ('1', 'Teacher'),
        ('2', 'Officer')
    )
    type = models.CharField(max_length=1, choices=typeChoices)

class Student(models.Model):
    userprofile = models.OneToOneField(UserProfile)
    std_id = models.CharField(max_length=13)
    schemeChoices = (
        ('0', 'หลักสูตรปรับปรุง Cpr.E 54'),
        ('1', 'หลักสูตรปรับปรุง EE 51'),
        ('2', 'หลักสูตรปรับปรุง ECE 55')
    )
    scheme = models.CharField(max_length=1, choices=schemeChoices)

    mainChoices = (
        ('0', 'Cpr.E'),
        ('1', 'G'),
        ('2', 'U'),
        ('3', 'C')
    )
    main = models.CharField(max_length=1, choices=mainChoices)

class Teacher(models.Model):
    userprofile = models.OneToOneField(UserProfile)
    shortname = models.CharField(max_length=3)
    position = models.CharField(max_length=100)

class Officer(models.Model):
    userprofile = models.OneToOneField(UserProfile)
    position = models.CharField(max_length=100)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username