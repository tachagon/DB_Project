from django.db import models

# Create your models here.
class subporzaa(models.Model):
    subjectID = models.CharField(primary_key=True, max_length=9)
    subjectName = models.CharField(max_length=200)