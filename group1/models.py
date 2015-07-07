from django.db import models

# Create your models here.

class Category(models.Model):    	
    name = models.CharField(max_length=200)
    code_name = models.IntegerField(primary_key=True)
    depart = models.CharField(max_length=10)
	
    def __unicode__(self):
        return str(self.code_name)

class Personal(models.Model):
    code_name = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
	
    def __unicode__(self):
        return self.code_name

class Document(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
#   doc = models.CharField(max_length=10)
    personal = models.ManyToManyField(Personal)
    year = models.CharField(max_length=4)
    number = models.CharField(max_length=10)
    number2 = models.CharField(max_length=10)
    detail1 = models.CharField(max_length=50)
    detail2 = models.CharField(max_length=50)
    detail3 = models.CharField(max_length=50)
    detail4 = models.CharField(max_length=50)
    docfile = models.FileField(upload_to='static/documents/%Y')

    def __unicode__(self):
        return self.name


