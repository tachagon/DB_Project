#-*- coding: utf-8 -*-
from django.db import models
from login.models import *
    
class Department(models.Model):
    #code  Nooooooooooo
    
    Department_ID = models.IntegerField(primary_key=True, max_length=10)
    Department_Name = models.CharField( max_length=100 )
    def __unicode__(self):
        return str(self.Department_ID )+"  "+  str(self.Department_Name )

class Course(models.Model):
    #code
    Course_ID = models.IntegerField(primary_key=True, max_length=15)
    Course_Name = models.CharField( max_length=100 , blank=True)
    Credit = models.IntegerField( max_length=10 , blank=True,null=True)
    def __unicode__(self):
        return str(self.Course_ID )
	
class Section(models.Model):
    Section = models.IntegerField(max_length=10, blank=True)
    Course_ID = models.ForeignKey(Course)
    classroom = models.CharField(max_length=20, blank=True)
    st_endTime = models.CharField(max_length=11, blank=True)
    T_name=models.CharField(max_length=30, blank=True)
    T_lastname=models.CharField(max_length=30, blank=True)
    shortname = models.CharField(max_length=60, blank=True)    
    date = models.CharField(max_length=9, blank=True)
    def __unicode__(self):
        return " Course "+str(self.Course_ID )+" Section "+str(self.Section)+" Time "+  str(self.st_endTime)+"  Teacher Name "+  str(self.T_name)
	
class Grade(models.Model):
    #code
    std_id = models.ForeignKey(Student)
    Course_ID = models.ForeignKey(Course)
    year        = models.IntegerField(max_length=10)
    term        = models.IntegerField(max_length=1)
    Grade = models.CharField( max_length=3)
    Section = models.ForeignKey(Section)
    check= models.CharField( max_length=20, blank=True)
    def __unicode__(self):
        return "Student "+str(self.std_id )+" Course "+str(self.Course_ID )+" Section "+str(self.Section)+" Year "+  str(self.year)+"  Term "+  str(self.term)

class Status(models.Model):
    #code nooooooooo
    std_id = models.ForeignKey(Student)
    state= models.CharField( max_length=40, blank=True)
    def __unicode__(self):
        return "Student "+str(self.std_id )+" State "+str(self.state )

class Teacher_Course(models.Model):
    #code nooooooooo
    shortname = models.ForeignKey(Teacher)
    Course_ID = models.ForeignKey(Course)
    Section = models.ForeignKey(Section)
    def __unicode__(self):
        return str(self.shortname  )+"  "+  str(self.Course_ID )+"  "+  str(self.Section )

	
class scheme(models.Model):
    #code nooooooooo
    Course_ID = models.ForeignKey(Course)
    schemeChoices = (
    ('0', 'ไม่มีในหลักสูตร'),  
    ('1', 'ปริญญาโท_หลักสูตร2ปี_แผน_ก_เเบบ_ก_2_ปกติ'),
    ('2', 'ปริญญาโท_หลักสูตร2ปี_แผน_ก_เเบบ_ก_2_สหกิจศึกษา'),
    ('3', 'ปริญญาเอก_หลักสูตร3ปี_แบบ_1.1'),
    ('4', 'ปริญญาเอก_หลักสูตร3ปี_แบบ_2.1'),
    ('5', 'ปริญญาเอก_หลักสูตร4ปี_แบบ_1.2'),
    ('6', 'ปริญญาเอก_หลักสูตร4ปี_แบบ_2.2')
    )
    scheme = models.CharField(max_length=1, choices=schemeChoices)
    def __unicode__(self):
        return str(self.Course_ID)+"  "+  str(self.scheme)
		
class viyanipon_adviser(models.Model):
    #code nooooooooo
    std_id = models.CharField(primary_key=True, max_length=13)
    teach_name = models.CharField(max_length=6)
    adviser = models.CharField(max_length=50)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.adviser)


	
class viyanipon_name(models.Model):
    #code nooooooooo
    std_id = models.CharField(primary_key=True, max_length=13)
    name = models.CharField(max_length=20)
    name_thai = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)


class viyanipon_project(models.Model):
    #code nooooooooo
    std_id = models.CharField(primary_key=True, max_length=13)
    project_name = models.CharField(max_length=6)
    name_day = models.IntegerField(max_length=2)
    name_month = models.CharField(max_length=50)
    name_year = models.IntegerField(max_length=4)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.name_day)+"  "+  str(self.name_month)+"  "+  str(self.name_year)
		
class viyanipon_test(models.Model):
    #code nooooooooo
    std_id = models.CharField(primary_key=True, max_length=13)
    test = models.CharField(max_length=6)
    test_day = models.IntegerField(max_length=2)
    test_month = models.CharField(max_length=50)
    test_year = models.IntegerField(max_length=4)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.test_day)+"  "+  str(self.test_month)+"  "+  str(self.test_year)
		
class viyanipon_testend(models.Model):
    #code nooooooooo
    std_id = models.CharField(primary_key=True, max_length=13)
    testend = models.CharField(max_length=6)
    testend_day = models.IntegerField(max_length=2)
    testend_month = models.CharField(max_length=50)
    testend_year = models.IntegerField(max_length=4)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.testend_day)+"  "+  str(self.testend_month)+"  "+  str(self.testend_year)


class date(models.Model):
    #code nooooooooo
    datee = models.CharField(max_length=20, blank=True)	
    def __unicode__(self):
        return str(self.datee)
    

class Viyanipon(models.Model):
    std_id = models.ForeignKey(Student)
    Teacher = models.CharField(max_length=100, blank=True)
    Offer_th= models.CharField(max_length=200, blank=True)
    Offer_en= models.CharField(max_length=200, blank=True)
    Test=models.CharField(max_length=20, blank=True)
    Advance_Test=models.CharField(max_length=20, blank=True)
    Protect_Test=models.CharField(max_length=20, blank=True)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.Offer_th)
