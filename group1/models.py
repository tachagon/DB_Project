from django.db import models
from login.models import UserProfile

# Create your models here.

class Category(models.Model):    	
    name = models.CharField(max_length=200)
	
    def __unicode__(self):
       return self.name

class Personal(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
	
    def __unicode__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    dept = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    number = models.CharField(max_length=10)
    number2 = models.CharField(max_length=10)
    detail1 = models.CharField(max_length=50)
    detail2 = models.CharField(max_length=50)
    detail3 = models.CharField(max_length=50)
    detail4 = models.CharField(max_length=50)
    docfile = models.FileField(upload_to='documents/%Y')
    added = models.CharField(max_length=50)
    addby = models.CharField(max_length=50)
    send_status = models.BooleanField(default=0)
    userProfile = models.ManyToManyField(UserProfile)

    def __unicode__(self):
        return self.name

class Document_modify(models.Model):
    modified = models.CharField(max_length=50)
    modifyby = models.CharField(max_length=50)
    document = models.ForeignKey(Document)

    def __unicode__(self):
        return self.modifyby

