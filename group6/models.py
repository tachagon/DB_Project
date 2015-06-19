from django.db import models

class StudentG6(models.Model):
    student_id = models.CharField(max_length=13)
    firstname_thai = models.CharField(max_length=200)
    lastname_thai = models.CharField(max_length=200)
    firstname_eng = models.CharField(max_length=200)
    lastname_eng = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    main = models.CharField(max_length=200)
    year_admission = models.IntegerField(default = 1)
    address = models.TextField()
    tel = models.CharField(max_length=200)
    workplace = models.TextField()

class TeacherG6(models.Model):
    firstname_thai = models.CharField(max_length=200)
    lastname_thai = models.CharField(max_length=200)
    firstname_eng = models.CharField(max_length=200)
    lastname_eng = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    address = models.TextField()
    workplace = models.TextField()
    tel = models.CharField(max_length=200)
    tel_con = models.CharField(max_length=200)

class ProjectG6(models.Model):
    name_thai = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    yearOfEducation = models.IntegerField(default = 1)
    objective = models.TextField()
    reason = models.TextField()
    scope = models.TextField()
    benefit = models.TextField()

class ResearchProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    teacher = models.ForeignKey(TeacherG6) #link to Teacher entity one to one
    numberOfPeople = models.IntegerField(default = 1)

class OfferProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    teacher = models.ForeignKey(TeacherG6) #link to Teacher entity one to one
    student = models.ManyToManyField(StudentG6) #link to Student many to many
    priceOfMaterial = models.FloatField(default=0.00)
    priceOfOther = models.FloatField(default=0.00)

class ApproveProjectForm(models.Model):
    project = models.ForeignKey(ProjectG6) #Link to Project entity one to one
    teacher = models.ForeignKey(TeacherG6) #link to Teacher entity one to one
    student = models.ForeignKey(StudentG6) #link to Student one to one
    course = models.CharField(max_length=200)
    semesterEnd = models.CharField(max_length=200)
    yearEnd = models.CharField(max_length=200)
    credit = models.IntegerField(default = 3)
