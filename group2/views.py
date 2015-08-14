#-*- coding: utf-8 -*-
# !/usr/bin/env python
import datetime
import time
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group2.models import *
from django.views import generic
from login.models import *
from datetime import datetime
from django.utils import timezone
from datetime import datetime
from array import array
from django.db.models import Max
from django.template import RequestContext
from django import forms
from fpdf import FPDF

def getUserType(request):
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user = user)
        return userprofile.type
    except:
        return 'admin'

def profile(request):
    template = 'group2/profile.html'    # get template
    context = {}
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj}
        context['currentUser'] = currentUser

    except: # can't get a Student object
        context = {}

    if currentUser.type != '0':
        template = 'group2/search_student.html'
        return render(request, template, {})
		
    return render(
        request,
        template,
        context
    )
		
def data_student(request):
    template = 'group2/data_student.html'    # get template
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}
        context['currentUser'] = currentUser

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
	
def data_student_edit(request):
    template = 'group2/data_student_edit.html'    # get template
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}
        context['currentUser'] = currentUser

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
	
def get_data_student_edit(request):
    template = 'group2/data_student.html'    # get template
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj, 'studentCur': studentCur}
        context['currentUser'] = currentUser
        

    except: # can't get a Student object
        context = {}

    if 'term' in request.POST and request.POST['term']:
		term = request.POST['term']
		
		
    
    #DS = detailStudy(term=term)
    #DS.save()
		
    return render(
        request,
        template,
        context
    )
	
def search_student(request):
    
    if request.method == 'POST':
        search = request.POST["search"]
        try:
            template = "group2/profile.html"
            context = {}
            studentObj = Student.objects.all()
            
            studentCur = Student.objects.get(std_id = search)
            return HttpResponseRedirect(reverse("group2:profile_admin", args=[studentCur.std_id]))
        except:
            template = "group2/search_student.html"
            context = {}
            context["error"] = "โปรดตรวจสอบรหัสนักศึกษาใหม่อีกครั้ง"
            
        return render(
            request,
            template,
            context
        )
	
def profile_admin(request, id):
    template = "group2/profile.html"
    context = {}
    print id
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        context['currentUser'] = currentUser
        studentObj = Student.objects.get(std_id=id)
        context['studentObj'] = studentObj
        context['currentUser'] = currentUser
        print studentObj

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )

def viyanipon_admin(request, id):
    template = "group2/viyanipon.html"
    context = {}
    print id
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        context['currentUser'] = currentUser
        studentObj = Student.objects.get(std_id=id)
        context['studentObj'] = studentObj
        context['currentUser'] = currentUser
        print studentObj

    except: # can't get a Student object
        context = {}

    table_show=Viyanipon.objects.filter(std_id=studentObj) 
    context = {'table_show': table_show,'studentObj': studentObj}
    return render(
        request,
        template,
        context
    )


def admin_look_school_record(request, id):
    template = "group2/admin_look_school_record.html"
    context = {}
    print id
    

    studentObj = Student.objects.get(std_id=id)
    year_std=studentObj.std_id
    yn=int("25"+year_std[:2] )
    
    if Grade.objects.filter(std_id=studentObj,year=yn,term=1,check="อนุมัติ"):      
        number_table1=Grade.objects.filter(std_id=studentObj,year=yn,term=1,check="อนุมัติ")   
        grade_all_1=0
        credit_all_1=0

        for i in number_table1:
            if i.Grade=="A":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*4)
                credit_all_1=credit_all_1+i.Course_ID.Credit
     
            elif i.Grade=="B+":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*3.5)
                credit_all_1=credit_all_1+i.Course_ID.Credit

            elif i.Grade=="B":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*3)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            elif i.Grade=="C+":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*2.5)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            
            elif i.Grade=="C":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*2)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            elif i.Grade=="D+":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*1.5)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            elif i.Grade=="D":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*1)
                credit_all_1=credit_all_1+i.Course_ID.Credit           
            
            elif i.Grade=="F":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*0)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            else:
                credit_all_1=1

        term1=grade_all_1/float(credit_all_1)
        context = {'yn':yn,'number_table1': number_table1,'studentObj':studentObj,'term1':term1}
        
        
 #####################################################################################################################################################           
        if Grade.objects.filter(std_id=studentObj,year=yn+1,term=2,check="อนุมัติ" ):
            number_table2=Grade.objects.filter(std_id=studentObj,year=yn+1,term=2,check="อนุมัติ")
            grade_all_2=0
            credit_all_2=0
        
  
            for i in number_table2:
                if i.Grade=="A":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*4)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
     
                elif i.Grade=="B+":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*3.5)
                    credit_all_2=credit_all_2+i.Course_ID.Credit

                elif i.Grade=="B":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*3)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
                elif i.Grade=="C+":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*2.5)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
            
                elif i.Grade=="C":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*2)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
                elif i.Grade=="D+":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*1.5)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
                elif i.Grade=="D":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*1)
                    credit_all_2=credit_all_2+i.Course_ID.Credit           
            
                elif i.Grade=="F":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*0)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
                else:
                    credit_all_2=1

            term2=grade_all_2/float(credit_all_2)
            cumulative2= ((term1*credit_all_1)+(term2*credit_all_2))/float(credit_all_1+credit_all_2)
            cumulative2_string=str(cumulative2)
            cumulative2_string=cumulative2_string[:4] 
            context = {'yn':yn,'yn_1':yn+1,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string}
 
 #####################################################################################################################################################     
   
            if Grade.objects.filter(std_id=studentObj,year=yn+1,term=1,check="อนุมัติ"):
        
                    number_table3=Grade.objects.filter(std_id=studentObj,year=yn+1,term=1,check="อนุมัติ")
                    grade_all_3=0
                    credit_all_3=0
        
  
                    for i in number_table3:
                        if i.Grade=="A":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*4)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
     
                        elif i.Grade=="B+":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*3.5)
                            credit_all_3=credit_all_3+i.Course_ID.Credit

                        elif i.Grade=="B":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*3)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
                        elif i.Grade=="C+":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*2.5)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
            
                        elif i.Grade=="C":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*2)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
                        elif i.Grade=="D+":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*1.5)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
                        elif i.Grade=="D":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*1)
                            credit_all_3=credit_all_3+i.Course_ID.Credit           
            
                        elif i.Grade=="F":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*0)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
                        else:
                            credit_all_3=1

                    term3=grade_all_3/float(credit_all_3)
                    cumulative3= (  (cumulative2*(credit_all_1+credit_all_2))+(term3*credit_all_3)  )/float(credit_all_1+credit_all_2+credit_all_3)
                    cumulative3_string=str(cumulative3)
                    cumulative3_string=cumulative3_string[:4] 
                    context = {'yn':yn,'yn_1':yn+1,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3}
                    

 ###################################################################################################################################################    
                    if Grade.objects.filter(std_id=studentObj,year=yn+2,term=2,check="อนุมัติ"or "ดรอป"):
        
                        number_table4=Grade.objects.filter(std_id=studentObj,year=yn+2,term=2,check="อนุมัติ")
                        grade_all_4=0
                        credit_all_4=0
        
  
                        for i in number_table4:
                                if i.Grade=="A":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*4)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
     
                                elif i.Grade=="B+":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*3.5)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit

                                elif i.Grade=="B":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*3)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
                                elif i.Grade=="C+":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*2.5)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
            
                                elif i.Grade=="C":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*2)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
                                elif i.Grade=="D+":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*1.5)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
                                elif i.Grade=="D":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*1)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit           
            
                                elif i.Grade=="F":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*0)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
                                    
                                else:
                                    credit_all_4=1

                        term4=grade_all_4/float(credit_all_4)
                        cumulative4= (  (cumulative3*(credit_all_1+credit_all_2+credit_all_3))+(term4*credit_all_4)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4)
                        cumulative4_string=str(cumulative4)
                        cumulative4_string=cumulative4_string[:4] 
                        context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                   ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                   ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                   ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string}
                        
###################################################################################################################################################  
                              
                        if Grade.objects.filter(std_id=studentObj,year=yn+2,term=1,check="อนุมัติ"):
                                    number_table5=Grade.objects.filter(std_id=studentObj,year=yn+2,term=1,check="อนุมัติ")
                                    grade_all_5=0
                                    credit_all_5=0
        
  
                                    for i in number_table5:
                                        if i.Grade=="A":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*4)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
     
                                        elif i.Grade=="B+":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*3.5)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit

                                        elif i.Grade=="B":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*3)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
                                        elif i.Grade=="C+":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*2.5)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
            
                                        elif i.Grade=="C":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*2)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
                                        elif i.Grade=="D+":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*1.5)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
                                        elif i.Grade=="D":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*1)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit           
            
                                        elif i.Grade=="F":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*0)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
                                        
                                        else:
                                            credit_all_5=1

                                    term5=grade_all_5/float(credit_all_5)
                                    cumulative5= (  (cumulative4*(credit_all_1+credit_all_2+credit_all_3+credit_all_4))+(term5*credit_all_5)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5)
                                    cumulative5_string=str(cumulative5)
                                    cumulative5_string=cumulative5_string[:4] 
                                    context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                               ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                               ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string}
                                    

         ###################################################################################################################################################                               
                                    if Grade.objects.filter(std_id=studentObj,year=yn+3,term=2,check="อนุมัติ"):
                                            number_table6=Grade.objects.filter(std_id=studentObj,year=yn+3,term=2,check="อนุมัติ")
                                            grade_all_6=0
                                            credit_all_6=0
        
  
                                            for i in number_table6:
                                                if i.Grade=="A":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*4)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
     
                                                elif i.Grade=="B+":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*3.5)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit

                                                elif i.Grade=="B":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*3)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
                                                elif i.Grade=="C+":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*2.5)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
            
                                                elif i.Grade=="C":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*2)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
                                                elif i.Grade=="D+":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*1.5)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
                                                elif i.Grade=="D":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*1)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit           
            
                                                elif i.Grade=="F":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*0)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
                                                else:
                                                    credit_all_6=1

                                            term6=grade_all_6/float(credit_all_6)
                                            cumulative6= (  (cumulative5*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5))+(term6*credit_all_6)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6)
                                            cumulative6_string=str(cumulative6)
                                            cumulative6_string=cumulative6_string[:4] 
                                            context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                       ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                       ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                       ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                       ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string}
                                            

         ###################################################################################################################################################                               
      

                                            if Grade.objects.filter(std_id=studentObj,year=yn+3,term=1,check="อนุมัติ"):
        
                                                    number_table7=Grade.objects.filter(std_id=studentObj,year=yn+3,term=1,check="อนุมัติ")
                                                    grade_all_7=0
                                                    credit_all_7=0
        
  
                                                    for i in number_table7:
                                                        if i.Grade=="A":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*4)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
     
                                                        elif i.Grade=="B+":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*3.5)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit

                                                        elif i.Grade=="B":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*3)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
                                                        elif i.Grade=="C+":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*2.5)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
            
                                                        elif i.Grade=="C":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*2)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
                                                        elif i.Grade=="D+":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*1.5)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
                                                        elif i.Grade=="D":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*1)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit           
            
                                                        elif i.Grade=="F":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*0)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
                                                            
                                                        else:
                                                            credit_all_7=1

                                                    term7=grade_all_7/float(credit_all_7)
                                                    cumulative7= (  (cumulative6*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6))+(term7*credit_all_7)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7)
                                                    cumulative7_string=str(cumulative7)
                                                    cumulative7_string=cumulative7_string[:4] 
                                                    context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                               ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                               ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                               ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                               ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string}
                                                    

                                               ###################################################################################################################################################            
                                                    if Grade.objects.filter(std_id=studentObj,year=yn+4,term=2,check="อนุมัติ"):
        
                                                            number_table8=Grade.objects.filter(std_id=studentObj,year=yn+3,term=2,check="อนุมัติ")
                                                            grade_all_8=0
                                                            credit_all_8=0
        
  
                                                            for i in number_table8:
                                                                if i.Grade=="A":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*4)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
     
                                                                elif i.Grade=="B+":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*3.5)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit

                                                                elif i.Grade=="B":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*3)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
                                                                elif i.Grade=="C+":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*2.5)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
            
                                                                elif i.Grade=="C":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*2)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
                                                                elif i.Grade=="D+":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*1.5)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
                                                                elif i.Grade=="D":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*1)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit           
            
                                                                elif i.Grade=="F":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*0)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
                                                                else:
                                                                    credit_all_8=1

                                                            term8=grade_all_8/float(credit_all_8)
                                                            cumulative8= (  (cumulative7*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7))+(term8*credit_all_8)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8)
                                                            cumulative8_string=str(cumulative8)
                                                            cumulative8_string=cumulative8_string[:4] 
                                                            context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'yn_4':yn+4,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                                       ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                                       ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                                       ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                                       ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                                       ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string
                                                                       ,'number_table8': number_table8,'term8':term8,'cumulative8':cumulative8_string}
                                                            
                                                         
                                                 ###################################################################################################################################################               
                                                            if Grade.objects.filter(std_id=studentObj,year=yn+4,term=1,check="อนุมัติ"):
        
                                                                    number_table9=Grade.objects.filter(std_id=studentObj,year=yn+4,term=1,check="อนุมัติ")
                                                                    grade_all_9=0
                                                                    credit_all_9=0
        
  
                                                                    for i in number_table9:
                                                                        if i.Grade=="A":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*4)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
     
                                                                        elif i.Grade=="B+":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*3.5)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit

                                                                        elif i.Grade=="B":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*3)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
                                                                        elif i.Grade=="C+":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*2.5)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
            
                                                                        elif i.Grade=="C":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*2)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
                                                                        elif i.Grade=="D+":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*1.5)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
                                                                        elif i.Grade=="D":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*1)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit           
            
                                                                        elif i.Grade=="F":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*0)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
                                                                        else:
                                                                            credit_all_9=1

                                                                    term9=grade_all_9/float(credit_all_9)
                                                                    cumulative9= (  (cumulative8*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8))+(term9*credit_all_9)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8+credit_all_9)
                                                                    cumulative9_string=str(cumulative9)
                                                                    cumulative9_string=cumulative9_string[:4] 
                                                                    context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'yn_4':yn+4,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                                               ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                                               ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                                               ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                                               ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string
                                                                               ,'number_table8': number_table8,'term8':term8,'cumulative8':cumulative8_string
                                                                               ,'number_table9': number_table9,'term9':term9,'cumulative9':cumulative9_string}
                                                                    
                                                                    
                                                                        
                                                                         ################################################################################################################################################### 
                                                                    if Grade.objects.filter(std_id=studentObj,year=yn+5,term=2,check="อนุมัติ"or "ดรอป"):
                                                                            number_table10=Grade.objects.filter(std_id=studentObj,year=yn+5,term=2,check="อนุมัติ")
                                                                            grade_all_10=0
                                                                            credit_all_10=0
        
  
                                                                            for i in number_table10:
                                                                                if i.Grade=="A":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*4)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
     
                                                                                elif i.Grade=="B+":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*3.5)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit

                                                                                elif i.Grade=="B":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*3)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
                                                                                elif i.Grade=="C+":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*2.5)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
            
                                                                                elif i.Grade=="C":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*2)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
                                                                                elif i.Grade=="D+":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*1.5)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
                                                                                elif i.Grade=="D":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*1)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit           
            
                                                                                elif i.Grade=="F":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*0)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
                                                                                    
                                                                                else:
                                                                                    credit_all_10=1

                                                                            term10=grade_all_10/float(credit_all_10)
                                                                            cumulative10= (  (cumulative9*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8+credit_all_9))+(term10*credit_all_10)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8+credit_all_9+credit_all_10)
                                                                            cumulative10_string=str(cumulative10)
                                                                            cumulative10_string=cumulative10_string[:4] 
                                                                            context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'yn_4':yn+4,'yn_5':yn+5,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                                                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                                                       ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                                                       ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                                                       ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                                                       ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                                                       ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string
                                                                                       ,'number_table8': number_table8,'term8':term8,'cumulative8':cumulative8_string
                                                                                       ,'number_table9': number_table9,'term9':term9,'cumulative9':cumulative9_string
                                                                                       ,'number_table10': number_table10,'term10':term10,'cumulative10':cumulative10_string}
                                                                            
                                                                            
    return render(
        request,
        template,
        context
    )


	
def regis_result_admin(request, id):
    template = "group2/regis_result.html"
    context = {}
    print id
 
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        context['currentUser'] = currentUser
        studentObj = Student.objects.get(std_id=id)
        context['studentObj'] = studentObj
        context['currentUser'] = currentUser
        print studentObj

    except: # can't get a Student object
        context = {}

    date=time.strftime("%x")
    month,day,year = date.split("/")
    day=int(day)
    year=int(year)
    year=year+2543
    
    if (    ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or  ((month=="09" or month=="10")and( day >= 1 or day <= 31)) or  ((month=="11" )and( day >= 1 or day <= 2))   ):
             t=1
    elif(   (month=="01" and (day>=11 or day <= 31))    or  ((month=="02" or month=="03")and( day >= 1 or day <= 31))  or  ((month=="04" )and( day >= 1 or day <= 4))           ):
             t=2
             
    table_show1=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="อนุมัติ")
    table_show2=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="ไม่อนุมัติ")
    table_show3=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="ดรอป")
    table_show4=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="อนุมัติดรอป")
    context = {'table_show1': table_show1,'table_show2': table_show2,'table_show3': table_show3,'table_show4': table_show4,'studentObj':studentObj}
    return render(
        request,
        template,
        context
    )
	
	
def Add_register(request):
    template = 'group2/regis_result.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}

    
    if request.method == 'POST':
        
        c_id1=request.POST.get("c_id1", False);
        sec1=request.POST.get("sec1", False);
        
        c_id2=request.POST.get("c_id2", False);
        sec2=request.POST.get("sec2", False);
        
        c_id3=request.POST.get("c_id3", False);
        sec3=request.POST.get("sec3", False);
        
        
        
        c_id4=request.POST.get("c_id4", False);
        sec4=request.POST.get("sec4", False);
        
        date=time.strftime("%x")
        month,day,year = date.split("/")

        day=int(day)
        year=int(year)
        year=year+2543
    

        if ( month=="07" or month=="08")and( day >= 10 or day <= 31):
                t="1"
                    
                if c_id1!=False:

                        #have data
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1),Section=int(sec1))
                    if Grade.objects.filter(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t) ):
                        context['duplicate']= "duplicate"
                    else:    
                        
                        if c_id2==False:                               
                                user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                user_check1.save()
                                context['success_re']= "success_re"  
                

                        else:
                            course2 = Course.objects.get(Course_ID=int(c_id2))
                            section2 = Section.objects.get(Course_ID=int(c_id2),Section=int(sec2))
                            
                            if Grade.objects.filter(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t) ):
                               context['duplicate']= "duplicate"
                            else:   
                                if c_id3==False:
                                    user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                    user_check1.save()                                
                  

                                    user_check2=Grade(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='เรียน')
                                    user_check2.save()
                                    context['success_re']= "success_re"  
  
                                else:
                                    course3 = Course.objects.get(Course_ID=int(c_id3))
                                    section3 = Section.objects.get(Course_ID=int(c_id3),Section=int(sec3))
                                    if Grade.objects.filter(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t) ):
                                       context['duplicate']= "duplicate"
                                    else: 
                                
                                        if c_id4==False:

                                            user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                            user_check1.save()                                
                  

                                            user_check2=Grade(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='เรียน')
                                            user_check2.save()
                                    

                                            user_check3=Grade(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),check='เรียน')
                                            user_check3.save()
                                            context['success_re']= "success_re"  
                                        
                                        else:
                                            course4 = Course.objects.get(Course_ID=int(c_id4))
                                            section4 = Section.objects.get(Course_ID=int(c_id4),Section=int(sec4))
                                            if Grade.objects.filter(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t) ):
                                               context['duplicate']= "duplicate"
                                            else: 
                                        
                                                user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                                user_check1.save()                                
                  

                                                user_check2=Grade(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='เรียน')
                                                user_check2.save()
                                    

                                                user_check3=Grade(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),check='เรียน')
                                                user_check3.save()                                         
                                        
                                        

                                                user_check4=Grade(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t),check='เรียน')
                                                user_check4.save()
                                                context['success_re']= "succes_re"  
                   
      
        elif(   (month=="01" and (day>=11 or day <= 31))  or  (month=="02" and day ==1)           ):
                t="2"
                if c_id1!=False:

                        #have data
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1),Section=int(sec1))
                    if Grade.objects.filter(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t) ):
                        context['duplicate1']= "duplicate1"
                    else:    
                        
                        if c_id2==False:                               
                                user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                user_check1.save()
                                context['success_re']= "success_re"  
                

                        else:
                            course2 = Course.objects.get(Course_ID=int(c_id2))
                            section2 = Section.objects.get(Course_ID=int(c_id2),Section=int(sec2))
                            
                            if Grade.objects.filter(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t) ):
                               context['duplicate2']= "duplicate2"
                            else:   
                                if c_id3==False:
                                    user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                    user_check1.save()                                
                  

                                    user_check2=Grade(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='เรียน')
                                    user_check2.save()
                                    context['success_re']= "success_re"  
  
                                else:
                                    course3 = Course.objects.get(Course_ID=int(c_id3))
                                    section3 = Section.objects.get(Course_ID=int(c_id3),Section=int(sec3))
                                    if Grade.objects.filter(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t) ):
                                       context['duplicate3']= "duplicate3"
                                    else: 
                                
                                        if c_id4==False:

                                            user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                            user_check1.save()                                
                  

                                            user_check2=Grade(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='เรียน')
                                            user_check2.save()
                                    

                                            user_check3=Grade(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),check='เรียน')
                                            user_check3.save()
                                            context['success_re']= "success_re"  
                                        
                                        else:
                                            course4 = Course.objects.get(Course_ID=int(c_id4))
                                            section4 = Section.objects.get(Course_ID=int(c_id4),Section=int(sec4))
                                            if Grade.objects.filter(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t) ):
                                               context['duplicate4']= "duplicate4"
                                            else: 
                                        
                                                user_check1=Grade(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='เรียน')
                                                user_check1.save()                                
                  

                                                user_check2=Grade(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='เรียน')
                                                user_check2.save()
                                    

                                                user_check3=Grade(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),check='เรียน')
                                                user_check3.save()                                         
                                        
                                        

                                                user_check4=Grade(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t),check='เรียน')
                                                user_check4.save()
                                                context['success_re']= "succes_re"  
                          
                else:
            
                        context['error_date']= "error_date"    

    return render(
        request,
        template,
        context
    )

	
def registeration(request):
    template = 'group2/registeration.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/registeration.html'
        return render(request, template, {})
	

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )


def registeration_admin(request):
    template = 'group2/registeration_admin.html'    # get template
    context = {}


    return render(
        request,
        template,
        context
    )

def regis_result(request):
    template = 'group2/regis_result.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj
        context['currentUser'] = currentUser

    except: # can't get a Student object
        context = {}
    
    date=time.strftime("%x")
    month,day,year = date.split("/")
    day=int(day)
    year=int(year)
    year=year+2543
    
    if (    ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or  ((month=="09" or month=="10" or month=="11" or month=="12")and( day >= 1 or day <= 31))    ):
             t=1
    elif(   (month=="01" and (day>=11 or day <= 31))    or  ((month=="02" or month=="03" or month=="04" or month=="05")and( day >= 1 or day <= 31))             ):
             t=2
             
    table_show1=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="อนุมัติ")
    table_show2=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="ไม่อนุมัติ")
    table_show3=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="ดรอป")
    table_show4=Grade.objects.filter(std_id=studentObj,year=year,term=t ,check="อนุมัติดรอป")
    context = {'table_show1': table_show1,'table_show2': table_show2,'table_show3': table_show3,'table_show4': table_show4,'studentObj':studentObj}
    
    return render(
        request,
        template,
        context
    )
	
def search_course(request):
    
    if request.method == 'POST':
        search = request.POST["search"]
        try:
            template = "group2/school_record_admin.html"
            context = {}
            courseObj = Course.objects.get(Course_ID = search)
            return HttpResponseRedirect(reverse("group2:school_record_admin", args=[courseObj.Course_ID]))
        except:
            template = "group2/search_course.html"
            context = {}
            context["error"] = "โปรดตรวจสอบรหัสวิชาใหม่อีกครั้ง"
            
        return render(
            request,
            template,
            context
        )
	
def school_record_admin(request, id):
    template = "group2/school_record_admin.html"
    context = {}
    print id
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        context['currentUser'] = currentUser
        courseObj = Course.objects.get(Course_ID=id)
        gradeObj = Grade.objects.all()
        context['courseObj'] = courseObj
        context['gradeObj'] = gradeObj

    except: # can't get a Student object
        context = {}

    return render(
        request,
        template,
        context
    )
	
def school_record_admin_edit(request, id):
    template = "group2/school_record_admin.html"
    context = {}
    print id
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        context['currentUser'] = currentUser
        courseObj = Course.objects.get(Course_ID=id)
        gradeObj = Grade.objects.all()
        context['courseObj'] = courseObj
        context['gradeObj'] = gradeObj

    except: # can't get a Student object
        context = {}

    if 'grade' in request.POST and request.POST['grade']:
		grade = request.POST['grade']
		

    return render(
        request,
        template,
        context
    )
	

def school_record(request):
    template = 'group2/school_record.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/school_record_admin.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)


    except: # can't get a Student object
        context = {}

    date=time.strftime("%x")
    month,day,year = date.split("/")
    day=int(day)

    year_std=studentObj.std_id
    yn=int("25"+year_std[:2] )

    if (    ((month=="11" or month=="12" )  and  (day >= 3 and day <= 31 ) ) or  ( (month=="04" or month=="05" or month=="06" or month=="07" ) and (day >= 5 and day <= 31 ) )            ):#after drop 
        if Grade.objects.filter(std_id=studentObj,year=yn,term=1,check="ดรอป"):
            school_record1=Grade.objects.get(std_id=studentObj,year=yn,term=1,check="ดรอป")
            school_record1.check="อนุมัติ"
            school_record1.save()

        if Grade.objects.filter(std_id=studentObj,year=yn,term=2,check="ดรอป"):
            school_record2=Grade.objects.get(std_id=studentObj,year=yn,term=2,check="ดรอป")
            school_record2.check="อนุมัติ"
            school_record2.save()
            
        if Grade.objects.filter(std_id=studentObj,year=yn+1,term=1,check="ดรอป"):
            school_record3=Grade.objects.get(std_id=studentObj,year=yn+1,term=1,check="ดรอป")
            school_record3.check="อนุมัติ"
            school_record3.save()

        if Grade.objects.filter(std_id=studentObj,year=yn+1,term=2,check="ดรอป"):
            school_record4=Grade.objects.get(std_id=studentObj,year=yn+1,term=2,check="ดรอป")
            school_record4.check="อนุมัติ"
            school_record4.save()
            
        if Grade.objects.filter(std_id=studentObj,year=yn+2,term=1,check="ดรอป"):
            school_record5=Grade.objects.get(std_id=studentObj,year=yn+2,term=1,check="ดรอป")
            school_record5.check="อนุมัติ"
            school_record5.save()

        if Grade.objects.filter(std_id=studentObj,year=yn+2,term=2,check="ดรอป"):
            school_record6=Grade.objects.get(std_id=studentObj,year=yn+2,term=2,check="ดรอป")
            school_record6.check="อนุมัติ"
            school_record6.save()
            
        if Grade.objects.filter(std_id=studentObj,year=yn+3,term=1,check="ดรอป"):
            school_record7=Grade.objects.get(std_id=studentObj,year=yn+3,term=1,check="ดรอป")
            school_record7.check="อนุมัติ"
            school_record7.save()

        if Grade.objects.filter(std_id=studentObj,year=yn+3,term=2,check="ดรอป"):
            school_record8=Grade.objects.get(std_id=studentObj,year=yn+3,term=2,check="ดรอป")
            school_record8.check="อนุมัติ"
            school_record8.save()

        if Grade.objects.filter(std_id=studentObj,year=yn+4,term=1,check="ดรอป"):
            school_record9=Grade.objects.get(std_id=studentObj,year=yn+4,term=1,check="ดรอป")
            school_record9.check="อนุมัติ"
            school_record9.save()

        if Grade.objects.filter(std_id=studentObj,year=yn+4,term=2,check="ดรอป"):
            school_record10=Grade.objects.get(std_id=studentObj,year=yn+4,term=2,check="ดรอป")
            school_record10.check="อนุมัติ"
            school_record10.save()
            
    if Grade.objects.filter(std_id=studentObj,year=yn,term=1,check="อนุมัติ"):      
        number_table1=Grade.objects.filter(std_id=studentObj,year=yn,term=1,check="อนุมัติ")   
        grade_all_1=0
        credit_all_1=0

        for i in number_table1:
            if i.Grade=="A":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*4)
                credit_all_1=credit_all_1+i.Course_ID.Credit
     
            elif i.Grade=="B+":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*3.5)
                credit_all_1=credit_all_1+i.Course_ID.Credit

            elif i.Grade=="B":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*3)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            elif i.Grade=="C+":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*2.5)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            
            elif i.Grade=="C":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*2)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            elif i.Grade=="D+":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*1.5)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            
            elif i.Grade=="D":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*1)
                credit_all_1=credit_all_1+i.Course_ID.Credit           
            
            elif i.Grade=="F":
                grade_all_1=grade_all_1+(i.Course_ID.Credit*0)
                credit_all_1=credit_all_1+i.Course_ID.Credit
            else:
                credit_all_1=1

        term1=grade_all_1/float(credit_all_1)
        context = {'yn':yn,'number_table1': number_table1,'studentObj':studentObj,'term1':term1}
        
        
 #####################################################################################################################################################           
        if Grade.objects.filter(std_id=studentObj,year=yn+1,term=2,check="อนุมัติ" ):
            number_table2=Grade.objects.filter(std_id=studentObj,year=yn+1,term=2,check="อนุมัติ")
            grade_all_2=0
            credit_all_2=0
        
  
            for i in number_table2:
                if i.Grade=="A":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*4)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
     
                elif i.Grade=="B+":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*3.5)
                    credit_all_2=credit_all_2+i.Course_ID.Credit

                elif i.Grade=="B":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*3)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
                elif i.Grade=="C+":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*2.5)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
            
                elif i.Grade=="C":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*2)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
                elif i.Grade=="D+":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*1.5)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
            
                elif i.Grade=="D":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*1)
                    credit_all_2=credit_all_2+i.Course_ID.Credit           
            
                elif i.Grade=="F":
                    grade_all_2=grade_all_2+(i.Course_ID.Credit*0)
                    credit_all_2=credit_all_2+i.Course_ID.Credit
                else:
                    credit_all_2=1

            term2=grade_all_2/float(credit_all_2)
            cumulative2= ((term1*credit_all_1)+(term2*credit_all_2))/float(credit_all_1+credit_all_2)
            cumulative2_string=str(cumulative2)
            cumulative2_string=cumulative2_string[:4] 
            context = {'yn':yn,'yn_1':yn+1,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string}
 
 #####################################################################################################################################################     
   
            if Grade.objects.filter(std_id=studentObj,year=yn+1,term=1,check="อนุมัติ"):
        
                    number_table3=Grade.objects.filter(std_id=studentObj,year=yn+1,term=1,check="อนุมัติ")
                    grade_all_3=0
                    credit_all_3=0
        
  
                    for i in number_table3:
                        if i.Grade=="A":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*4)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
     
                        elif i.Grade=="B+":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*3.5)
                            credit_all_3=credit_all_3+i.Course_ID.Credit

                        elif i.Grade=="B":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*3)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
                        elif i.Grade=="C+":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*2.5)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
            
                        elif i.Grade=="C":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*2)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
                        elif i.Grade=="D+":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*1.5)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
            
                        elif i.Grade=="D":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*1)
                            credit_all_3=credit_all_3+i.Course_ID.Credit           
            
                        elif i.Grade=="F":
                            grade_all_3=grade_all_3+(i.Course_ID.Credit*0)
                            credit_all_3=credit_all_3+i.Course_ID.Credit
                        else:
                            credit_all_3=1

                    term3=grade_all_3/float(credit_all_3)
                    cumulative3= (  (cumulative2*(credit_all_1+credit_all_2))+(term3*credit_all_3)  )/float(credit_all_1+credit_all_2+credit_all_3)
                    cumulative3_string=str(cumulative3)
                    cumulative3_string=cumulative3_string[:4] 
                    context = {'yn':yn,'yn_1':yn+1,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3}
                    

 ###################################################################################################################################################    
                    if Grade.objects.filter(std_id=studentObj,year=yn+2,term=2,check="อนุมัติ"or "ดรอป"):
        
                        number_table4=Grade.objects.filter(std_id=studentObj,year=yn+2,term=2,check="อนุมัติ")
                        grade_all_4=0
                        credit_all_4=0
        
  
                        for i in number_table4:
                                if i.Grade=="A":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*4)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
     
                                elif i.Grade=="B+":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*3.5)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit

                                elif i.Grade=="B":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*3)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
                                elif i.Grade=="C+":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*2.5)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
            
                                elif i.Grade=="C":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*2)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
                                elif i.Grade=="D+":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*1.5)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
            
                                elif i.Grade=="D":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*1)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit           
            
                                elif i.Grade=="F":
                                    grade_all_4=grade_all_4+(i.Course_ID.Credit*0)
                                    credit_all_4=credit_all_4+i.Course_ID.Credit
                                    
                                else:
                                    credit_all_4=1

                        term4=grade_all_4/float(credit_all_4)
                        cumulative4= (  (cumulative3*(credit_all_1+credit_all_2+credit_all_3))+(term4*credit_all_4)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4)
                        cumulative4_string=str(cumulative4)
                        cumulative4_string=cumulative4_string[:4] 
                        context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                   ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                   ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                   ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string}
                        
###################################################################################################################################################  
                              
                        if Grade.objects.filter(std_id=studentObj,year=yn+2,term=1,check="อนุมัติ"):
                                    number_table5=Grade.objects.filter(std_id=studentObj,year=yn+2,term=1,check="อนุมัติ")
                                    grade_all_5=0
                                    credit_all_5=0
        
  
                                    for i in number_table5:
                                        if i.Grade=="A":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*4)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
     
                                        elif i.Grade=="B+":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*3.5)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit

                                        elif i.Grade=="B":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*3)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
                                        elif i.Grade=="C+":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*2.5)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
            
                                        elif i.Grade=="C":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*2)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
                                        elif i.Grade=="D+":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*1.5)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
            
                                        elif i.Grade=="D":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*1)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit           
            
                                        elif i.Grade=="F":
                                            grade_all_5=grade_all_5+(i.Course_ID.Credit*0)
                                            credit_all_5=credit_all_5+i.Course_ID.Credit
                                        
                                        else:
                                            credit_all_5=1

                                    term5=grade_all_5/float(credit_all_5)
                                    cumulative5= (  (cumulative4*(credit_all_1+credit_all_2+credit_all_3+credit_all_4))+(term5*credit_all_5)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5)
                                    cumulative5_string=str(cumulative5)
                                    cumulative5_string=cumulative5_string[:4] 
                                    context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                               ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                               ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string}
                                    

         ###################################################################################################################################################                               
                                    if Grade.objects.filter(std_id=studentObj,year=yn+3,term=2,check="อนุมัติ"):
                                            number_table6=Grade.objects.filter(std_id=studentObj,year=yn+3,term=2,check="อนุมัติ")
                                            grade_all_6=0
                                            credit_all_6=0
        
  
                                            for i in number_table6:
                                                if i.Grade=="A":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*4)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
     
                                                elif i.Grade=="B+":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*3.5)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit

                                                elif i.Grade=="B":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*3)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
                                                elif i.Grade=="C+":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*2.5)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
            
                                                elif i.Grade=="C":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*2)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
                                                elif i.Grade=="D+":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*1.5)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
            
                                                elif i.Grade=="D":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*1)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit           
            
                                                elif i.Grade=="F":
                                                    grade_all_6=grade_all_6+(i.Course_ID.Credit*0)
                                                    credit_all_6=credit_all_6+i.Course_ID.Credit
                                                else:
                                                    credit_all_6=1

                                            term6=grade_all_6/float(credit_all_6)
                                            cumulative6= (  (cumulative5*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5))+(term6*credit_all_6)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6)
                                            cumulative6_string=str(cumulative6)
                                            cumulative6_string=cumulative6_string[:4] 
                                            context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                       ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                       ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                       ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                       ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string}
                                            

         ###################################################################################################################################################                               
      

                                            if Grade.objects.filter(std_id=studentObj,year=yn+3,term=1,check="อนุมัติ"):
        
                                                    number_table7=Grade.objects.filter(std_id=studentObj,year=yn+3,term=1,check="อนุมัติ")
                                                    grade_all_7=0
                                                    credit_all_7=0
        
  
                                                    for i in number_table7:
                                                        if i.Grade=="A":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*4)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
     
                                                        elif i.Grade=="B+":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*3.5)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit

                                                        elif i.Grade=="B":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*3)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
                                                        elif i.Grade=="C+":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*2.5)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
            
                                                        elif i.Grade=="C":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*2)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
                                                        elif i.Grade=="D+":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*1.5)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
            
                                                        elif i.Grade=="D":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*1)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit           
            
                                                        elif i.Grade=="F":
                                                            grade_all_7=grade_all_7+(i.Course_ID.Credit*0)
                                                            credit_all_7=credit_all_7+i.Course_ID.Credit
                                                            
                                                        else:
                                                            credit_all_7=1

                                                    term7=grade_all_7/float(credit_all_7)
                                                    cumulative7= (  (cumulative6*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6))+(term7*credit_all_7)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7)
                                                    cumulative7_string=str(cumulative7)
                                                    cumulative7_string=cumulative7_string[:4] 
                                                    context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                               ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                               ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                               ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                               ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string}
                                                    

                                               ###################################################################################################################################################            
                                                    if Grade.objects.filter(std_id=studentObj,year=yn+4,term=2,check="อนุมัติ"):
        
                                                            number_table8=Grade.objects.filter(std_id=studentObj,year=yn+4,term=2,check="อนุมัติ")
                                                            grade_all_8=0
                                                            credit_all_8=0
        
  
                                                            for i in number_table8:
                                                                if i.Grade=="A":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*4)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
     
                                                                elif i.Grade=="B+":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*3.5)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit

                                                                elif i.Grade=="B":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*3)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
                                                                elif i.Grade=="C+":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*2.5)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
            
                                                                elif i.Grade=="C":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*2)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
                                                                elif i.Grade=="D+":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*1.5)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
            
                                                                elif i.Grade=="D":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*1)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit           
            
                                                                elif i.Grade=="F":
                                                                    grade_all_8=grade_all_8+(i.Course_ID.Credit*0)
                                                                    credit_all_8=credit_all_8+i.Course_ID.Credit
                                                                else:
                                                                    credit_all_8=1

                                                            term8=grade_all_8/float(credit_all_8)
                                                            cumulative8= (  (cumulative7*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7))+(term8*credit_all_8)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8)
                                                            cumulative8_string=str(cumulative8)
                                                            cumulative8_string=cumulative8_string[:4] 
                                                            context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'yn_4':yn+4,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                                       ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                                       ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                                       ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                                       ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                                       ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string
                                                                       ,'number_table8': number_table8,'term8':term8,'cumulative8':cumulative8_string}
                                                            
                                                         
                                                 ###################################################################################################################################################               
                                                            if Grade.objects.filter(std_id=studentObj,year=yn+4,term=1,check="อนุมัติ"):
        
                                                                    number_table9=Grade.objects.filter(std_id=studentObj,year=yn+4,term=1,check="อนุมัติ")
                                                                    grade_all_9=0
                                                                    credit_all_9=0
        
  
                                                                    for i in number_table9:
                                                                        if i.Grade=="A":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*4)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
     
                                                                        elif i.Grade=="B+":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*3.5)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit

                                                                        elif i.Grade=="B":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*3)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
                                                                        elif i.Grade=="C+":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*2.5)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
            
                                                                        elif i.Grade=="C":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*2)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
                                                                        elif i.Grade=="D+":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*1.5)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
            
                                                                        elif i.Grade=="D":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*1)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit           
            
                                                                        elif i.Grade=="F":
                                                                            grade_all_9=grade_all_9+(i.Course_ID.Credit*0)
                                                                            credit_all_9=credit_all_9+i.Course_ID.Credit
                                                                        else:
                                                                            credit_all_9=1

                                                                    term9=grade_all_9/float(credit_all_9)
                                                                    cumulative9= (  (cumulative8*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8))+(term9*credit_all_9)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8+credit_all_9)
                                                                    cumulative9_string=str(cumulative9)
                                                                    cumulative9_string=cumulative9_string[:4] 
                                                                    context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'yn_4':yn+4,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                                               ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                                               ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                                               ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                                               ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                                               ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                                               ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string
                                                                               ,'number_table8': number_table8,'term8':term8,'cumulative8':cumulative8_string
                                                                               ,'number_table9': number_table9,'term9':term9,'cumulative9':cumulative9_string}
                                                                    
                                                                    
                                                                        
                                                                         ################################################################################################################################################### 
                                                                    if Grade.objects.filter(std_id=studentObj,year=yn+5,term=2,check="อนุมัติ"or "ดรอป"):
                                                                            number_table10=Grade.objects.filter(std_id=studentObj,year=yn+5,term=2,check="อนุมัติ")
                                                                            grade_all_10=0
                                                                            credit_all_10=0
        
  
                                                                            for i in number_table10:
                                                                                if i.Grade=="A":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*4)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
     
                                                                                elif i.Grade=="B+":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*3.5)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit

                                                                                elif i.Grade=="B":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*3)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
                                                                                elif i.Grade=="C+":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*2.5)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
            
                                                                                elif i.Grade=="C":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*2)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
                                                                                elif i.Grade=="D+":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*1.5)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
            
                                                                                elif i.Grade=="D":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*1)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit           
            
                                                                                elif i.Grade=="F":
                                                                                    grade_all_10=grade_all_10+(i.Course_ID.Credit*0)
                                                                                    credit_all_10=credit_all_10+i.Course_ID.Credit
                                                                                    
                                                                                else:
                                                                                    credit_all_10=1

                                                                            term10=grade_all_10/float(credit_all_10)
                                                                            cumulative10= (  (cumulative9*(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8+credit_all_9))+(term10*credit_all_10)  )/float(credit_all_1+credit_all_2+credit_all_3+credit_all_4+credit_all_5+credit_all_6+credit_all_7+credit_all_8+credit_all_9+credit_all_10)
                                                                            cumulative10_string=str(cumulative10)
                                                                            cumulative10_string=cumulative10_string[:4] 
                                                                            context = {'yn':yn,'yn_1':yn+1,'yn_2':yn+2,'yn_3':yn+3,'yn_4':yn+4,'yn_5':yn+5,'number_table1': number_table1,'studentObj':studentObj,'term1':term1
                                                                                       ,'number_table2': number_table2,'term2':term2,'cumulative2':cumulative2_string
                                                                                       ,'term3':term3,'cumulative3':cumulative3_string,'number_table3': number_table3
                                                                                       ,'number_table4': number_table4,'term4':term4,'cumulative4':cumulative4_string
                                                                                       ,'number_table5': number_table5,'term5':term5,'cumulative5':cumulative5_string
                                                                                       ,'number_table6': number_table6,'term6':term6,'cumulative6':cumulative6_string
                                                                                       ,'number_table7': number_table7,'term7':term7,'cumulative7':cumulative7_string
                                                                                       ,'number_table8': number_table8,'term8':term8,'cumulative8':cumulative8_string
                                                                                       ,'number_table9': number_table9,'term9':term9,'cumulative9':cumulative9_string
                                                                                       ,'number_table10': number_table10,'term10':term10,'cumulative10':cumulative10_string}
                                                                            
                                                                            
    return render(
        request,
        template,
        context
    )
	

def Find_course(request):
    template = 'group2/registeration.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}

    
    if request.method == 'POST':

        c1=request.POST.get("c1", False);
        s1=request.POST.get("s1", False);

        c2=request.POST.get("c2", False);
        s2=request.POST.get("s2", False);
        
        c3=request.POST.get("c3", False);
        s3=request.POST.get("s3", False);
        
        c4=request.POST.get("c4", False);
        s4=request.POST.get("s4", False);
        
        
        date=time.strftime("%x")
        month,day,year = date.split("/")
        day=int(day)
        year=int(year)
        year=year+2543
        
        if ( month=="07" or month=="08")and( day >= 10 or day <= 31):
            t=1
            if c1!='':
               if Course.objects.filter(Course_ID=int(c1)):
                  course1 = Course.objects.get(Course_ID=int(c1))
                  if Section.objects.filter(Section=int(s1) ,Course_ID=course1):
                     number_table1=Section.objects.filter(Section=int(s1),Course_ID=course1  )
                     context={'number_table1': number_table1,'studentObj':studentObj}

            if c2!='' and c1!='':
               if Course.objects.filter(Course_ID=int(c2)):
                  course2 = Course.objects.get(Course_ID=int(c2))
                  if Section.objects.filter(Section=int(s2) ,Course_ID=course2):
                     number_table2=Section.objects.filter(Section=int(s2),Course_ID=course2  )
                     context={'number_table1': number_table1,'number_table2': number_table2,'studentObj':studentObj}
                     
            if c2!='' and c1!=''and c3!='':
               if Course.objects.filter(Course_ID=int(c3)):
                  course3 = Course.objects.get(Course_ID=int(c3))
                  if Section.objects.filter(Section=int(s3) ,Course_ID=course3):
                     number_table3=Section.objects.filter(Section=int(s3),Course_ID=course3  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'studentObj':studentObj}                     

            if c2!='' and c1!=''and c3!='' and c4!='':
               if Course.objects.filter(Course_ID=int(c4)):
                  course4 = Course.objects.get(Course_ID=int(c4))
                  if Section.objects.filter(Section=int(s4) ,Course_ID=course4):
                     number_table4=Section.objects.filter(Section=int(s4),Course_ID=course4  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'number_table4': number_table4,'studentObj':studentObj}                    
 
        elif(   (month=="01" and (day>=11 or day <= 31))  or  (month=="02" and day ==1)           ):
            t=2

            if c1!='':
               if Course.objects.filter(Course_ID=int(c1)):
                  course1 = Course.objects.get(Course_ID=int(c1))
                  if Section.objects.filter(Section=int(s1) ,Course_ID=course1):
                     number_table1=Section.objects.filter(Section=int(s1),Course_ID=course1  )
                     context={'number_table1': number_table1,'studentObj':studentObj}

            if c2!='' and c1!='':
               if Course.objects.filter(Course_ID=int(c2)):
                  course2 = Course.objects.get(Course_ID=int(c2))
                  if Section.objects.filter(Section=int(s2) ,Course_ID=course2):
                     number_table2=Section.objects.filter(Section=int(s2),Course_ID=course2  )
                     context={'number_table1': number_table1,'number_table2': number_table2,'studentObj':studentObj}
                     
            if c2!='' and c1!=''and c3!='':
               if Course.objects.filter(Course_ID=int(c3)):
                  course3 = Course.objects.get(Course_ID=int(c3))
                  if Section.objects.filter(Section=int(s3) ,Course_ID=course3):
                     number_table3=Section.objects.filter(Section=int(s3),Course_ID=course3  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'studentObj':studentObj}                     

            if c2!='' and c1!=''and c3!='' and c4!='':
               if Course.objects.filter(Course_ID=int(c4)):
                  course4 = Course.objects.get(Course_ID=int(c4))
                  if Section.objects.filter(Section=int(s4) ,Course_ID=course4):
                     number_table4=Section.objects.filter(Section=int(s4),Course_ID=course4  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'number_table4': number_table4,'studentObj':studentObj}   
                    
        else:
            context['error_date']= "error_date" 
    else:
        context = {}

    return render(
        request,
        template,
        context
    )



def Find_course_drop(request):
    template = 'group2/drop.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}

    
    if request.method == 'POST':

        c1=request.POST.get("c1", False);
        s1=request.POST.get("s1", False);

        c2=request.POST.get("c2", False);
        s2=request.POST.get("s2", False);
        
        c3=request.POST.get("c3", False);
        s3=request.POST.get("s3", False);
        
        c4=request.POST.get("c4", False);
        s4=request.POST.get("s4", False);
        
        
        date=time.strftime("%x")
        month,day,year = date.split("/")
        day=int(day)
        year=int(year)
        year=year+2543
        
        if (    ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or  ((month=="09" or month=="10")and( day >= 1 or day <= 31)) or  ((month=="11" )and( day >= 1 or day <= 2))   ):
            t=1
            if c1!='':
               if Course.objects.filter(Course_ID=int(c1)):
                  course1 = Course.objects.get(Course_ID=int(c1))
                  if Section.objects.filter(Section=int(s1) ,Course_ID=course1):
                     number_table1=Section.objects.filter(Section=int(s1),Course_ID=course1  )
                     context={'number_table1': number_table1,'studentObj':studentObj}

            if c2!='' and c1!='':
               if Course.objects.filter(Course_ID=int(c2)):
                  course2 = Course.objects.get(Course_ID=int(c2))
                  if Section.objects.filter(Section=int(s2) ,Course_ID=course2):
                     number_table2=Section.objects.filter(Section=int(s2),Course_ID=course2  )
                     context={'number_table1': number_table1,'number_table2': number_table2,'studentObj':studentObj}
                     
            if c2!='' and c1!=''and c3!='':
               if Course.objects.filter(Course_ID=int(c3)):
                  course3 = Course.objects.get(Course_ID=int(c3))
                  if Section.objects.filter(Section=int(s3) ,Course_ID=course3):
                     number_table3=Section.objects.filter(Section=int(s3),Course_ID=course3  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'studentObj':studentObj}                     

            if c2!='' and c1!=''and c3!='' and c4!='':
               if Course.objects.filter(Course_ID=int(c4)):
                  course4 = Course.objects.get(Course_ID=int(c4))
                  if Section.objects.filter(Section=int(s4) ,Course_ID=course4):
                     number_table4=Section.objects.filter(Section=int(s4),Course_ID=course4  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'number_table4': number_table4,'studentObj':studentObj}                    
 
        elif(   (month=="01" and (day>=11 or day <= 31))    or  ((month=="02" or month=="03")and( day >= 1 or day <= 31))  or  ((month=="04" )and( day >= 1 or day <= 4))           ):
            t=2

            if c1!='':
               if Course.objects.filter(Course_ID=int(c1)):
                  course1 = Course.objects.get(Course_ID=int(c1))
                  if Section.objects.filter(Section=int(s1) ,Course_ID=course1):
                     number_table1=Section.objects.filter(Section=int(s1),Course_ID=course1  )
                     context={'number_table1': number_table1,'studentObj':studentObj}

            if c2!='' and c1!='':
               if Course.objects.filter(Course_ID=int(c2)):
                  course2 = Course.objects.get(Course_ID=int(c2))
                  if Section.objects.filter(Section=int(s2) ,Course_ID=course2):
                     number_table2=Section.objects.filter(Section=int(s2),Course_ID=course2  )
                     context={'number_table1': number_table1,'number_table2': number_table2,'studentObj':studentObj}
                     
            if c2!='' and c1!=''and c3!='':
               if Course.objects.filter(Course_ID=int(c3)):
                  course3 = Course.objects.get(Course_ID=int(c3))
                  if Section.objects.filter(Section=int(s3) ,Course_ID=course3):
                     number_table3=Section.objects.filter(Section=int(s3),Course_ID=course3  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'studentObj':studentObj}                     

            if c2!='' and c1!=''and c3!='' and c4!='':
               if Course.objects.filter(Course_ID=int(c4)):
                  course4 = Course.objects.get(Course_ID=int(c4))
                  if Section.objects.filter(Section=int(s4) ,Course_ID=course4):
                     number_table4=Section.objects.filter(Section=int(s4),Course_ID=course4  )
                     context={'number_table1': number_table1,'number_table2': number_table2
                              ,'number_table3': number_table3,'number_table4': number_table4,'studentObj':studentObj}   
                    
        else:
            context['error_date']= "error_date" 
    else:
        context = {}

    return render(
        request,
        template,
        context
    )


def find_registeration_admin(request):
    template = 'group2/registeration_admin.html'    # get template
    context = {}
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)

    except: # can't get a Student object
        context = {}


    if request.method == 'POST':
        c1=request.POST["c1"]
        s1=request.POST["s1"]

    course = Course.objects.get(Course_ID=int(c_id))
    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))

    date=time.strftime("%x")
    month,day,year = date.split("/")
    day=int(day)
    year=int(year)
    year=year+2543

    if Grade.objects.filter(std_id=studentObj,Course_ID=course ,Section=secc  ):
        context['duplicate']= "duplicate" 
    else:
        if month=="07":
           if day >= 10 & day <= 31:
                t="1"
                grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc )
                grade_put.save()
        
                table_show=Grade.objects.filter(std_id=studentObj )
                context = {'table_show': table_show,'studentObj':studentObj}
           else:
            context['error_date']= "error_date" 
            
        elif month=="01":
            if day>=11 & day<= 31:
               t="2"
               grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc )
               grade_put.save()
        
               table_show=Grade.objects.filter(std_id=studentObj )
               context = {'table_show': table_show,'studentObj':studentObj}
            else:
                 context['error_date']= "error_date"
    
        elif month=="02":
             if day==1: 
                t="2"
                grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc )
                grade_put.save()
        
                table_show=Grade.objects.filter(std_id=studentObj )
                context = {'table_show': table_show,'studentObj':studentObj}
             else:
                 context['error_date']= "error_date" 
        else:
            context['error_date']= "error_date"
            

    return render(
        request,
        template,
        context
    )



def Update_check_admin(request):
    template = 'group2/registeration_admin.html'    # get template
    context = {}

    if request.method == 'POST':

        c_id=request.POST["c_id"]
        sec=request.POST["sec"]
        
        s_id1=request.POST.get("s_id1", False);
        state1=request.POST.get("state1", False);

        s_id2=request.POST.get("s_id2", False);
        state2=request.POST.get("state2", False);
        
        s_id3=request.POST.get("s_id3", False);
        state3=request.POST.get("state3", False);
    
        s_id4=request.POST.get("s_id4", False);
        state4=request.POST.get("state4", False);
        
        s_id5=request.POST.get("s_id5", False);
        state5=request.POST.get("state5", False);
        
        s_id6=request.POST.get("s_id6", False);
        state6=request.POST.get("state6", False);
        
        s_id7=request.POST.get("s_id7", False);
        state7=request.POST.get("state7", False);
        
        s_id8=request.POST.get("s_id8", False);
        state8=request.POST.get("state8", False);
    
        s_id9=request.POST.get("s_id9", False);
        state9=request.POST.get("state9", False);
        
        s_id10=request.POST.get("s_id10", False);
        state10=request.POST.get("state10", False);

        s_id11=request.POST.get("s_id11", False);
        state11=request.POST.get("state11", False);

        s_id12=request.POST.get("s_id12", False);
        state12=request.POST.get("state12", False);
        
        s_id13=request.POST.get("s_id13", False);
        state13=request.POST.get("state13", False);
    
        s_id14=request.POST.get("s_id14", False);
        state14=request.POST.get("state14", False);
        
        s_id15=request.POST.get("s_id15", False);
        state15=request.POST.get("state15", False);
        
        s_id16=request.POST.get("s_id16", False);
        state16=request.POST.get("state16", False);
        
        s_id17=request.POST.get("s_id17", False);
        state17=request.POST.get("state17", False);
        
        s_id18=request.POST.get("s_id18", False);
        state18=request.POST.get("state18", False);
    
        s_id19=request.POST.get("s_id19", False);
        state19=request.POST.get("state19", False);
        
        s_id20=request.POST.get("s_id20", False);
        state20=request.POST.get("state20", False);

        s_id21=request.POST.get("s_id21", False);
        state21=request.POST.get("state21", False);

        s_id22=request.POST.get("s_id22", False);
        state22=request.POST.get("state22", False);
        
        s_id23=request.POST.get("s_id23", False);
        state23=request.POST.get("state23", False);
    
        s_id24=request.POST.get("s_id24", False);
        state24=request.POST.get("state24", False);
        
        s_id25=request.POST.get("s_id25", False);
        state25=request.POST.get("state25", False);
        
        s_id26=request.POST.get("s_id26", False);
        state26=request.POST.get("state26", False);
        
        s_id27=request.POST.get("s_id27", False);
        state27=request.POST.get("state27", False);
        
        s_id28=request.POST.get("s_id28", False);
        state28=request.POST.get("state28", False);
    
        s_id29=request.POST.get("s_id29", False);
        state29=request.POST.get("state29", False);
        
        s_id30=request.POST.get("s_id30", False);
        state30=request.POST.get("state30", False);
        
        s_id31=request.POST.get("s_id31", False);
        state31=request.POST.get("state31", False);

        s_id32=request.POST.get("s_id32", False);
        state32=request.POST.get("state32", False);
        
        s_id33=request.POST.get("s_id33", False);
        state33=request.POST.get("state33", False);
    
        s_id34=request.POST.get("s_id34", False);
        state34=request.POST.get("state34", False);
        
        s_id35=request.POST.get("s_id35", False);
        state35=request.POST.get("state35", False);
        
        s_id36=request.POST.get("s_id36", False);
        state36=request.POST.get("state36", False);
        
        s_id37=request.POST.get("s_id37", False);
        state37=request.POST.get("state37", False);
        
        s_id38=request.POST.get("s_id38", False);
        state38=request.POST.get("state38", False);
    
        s_id39=request.POST.get("s_id39", False);
        state39=request.POST.get("state39", False);
        
        s_id40=request.POST.get("s_id40", False);
        state40=request.POST.get("state40", False);

      
        date=time.strftime("%x")
        month,day,year = date.split("/")

        day=int(day)
        year=int(year)
        year=year+2543
    

        if ( ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or ((month=="09")and(day == 1))              ):
            t="1"
             
            course = Course.objects.get(Course_ID=int(c_id))
            section = Section.objects.get(Course_ID=course,Section=int(sec) )
            
            if s_id1!=False:                
                student1 = Student.objects.get(std_id=s_id1)           
                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check1.check= state1
                admin_check1.save()
                
            if s_id2!=False:                
                student2 = Student.objects.get(std_id=s_id2)         
                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check2.check= state2
                admin_check2.save()            
                
            if s_id3!=False:                
                student3 = Student.objects.get(std_id=s_id3)         
                admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check3.check= state3
                admin_check3.save()
                
            if s_id4!=False:                
                student4 = Student.objects.get(std_id=s_id4)         
                admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check4.check= state4
                admin_check4.save()
                
            if s_id5!=False:                
                student5 = Student.objects.get(std_id=s_id5)         
                admin_check5=Grade.objects.get(std_id=student5 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check5.check= state5
                admin_check5.save()
                
            if s_id6!=False:                
                student6 = Student.objects.get(std_id=s_id6)         
                admin_check6=Grade.objects.get(std_id=student6 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check6.check= state6
                admin_check6.save()
                            
            if s_id7!=False:                
                student7 = Student.objects.get(std_id=s_id7)         
                admin_check7=Grade.objects.get(std_id=student7 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check7.check= state7
                admin_check7.save()
                
            if s_id8!=False:                
                student8 = Student.objects.get(std_id=s_id8)         
                admin_check8=Grade.objects.get(std_id=student8 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check8.check= state8
                admin_check8.save()
                
            if s_id9!=False:                
                student9 = Student.objects.get(std_id=s_id9)         
                admin_check9=Grade.objects.get(std_id=student9 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check9.check= state9
                admin_check9.save()
                
            if s_id10!=False:                
                student10 = Student.objects.get(std_id=s_id10)         
                admin_check10=Grade.objects.get(std_id=student10 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check10.check= state10
                admin_check10.save()

            if s_id11!=False:                
                student11 = Student.objects.get(std_id=s_id11)           
                admin_check11=Grade.objects.get(std_id=student11 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check11.check= state11
                admin_check11.save()
                
            if s_id12!=False:                
                student12 = Student.objects.get(std_id=s_id12)         
                admin_check12=Grade.objects.get(std_id=student12 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check12.check= state12
                admin_check12.save()            
                
            if s_id13!=False:                
                student13 = Student.objects.get(std_id=s_id13)         
                admin_check13=Grade.objects.get(std_id=student13 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check13.check= state13
                admin_check13.save()
                
            if s_id14!=False:                
                student14 = Student.objects.get(std_id=s_id14)         
                admin_check14=Grade.objects.get(std_id=student14 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check14.check= state14
                admin_check14.save()
                
            if s_id15!=False:                
                student15 = Student.objects.get(std_id=s_id15)         
                admin_check15=Grade.objects.get(std_id=student15 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check15.check= state15
                admin_check15.save()
                
            if s_id16!=False:                
                student16 = Student.objects.get(std_id=s_id16)         
                admin_check16=Grade.objects.get(std_id=student16 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check16.check= state16
                admin_check16.save()
                            
            if s_id17!=False:                
                student17 = Student.objects.get(std_id=s_id17)         
                admin_check17=Grade.objects.get(std_id=student17 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check17.check= state17
                admin_check17.save()
                
            if s_id18!=False:                
                student18 = Student.objects.get(std_id=s_id18)         
                admin_check18=Grade.objects.get(std_id=student18 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check18.check= state18
                admin_check18.save()
                
            if s_id19!=False:                
                student19 = Student.objects.get(std_id=s_id19)         
                admin_check19=Grade.objects.get(std_id=student19 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check19.check= state19
                admin_check19.save()
                
            if s_id20!=False:                
                student20 = Student.objects.get(std_id=s_id20)         
                admin_check20=Grade.objects.get(std_id=student20 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check20.check= state20
                admin_check20.save()              
                
            if s_id21!=False:                
                student21 = Student.objects.get(std_id=s_id21)           
                admin_check21=Grade.objects.get(std_id=student21 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check21.check= state21
                admin_check21.save()
                
            if s_id22!=False:                
                student22 = Student.objects.get(std_id=s_id22)         
                admin_check22=Grade.objects.get(std_id=student22 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check22.check= state22
                admin_check22.save()            
                
            if s_id23!=False:                
                student23 = Student.objects.get(std_id=s_id23)         
                admin_check23=Grade.objects.get(std_id=student23 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check23.check= state23
                admin_check23.save()
                
            if s_id24!=False:                
                student24 = Student.objects.get(std_id=s_id24)         
                admin_check24=Grade.objects.get(std_id=student24 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check24.check= state24
                admin_check24.save()
                
            if s_id25!=False:                
                student25 = Student.objects.get(std_id=s_id25)         
                admin_check25=Grade.objects.get(std_id=student25 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check25.check= state25
                admin_check25.save()
                
            if s_id26!=False:                
                student26 = Student.objects.get(std_id=s_id26)         
                admin_check26=Grade.objects.get(std_id=student26 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check26.check= state26
                admin_check26.save()
                            
            if s_id27!=False:                
                student27 = Student.objects.get(std_id=s_id27)         
                admin_check27=Grade.objects.get(std_id=student27 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check27.check= state27
                admin_check27.save()
                
            if s_id28!=False:                
                student28 = Student.objects.get(std_id=s_id28)         
                admin_check28=Grade.objects.get(std_id=student28 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check28.check= state28
                admin_check28.save()
                
            if s_id29!=False:                
                student29 = Student.objects.get(std_id=s_id29)         
                admin_check29=Grade.objects.get(std_id=student29 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check29.check= state29
                admin_check29.save()
                
            if s_id30!=False:                
                student30 = Student.objects.get(std_id=s_id30)         
                admin_check30=Grade.objects.get(std_id=student30 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check30.check= state30
                admin_check30.save()
                
            if s_id31!=False:                
                student31 = Student.objects.get(std_id=s_id31)           
                admin_check31=Grade.objects.get(std_id=student31 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check31.check= state31
                admin_check31.save()
                
            if s_id32!=False:                
                student32 = Student.objects.get(std_id=s_id32)         
                admin_check32=Grade.objects.get(std_id=student32 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check32.check= state32
                admin_check32.save()            
                
            if s_id33!=False:                
                student33 = Student.objects.get(std_id=s_id33)         
                admin_check33=Grade.objects.get(std_id=student33 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check33.check= state33
                admin_check33.save()
                
            if s_id34!=False:                
                student34 = Student.objects.get(std_id=s_id34)         
                admin_check34=Grade.objects.get(std_id=student34 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check34.check= state34
                admin_check34.save()
                
            if s_id35!=False:                
                student35 = Student.objects.get(std_id=s_id35)         
                admin_check35=Grade.objects.get(std_id=student35 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check35.check= state35
                admin_check35.save()
                
            if s_id36!=False:                
                student36 = Student.objects.get(std_id=s_id36)         
                admin_check36=Grade.objects.get(std_id=student36 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check36.check= state36
                admin_check36.save()
                            
            if s_id37!=False:                
                student37 = Student.objects.get(std_id=s_id37)         
                admin_check37=Grade.objects.get(std_id=student37 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check37.check= state37
                admin_check37.save()
                
            if s_id38!=False:                
                student38 = Student.objects.get(std_id=s_id38)         
                admin_check38=Grade.objects.get(std_id=student38 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check38.check= state38
                admin_check38.save()
                
            if s_id39!=False:                
                student39 = Student.objects.get(std_id=s_id39)         
                admin_check39=Grade.objects.get(std_id=student39 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check39.check= state39
                admin_check39.save()
                
            if s_id40!=False:                
                student40 = Student.objects.get(std_id=s_id40)         
                admin_check40=Grade.objects.get(std_id=student40 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check40.check= state40
                admin_check40.save()
                
      
        elif(   (month=="01" and (day>=11 or day <= 31))  or  (month=="02" and day <=2)           ):
            t="2"
            course = Course.objects.get(Course_ID=int(c_id))
            section = Section.objects.get(Course_ID=course,Section=int(sec) )
            
            if s_id1!=False:                
                student1 = Student.objects.get(std_id=s_id1)           
                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check1.check= state1
                admin_check1.save()
                
            if s_id2!=False:                
                student2 = Student.objects.get(std_id=s_id2)         
                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check2.check= state2
                admin_check2.save()            
                
            if s_id3!=False:                
                student3 = Student.objects.get(std_id=s_id3)         
                admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check3.check= state3
                admin_check3.save()
                
            if s_id4!=False:                
                student4 = Student.objects.get(std_id=s_id4)         
                admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check4.check= state4
                admin_check4.save()
                
            if s_id5!=False:                
                student5 = Student.objects.get(std_id=s_id5)         
                admin_check5=Grade.objects.get(std_id=student5 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check5.check= state5
                admin_check5.save()
                
            if s_id6!=False:                
                student6 = Student.objects.get(std_id=s_id6)         
                admin_check6=Grade.objects.get(std_id=student6 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check6.check= state6
                admin_check6.save()
                            
            if s_id7!=False:                
                student7 = Student.objects.get(std_id=s_id7)         
                admin_check7=Grade.objects.get(std_id=student7 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check7.check= state7
                admin_check7.save()
                
            if s_id8!=False:                
                student8 = Student.objects.get(std_id=s_id8)         
                admin_check8=Grade.objects.get(std_id=student8 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check8.check= state8
                admin_check8.save()
                
            if s_id9!=False:                
                student9 = Student.objects.get(std_id=s_id9)         
                admin_check9=Grade.objects.get(std_id=student9 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check9.check= state9
                admin_check9.save()
                
            if s_id10!=False:                
                student10 = Student.objects.get(std_id=s_id10)         
                admin_check10=Grade.objects.get(std_id=student10 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check10.check= state10
                admin_check10.save()

            if s_id11!=False:                
                student11 = Student.objects.get(std_id=s_id11)           
                admin_check11=Grade.objects.get(std_id=student11 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check11.check= state11
                admin_check11.save()
                
            if s_id12!=False:                
                student12 = Student.objects.get(std_id=s_id12)         
                admin_check12=Grade.objects.get(std_id=student12 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check12.check= state12
                admin_check12.save()            
                
            if s_id13!=False:                
                student13 = Student.objects.get(std_id=s_id13)         
                admin_check13=Grade.objects.get(std_id=student13 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check13.check= state13
                admin_check13.save()
                
            if s_id14!=False:                
                student14 = Student.objects.get(std_id=s_id14)         
                admin_check14=Grade.objects.get(std_id=student14 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check14.check= state14
                admin_check14.save()
                
            if s_id15!=False:                
                student15 = Student.objects.get(std_id=s_id15)         
                admin_check15=Grade.objects.get(std_id=student15 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check15.check= state15
                admin_check15.save()
                
            if s_id16!=False:                
                student16 = Student.objects.get(std_id=s_id16)         
                admin_check16=Grade.objects.get(std_id=student16 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check16.check= state16
                admin_check16.save()
                            
            if s_id17!=False:                
                student17 = Student.objects.get(std_id=s_id17)         
                admin_check17=Grade.objects.get(std_id=student17 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check17.check= state17
                admin_check17.save()
                
            if s_id18!=False:                
                student18 = Student.objects.get(std_id=s_id18)         
                admin_check18=Grade.objects.get(std_id=student18 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check18.check= state18
                admin_check18.save()
                
            if s_id19!=False:                
                student19 = Student.objects.get(std_id=s_id19)         
                admin_check19=Grade.objects.get(std_id=student19 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check19.check= state19
                admin_check19.save()
                
            if s_id20!=False:                
                student20 = Student.objects.get(std_id=s_id20)         
                admin_check20=Grade.objects.get(std_id=student20 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check20.check= state20
                admin_check20.save()              
                
            if s_id21!=False:                
                student21 = Student.objects.get(std_id=s_id21)           
                admin_check21=Grade.objects.get(std_id=student21 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check21.check= state21
                admin_check21.save()
                
            if s_id22!=False:                
                student22 = Student.objects.get(std_id=s_id22)         
                admin_check22=Grade.objects.get(std_id=student22 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check22.check= state22
                admin_check22.save()            
                
            if s_id23!=False:                
                student23 = Student.objects.get(std_id=s_id23)         
                admin_check23=Grade.objects.get(std_id=student23 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check23.check= state23
                admin_check23.save()
                
            if s_id24!=False:                
                student24 = Student.objects.get(std_id=s_id24)         
                admin_check24=Grade.objects.get(std_id=student24 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check24.check= state24
                admin_check24.save()
                
            if s_id25!=False:                
                student25 = Student.objects.get(std_id=s_id25)         
                admin_check25=Grade.objects.get(std_id=student25 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check25.check= state25
                admin_check25.save()
                
            if s_id26!=False:                
                student26 = Student.objects.get(std_id=s_id26)         
                admin_check26=Grade.objects.get(std_id=student26 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check26.check= state26
                admin_check26.save()
                            
            if s_id27!=False:                
                student27 = Student.objects.get(std_id=s_id27)         
                admin_check27=Grade.objects.get(std_id=student27 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check27.check= state27
                admin_check27.save()
                
            if s_id28!=False:                
                student28 = Student.objects.get(std_id=s_id28)         
                admin_check28=Grade.objects.get(std_id=student28 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check28.check= state28
                admin_check28.save()
                
            if s_id29!=False:                
                student29 = Student.objects.get(std_id=s_id29)         
                admin_check29=Grade.objects.get(std_id=student29 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check29.check= state29
                admin_check29.save()
                
            if s_id30!=False:                
                student30 = Student.objects.get(std_id=s_id30)         
                admin_check30=Grade.objects.get(std_id=student30 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check30.check= state30
                admin_check30.save()
                
            if s_id31!=False:                
                student31 = Student.objects.get(std_id=s_id31)           
                admin_check31=Grade.objects.get(std_id=student31 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check31.check= state31
                admin_check31.save()
                
            if s_id32!=False:                
                student32 = Student.objects.get(std_id=s_id32)         
                admin_check32=Grade.objects.get(std_id=student32 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check32.check= state32
                admin_check32.save()            
                
            if s_id33!=False:                
                student33 = Student.objects.get(std_id=s_id33)         
                admin_check33=Grade.objects.get(std_id=student33 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check33.check= state33
                admin_check33.save()
                
            if s_id34!=False:                
                student34 = Student.objects.get(std_id=s_id34)         
                admin_check34=Grade.objects.get(std_id=student34 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check34.check= state34
                admin_check34.save()
                
            if s_id35!=False:                
                student35 = Student.objects.get(std_id=s_id35)         
                admin_check35=Grade.objects.get(std_id=student35 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check35.check= state35
                admin_check35.save()
                
            if s_id36!=False:                
                student36 = Student.objects.get(std_id=s_id36)         
                admin_check36=Grade.objects.get(std_id=student36 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check36.check= state36
                admin_check36.save()
                            
            if s_id37!=False:                
                student37 = Student.objects.get(std_id=s_id37)         
                admin_check37=Grade.objects.get(std_id=student37 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check37.check= state37
                admin_check37.save()
                
            if s_id38!=False:                
                student38 = Student.objects.get(std_id=s_id38)         
                admin_check38=Grade.objects.get(std_id=student38 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check38.check= state38
                admin_check38.save()
                
            if s_id39!=False:                
                student39 = Student.objects.get(std_id=s_id39)         
                admin_check39=Grade.objects.get(std_id=student39 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check39.check= state39
                admin_check39.save()
                
            if s_id40!=False:                
                student40 = Student.objects.get(std_id=s_id40)         
                admin_check40=Grade.objects.get(std_id=student40 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check40.check= state40
                admin_check40.save()
               
        else:
            context['error_date']= "error_date"
 
    return render(
        request,
        template,
        context
    )


def Update_check_drop(request):
    template = 'group2/drop_admin.html'    # get template
    context = {}
    if request.method == 'POST':

        c_id=request.POST["c_id"]
        sec=request.POST["sec"]
        
        s_id1=request.POST.get("s_id1", False);
        state1=request.POST.get("state1", False);

        s_id2=request.POST.get("s_id2", False);
        state2=request.POST.get("state2", False);
        
        s_id3=request.POST.get("s_id3", False);
        state3=request.POST.get("state3", False);
    
        s_id4=request.POST.get("s_id4", False);
        state4=request.POST.get("state4", False);
        
        s_id5=request.POST.get("s_id5", False);
        state5=request.POST.get("state5", False);
        
        s_id6=request.POST.get("s_id6", False);
        state6=request.POST.get("state6", False);
        
        s_id7=request.POST.get("s_id7", False);
        state7=request.POST.get("state7", False);
        
        s_id8=request.POST.get("s_id8", False);
        state8=request.POST.get("state8", False);
    
        s_id9=request.POST.get("s_id9", False);
        state9=request.POST.get("state9", False);
        
        s_id10=request.POST.get("s_id10", False);
        state10=request.POST.get("state10", False);

        s_id11=request.POST.get("s_id11", False);
        state11=request.POST.get("state11", False);

        s_id12=request.POST.get("s_id12", False);
        state12=request.POST.get("state12", False);
        
        s_id13=request.POST.get("s_id13", False);
        state13=request.POST.get("state13", False);
    
        s_id14=request.POST.get("s_id14", False);
        state14=request.POST.get("state14", False);
        
        s_id15=request.POST.get("s_id15", False);
        state15=request.POST.get("state15", False);
        
        s_id16=request.POST.get("s_id16", False);
        state16=request.POST.get("state16", False);
        
        s_id17=request.POST.get("s_id17", False);
        state17=request.POST.get("state17", False);
        
        s_id18=request.POST.get("s_id18", False);
        state18=request.POST.get("state18", False);
    
        s_id19=request.POST.get("s_id19", False);
        state19=request.POST.get("state19", False);
        
        s_id20=request.POST.get("s_id20", False);
        state20=request.POST.get("state20", False);

        s_id21=request.POST.get("s_id21", False);
        state21=request.POST.get("state21", False);

        s_id22=request.POST.get("s_id22", False);
        state22=request.POST.get("state22", False);
        
        s_id23=request.POST.get("s_id23", False);
        state23=request.POST.get("state23", False);
    
        s_id24=request.POST.get("s_id24", False);
        state24=request.POST.get("state24", False);
        
        s_id25=request.POST.get("s_id25", False);
        state25=request.POST.get("state25", False);
        
        s_id26=request.POST.get("s_id26", False);
        state26=request.POST.get("state26", False);
        
        s_id27=request.POST.get("s_id27", False);
        state27=request.POST.get("state27", False);
        
        s_id28=request.POST.get("s_id28", False);
        state28=request.POST.get("state28", False);
    
        s_id29=request.POST.get("s_id29", False);
        state29=request.POST.get("state29", False);
        
        s_id30=request.POST.get("s_id30", False);
        state30=request.POST.get("state30", False);
        
        s_id31=request.POST.get("s_id31", False);
        state31=request.POST.get("state31", False);

        s_id32=request.POST.get("s_id32", False);
        state32=request.POST.get("state32", False);
        
        s_id33=request.POST.get("s_id33", False);
        state33=request.POST.get("state33", False);
    
        s_id34=request.POST.get("s_id34", False);
        state34=request.POST.get("state34", False);
        
        s_id35=request.POST.get("s_id35", False);
        state35=request.POST.get("state35", False);
        
        s_id36=request.POST.get("s_id36", False);
        state36=request.POST.get("state36", False);
        
        s_id37=request.POST.get("s_id37", False);
        state37=request.POST.get("state37", False);
        
        s_id38=request.POST.get("s_id38", False);
        state38=request.POST.get("state38", False);
    
        s_id39=request.POST.get("s_id39", False);
        state39=request.POST.get("state39", False);
        
        s_id40=request.POST.get("s_id40", False);
        state40=request.POST.get("state40", False);

      
        date=time.strftime("%x")
        month,day,year = date.split("/")

        day=int(day)
        year=int(year)
        year=year+2543
    

        if (    ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or  ((month=="09" or month=="10")and( day >= 1 or day <= 31)) or  ((month=="11" )and( day >= 1 or day <= 3))   ):
            t="1"
             
            course = Course.objects.get(Course_ID=int(c_id))
            section = Section.objects.get(Course_ID=course,Section=int(sec) )
            
            if s_id1!=False:                
                student1 = Student.objects.get(std_id=s_id1)           
                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check1.check= state1
                admin_check1.save()
                
            if s_id2!=False:                
                student2 = Student.objects.get(std_id=s_id2)         
                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check2.check= state2
                admin_check2.save()            
                
            if s_id3!=False:                
                student3 = Student.objects.get(std_id=s_id3)         
                admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check3.check= state3
                admin_check3.save()
                
            if s_id4!=False:                
                student4 = Student.objects.get(std_id=s_id4)         
                admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check4.check= state4
                admin_check4.save()
                
            if s_id5!=False:                
                student5 = Student.objects.get(std_id=s_id5)         
                admin_check5=Grade.objects.get(std_id=student5 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check5.check= state5
                admin_check5.save()
                
            if s_id6!=False:                
                student6 = Student.objects.get(std_id=s_id6)         
                admin_check6=Grade.objects.get(std_id=student6 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check6.check= state6
                admin_check6.save()
                            
            if s_id7!=False:                
                student7 = Student.objects.get(std_id=s_id7)         
                admin_check7=Grade.objects.get(std_id=student7 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check7.check= state7
                admin_check7.save()
                
            if s_id8!=False:                
                student8 = Student.objects.get(std_id=s_id8)         
                admin_check8=Grade.objects.get(std_id=student8 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check8.check= state8
                admin_check8.save()
                
            if s_id9!=False:                
                student9 = Student.objects.get(std_id=s_id9)         
                admin_check9=Grade.objects.get(std_id=student9 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check9.check= state9
                admin_check9.save()
                
            if s_id10!=False:                
                student10 = Student.objects.get(std_id=s_id10)         
                admin_check10=Grade.objects.get(std_id=student10 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check10.check= state10
                admin_check10.save()

            if s_id11!=False:                
                student11 = Student.objects.get(std_id=s_id11)           
                admin_check11=Grade.objects.get(std_id=student11 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check11.check= state11
                admin_check11.save()
                
            if s_id12!=False:                
                student12 = Student.objects.get(std_id=s_id12)         
                admin_check12=Grade.objects.get(std_id=student12 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check12.check= state12
                admin_check12.save()            
                
            if s_id13!=False:                
                student13 = Student.objects.get(std_id=s_id13)         
                admin_check13=Grade.objects.get(std_id=student13 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check13.check= state13
                admin_check13.save()
                
            if s_id14!=False:                
                student14 = Student.objects.get(std_id=s_id14)         
                admin_check14=Grade.objects.get(std_id=student14 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check14.check= state14
                admin_check14.save()
                
            if s_id15!=False:                
                student15 = Student.objects.get(std_id=s_id15)         
                admin_check15=Grade.objects.get(std_id=student15 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check15.check= state15
                admin_check15.save()
                
            if s_id16!=False:                
                student16 = Student.objects.get(std_id=s_id16)         
                admin_check16=Grade.objects.get(std_id=student16 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check16.check= state16
                admin_check16.save()
                            
            if s_id17!=False:                
                student17 = Student.objects.get(std_id=s_id17)         
                admin_check17=Grade.objects.get(std_id=student17 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check17.check= state17
                admin_check17.save()
                
            if s_id18!=False:                
                student18 = Student.objects.get(std_id=s_id18)         
                admin_check18=Grade.objects.get(std_id=student18 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check18.check= state18
                admin_check18.save()
                
            if s_id19!=False:                
                student19 = Student.objects.get(std_id=s_id19)         
                admin_check19=Grade.objects.get(std_id=student19 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check19.check= state19
                admin_check19.save()
                
            if s_id20!=False:                
                student20 = Student.objects.get(std_id=s_id20)         
                admin_check20=Grade.objects.get(std_id=student20 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check20.check= state20
                admin_check20.save()              
                
            if s_id21!=False:                
                student21 = Student.objects.get(std_id=s_id21)           
                admin_check21=Grade.objects.get(std_id=student21 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check21.check= state21
                admin_check21.save()
                
            if s_id22!=False:                
                student22 = Student.objects.get(std_id=s_id22)         
                admin_check22=Grade.objects.get(std_id=student22 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check22.check= state22
                admin_check22.save()            
                
            if s_id23!=False:                
                student23 = Student.objects.get(std_id=s_id23)         
                admin_check23=Grade.objects.get(std_id=student23 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check23.check= state23
                admin_check23.save()
                
            if s_id24!=False:                
                student24 = Student.objects.get(std_id=s_id24)         
                admin_check24=Grade.objects.get(std_id=student24 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check24.check= state24
                admin_check24.save()
                
            if s_id25!=False:                
                student25 = Student.objects.get(std_id=s_id25)         
                admin_check25=Grade.objects.get(std_id=student25 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check25.check= state25
                admin_check25.save()
                
            if s_id26!=False:                
                student26 = Student.objects.get(std_id=s_id26)         
                admin_check26=Grade.objects.get(std_id=student26 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check26.check= state26
                admin_check26.save()
                            
            if s_id27!=False:                
                student27 = Student.objects.get(std_id=s_id27)         
                admin_check27=Grade.objects.get(std_id=student27 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check27.check= state27
                admin_check27.save()
                
            if s_id28!=False:                
                student28 = Student.objects.get(std_id=s_id28)         
                admin_check28=Grade.objects.get(std_id=student28 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check28.check= state28
                admin_check28.save()
                
            if s_id29!=False:                
                student29 = Student.objects.get(std_id=s_id29)         
                admin_check29=Grade.objects.get(std_id=student29 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check29.check= state29
                admin_check29.save()
                
            if s_id30!=False:                
                student30 = Student.objects.get(std_id=s_id30)         
                admin_check30=Grade.objects.get(std_id=student30 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check30.check= state30
                admin_check30.save()
                
            if s_id31!=False:                
                student31 = Student.objects.get(std_id=s_id31)           
                admin_check31=Grade.objects.get(std_id=student31 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check31.check= state31
                admin_check31.save()
                
            if s_id32!=False:                
                student32 = Student.objects.get(std_id=s_id32)         
                admin_check32=Grade.objects.get(std_id=student32 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check32.check= state32
                admin_check32.save()            
                
            if s_id33!=False:                
                student33 = Student.objects.get(std_id=s_id33)         
                admin_check33=Grade.objects.get(std_id=student33 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check33.check= state33
                admin_check33.save()
                
            if s_id34!=False:                
                student34 = Student.objects.get(std_id=s_id34)         
                admin_check34=Grade.objects.get(std_id=student34 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check34.check= state34
                admin_check34.save()
                
            if s_id35!=False:                
                student35 = Student.objects.get(std_id=s_id35)         
                admin_check35=Grade.objects.get(std_id=student35 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check35.check= state35
                admin_check35.save()
                
            if s_id36!=False:                
                student36 = Student.objects.get(std_id=s_id36)         
                admin_check36=Grade.objects.get(std_id=student36 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check36.check= state36
                admin_check36.save()
                            
            if s_id37!=False:                
                student37 = Student.objects.get(std_id=s_id37)         
                admin_check37=Grade.objects.get(std_id=student37 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check37.check= state37
                admin_check37.save()
                
            if s_id38!=False:                
                student38 = Student.objects.get(std_id=s_id38)         
                admin_check38=Grade.objects.get(std_id=student38 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check38.check= state38
                admin_check38.save()
                
            if s_id39!=False:                
                student39 = Student.objects.get(std_id=s_id39)         
                admin_check39=Grade.objects.get(std_id=student39 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check39.check= state39
                admin_check39.save()
                
            if s_id40!=False:                
                student40 = Student.objects.get(std_id=s_id40)         
                admin_check40=Grade.objects.get(std_id=student40 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check40.check= state40
                admin_check40.save()
                
      
        elif(   (month=="01" and (day>=11 or day <= 31))    or  ((month=="02" or month=="03")and( day >= 1 or day <= 31))  or  ((month=="04" )and( day >= 1 or day <= 5))           ):
            t="2"
            course = Course.objects.get(Course_ID=int(c_id))
            section = Section.objects.get(Course_ID=course,Section=int(sec) )
            
            if s_id1!=False:                
                student1 = Student.objects.get(std_id=s_id1)           
                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check1.check= state1
                admin_check1.save()
                
            if s_id2!=False:                
                student2 = Student.objects.get(std_id=s_id2)         
                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check2.check= state2
                admin_check2.save()            
                
            if s_id3!=False:                
                student3 = Student.objects.get(std_id=s_id3)         
                admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check3.check= state3
                admin_check3.save()
                
            if s_id4!=False:                
                student4 = Student.objects.get(std_id=s_id4)         
                admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check4.check= state4
                admin_check4.save()
                
            if s_id5!=False:                
                student5 = Student.objects.get(std_id=s_id5)         
                admin_check5=Grade.objects.get(std_id=student5 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check5.check= state5
                admin_check5.save()
                
            if s_id6!=False:                
                student6 = Student.objects.get(std_id=s_id6)         
                admin_check6=Grade.objects.get(std_id=student6 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check6.check= state6
                admin_check6.save()
                            
            if s_id7!=False:                
                student7 = Student.objects.get(std_id=s_id7)         
                admin_check7=Grade.objects.get(std_id=student7 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check7.check= state7
                admin_check7.save()
                
            if s_id8!=False:                
                student8 = Student.objects.get(std_id=s_id8)         
                admin_check8=Grade.objects.get(std_id=student8 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check8.check= state8
                admin_check8.save()
                
            if s_id9!=False:                
                student9 = Student.objects.get(std_id=s_id9)         
                admin_check9=Grade.objects.get(std_id=student9 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check9.check= state9
                admin_check9.save()
                
            if s_id10!=False:                
                student10 = Student.objects.get(std_id=s_id10)         
                admin_check10=Grade.objects.get(std_id=student10 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check10.check= state10
                admin_check10.save()

            if s_id11!=False:                
                student11 = Student.objects.get(std_id=s_id11)           
                admin_check11=Grade.objects.get(std_id=student11 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check11.check= state11
                admin_check11.save()
                
            if s_id12!=False:                
                student12 = Student.objects.get(std_id=s_id12)         
                admin_check12=Grade.objects.get(std_id=student12 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check12.check= state12
                admin_check12.save()            
                
            if s_id13!=False:                
                student13 = Student.objects.get(std_id=s_id13)         
                admin_check13=Grade.objects.get(std_id=student13 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check13.check= state13
                admin_check13.save()
                
            if s_id14!=False:                
                student14 = Student.objects.get(std_id=s_id14)         
                admin_check14=Grade.objects.get(std_id=student14 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check14.check= state14
                admin_check14.save()
                
            if s_id15!=False:                
                student15 = Student.objects.get(std_id=s_id15)         
                admin_check15=Grade.objects.get(std_id=student15 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check15.check= state15
                admin_check15.save()
                
            if s_id16!=False:                
                student16 = Student.objects.get(std_id=s_id16)         
                admin_check16=Grade.objects.get(std_id=student16 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check16.check= state16
                admin_check16.save()
                            
            if s_id17!=False:                
                student17 = Student.objects.get(std_id=s_id17)         
                admin_check17=Grade.objects.get(std_id=student17 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check17.check= state17
                admin_check17.save()
                
            if s_id18!=False:                
                student18 = Student.objects.get(std_id=s_id18)         
                admin_check18=Grade.objects.get(std_id=student18 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check18.check= state18
                admin_check18.save()
                
            if s_id19!=False:                
                student19 = Student.objects.get(std_id=s_id19)         
                admin_check19=Grade.objects.get(std_id=student19 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check19.check= state19
                admin_check19.save()
                
            if s_id20!=False:                
                student20 = Student.objects.get(std_id=s_id20)         
                admin_check20=Grade.objects.get(std_id=student20 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check20.check= state20
                admin_check20.save()              
                
            if s_id21!=False:                
                student21 = Student.objects.get(std_id=s_id21)           
                admin_check21=Grade.objects.get(std_id=student21 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check21.check= state21
                admin_check21.save()
                
            if s_id22!=False:                
                student22 = Student.objects.get(std_id=s_id22)         
                admin_check22=Grade.objects.get(std_id=student22 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check22.check= state22
                admin_check22.save()            
                
            if s_id23!=False:                
                student23 = Student.objects.get(std_id=s_id23)         
                admin_check23=Grade.objects.get(std_id=student23 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check23.check= state23
                admin_check23.save()
                
            if s_id24!=False:                
                student24 = Student.objects.get(std_id=s_id24)         
                admin_check24=Grade.objects.get(std_id=student24 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check24.check= state24
                admin_check24.save()
                
            if s_id25!=False:                
                student25 = Student.objects.get(std_id=s_id25)         
                admin_check25=Grade.objects.get(std_id=student25 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check25.check= state25
                admin_check25.save()
                
            if s_id26!=False:                
                student26 = Student.objects.get(std_id=s_id26)         
                admin_check26=Grade.objects.get(std_id=student26 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check26.check= state26
                admin_check26.save()
                            
            if s_id27!=False:                
                student27 = Student.objects.get(std_id=s_id27)         
                admin_check27=Grade.objects.get(std_id=student27 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check27.check= state27
                admin_check27.save()
                
            if s_id28!=False:                
                student28 = Student.objects.get(std_id=s_id28)         
                admin_check28=Grade.objects.get(std_id=student28 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check28.check= state28
                admin_check28.save()
                
            if s_id29!=False:                
                student29 = Student.objects.get(std_id=s_id29)         
                admin_check29=Grade.objects.get(std_id=student29 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check29.check= state29
                admin_check29.save()
                
            if s_id30!=False:                
                student30 = Student.objects.get(std_id=s_id30)         
                admin_check30=Grade.objects.get(std_id=student30 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check30.check= state30
                admin_check30.save()
                
            if s_id31!=False:                
                student31 = Student.objects.get(std_id=s_id31)           
                admin_check31=Grade.objects.get(std_id=student31 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check31.check= state31
                admin_check31.save()
                
            if s_id32!=False:                
                student32 = Student.objects.get(std_id=s_id32)         
                admin_check32=Grade.objects.get(std_id=student32 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check32.check= state32
                admin_check32.save()            
                
            if s_id33!=False:                
                student33 = Student.objects.get(std_id=s_id33)         
                admin_check33=Grade.objects.get(std_id=student33 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check33.check= state33
                admin_check33.save()
                
            if s_id34!=False:                
                student34 = Student.objects.get(std_id=s_id34)         
                admin_check34=Grade.objects.get(std_id=student34 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check34.check= state34
                admin_check34.save()
                
            if s_id35!=False:                
                student35 = Student.objects.get(std_id=s_id35)         
                admin_check35=Grade.objects.get(std_id=student35 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check35.check= state35
                admin_check35.save()
                
            if s_id36!=False:                
                student36 = Student.objects.get(std_id=s_id36)         
                admin_check36=Grade.objects.get(std_id=student36 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check36.check= state36
                admin_check36.save()
                            
            if s_id37!=False:                
                student37 = Student.objects.get(std_id=s_id37)         
                admin_check37=Grade.objects.get(std_id=student37 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check37.check= state37
                admin_check37.save()
                
            if s_id38!=False:                
                student38 = Student.objects.get(std_id=s_id38)         
                admin_check38=Grade.objects.get(std_id=student38 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check38.check= state38
                admin_check38.save()
                
            if s_id39!=False:                
                student39 = Student.objects.get(std_id=s_id39)         
                admin_check39=Grade.objects.get(std_id=student39 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check39.check= state39
                admin_check39.save()
                
            if s_id40!=False:                
                student40 = Student.objects.get(std_id=s_id40)         
                admin_check40=Grade.objects.get(std_id=student40 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='')
                admin_check40.check= state40
                admin_check40.save()
               
        else:
            context['error_date']= "error_date"

    return render(
        request,
        template,
        context
    )



def Find_course_admin(request):
    template = 'group2/registeration.html'   # get template
    context = {}

    if request.method == 'POST':
        c1=request.POST["c1"]
        s1=request.POST["s1"]
 
        if c1=="":

                context['error_find_course']= "error_find_course"
        else:

                 if Section.objects.filter(Section=int(s1),Course_ID=int(c1) ):
                    number_table=Section.objects.filter(Section=int(s1),Course_ID=int(c1) )
                    context={'number_table': number_table}
                 else:
                     context['error_find_data']= "error_data"
      

        
    else:
        context = {}

    return render(
        request,
        template,
        context
    )


def Edit_course_admin(request):
    template = 'group2/registeration.html'    # get template
    context = {}
    
    
    if request.method == 'POST':
        c_id=request.POST["c_id"]
        
        sec_original=request.POST["sec_original"]
        sec_new=request.POST["sec_new"]
        day_new=request.POST["day_new"]
        time_new=request.POST["time_new"]       
        place_new=request.POST["place_new"]          
        

        if c_id=="":
           context['error_edit']= "error_edit" 
        

        else:
           if sec_new==" ":
            
              course = Course.objects.get(Course_ID=int(c_id))
              if Section.objects.get(Section=int(sec_original) ,Course_ID=course):  
                    secc = Section.objects.get(Section=int(sec_original) ,Course_ID=course)


                    secc.classroom  = place_new
                    secc.st_endTime  = time_new
                    secc.date  = day_new
                    secc.save()
                    table_show=Section.objects.filter(Course_ID=course,Section=int(sec_original))
                    context = {'table_show': table_show}
              else:
                   context['error_edit']= "error_edit" 
            
           else:
               course = Course.objects.get(Course_ID=int(c_id))
               if Section.objects.get(Section=int(sec_original) ,Course_ID=course):
                    secc = Section.objects.get(Section=int(sec_original) ,Course_ID=course)
                    secc.Section = int(sec_new)
                    secc.classroom  = place_new
                    secc.st_endTime  = time_new
                    secc.date  = day_new
                    secc.save()
                    table_show=Section.objects.filter(Course_ID=course,Section=int(sec_new))
                    context = {'table_show': table_show}
               else:
                   context['error_edit']= "error_edit" 
    else:
        context = {}
    return render(
        request,
        template,
        context
    )


def Add_course_admin(request):
    template = 'group2/registeration.html'    # get template
    context = {}

    
    if request.method == 'POST':
        c_id=request.POST["c_id"]
        c_name=request.POST["c_name"]
        credit=request.POST["credit"]
        sec=request.POST["sec"]
        room=request.POST["room"]
        day=request.POST["day"]
        time=request.POST["time"]
        n_teacher=request.POST["n_teacher"]
        l_teacher=request.POST["l_teacher"]
        teacher_id=request.POST["teacher_id"]
               

        if c_id=="":
           if sec==" ":
               context['error_course']= "error_course"
               context['error_sec']= "error_sec"
           else:
               context['error_course']= "error_course"
        else:
            if sec==" ":
               context['error_sec']= "error_sec"
            else:
                if Course.objects.filter(Course_ID=int(c_id) ):
                    course = Course.objects.get(Course_ID=int(c_id) )
                   
                    if Section.objects.filter(Course_ID=course,Section=int(sec) ):
                         context['duplicate_add']= "duplicate_add"
                    else:    
                        add=Section(Section=int(sec),Course_ID=course,classroom=room,st_endTime=time,date=day,T_name=n_teacher,T_lastname=l_teacher,shortname= teacher_id)
                        add.save()
                        table_show=Section.objects.filter(Course_ID=course,Section=int(sec) )
                        context = {'table_show': table_show}
                else:

                        c=Course.objects.create(Course_ID=int(c_id),Credit=int(credit),Course_Name=c_name)
                        course = Course.objects.get(Course_ID=int(c_id) )
                        add=Section(Section=int(sec),Course_ID=course,classroom=room,st_endTime=time,date=day,T_name=n_teacher,T_lastname=l_teacher,shortname= teacher_id)
                        add.save()

                        table_show=Section.objects.filter(Course_ID=course,Section=int(sec) )
                        context = {'table_show': table_show}

    return render(
        request,
        template,
        context
    )

def drop(request):
    template = 'group2/drop.html'    # get template
    context = {}
    
    #number_table=Base.objects.all()
    if getUserType(request) != '0':
        template = 'group2/drop.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
		#Grade = Grade.objects.get(std_id = studentObj.std_id )
		#Course = Course.objects.get(Course_ID = )
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}
    
    return render(
        request,
        template,
        context
    )    
    
def drop_admin(request):
    template = 'group2/drop_admin.html'    # get template
    context = {}
    

	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
		#Grade = Grade.objects.get(std_id = studentObj.std_id )
		#Course = Course.objects.get(Course_ID = )
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}
    
    return render(
        request,
        template,
        context
    )    
    
    
def Admin_check_register(request):
    template = 'group2/regis_result.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)

    except: # can't get a Student object
        context = {}


    if request.method == 'POST':
        c_id=request.POST["c_id1"]
        sec=request.POST["sec1"]



    course = Course.objects.get(Course_ID=int(c_id))
    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))

    date=time.strftime("%x")
    month,day,year = date.split("/")
    day=int(day)
    year=int(year)
    year=year+2543

    if Grade.objects.filter(std_id=studentObj,Course_ID=course ,Section=secc  ):
        context['duplicate']= "duplicate" 
    else:
        if ( month=="07" or month=="08")and( day >= 10 or day <= 31):
                t="1"
                grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc ,check='เรียน')
                grade_put.save()
                context['success_re']= "success_re" 

            

    
        elif(   (month=="01" and (day>=11 or day <= 31))  or  (month=="02" and day ==1)           ):
                t="2"
                grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc ,check='เรียน')
                grade_put.save()
                context['success_re']= "success_re" 
        

        else:
            context['error_date']= "error_date"

    return render(
        request,
        template,
        context
    )



def Admin_check_drop(request):
    template = 'group2/regis_result.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
    except: # can't get a Student object
        context = {}


    if request.method == 'POST':
        
        c_id1=request.POST.get("c_id1", False);
        sec1=request.POST.get("sec1", False);
        
        c_id2=request.POST.get("c_id2", False);
        sec2=request.POST.get("sec2", False);
        
        c_id3=request.POST.get("c_id3", False);
        sec3=request.POST.get("sec3", False);
        
        c_id4=request.POST.get("c_id4", False);
        sec4=request.POST.get("sec4", False);
        
        
        date=time.strftime("%x")
        month,day,year = date.split("/")
        day=int(day)
        year=int(year)
        year=year+2543
        

        if (    ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or  ((month=="09" or month=="10")and( day >= 1 or day <= 31)) or  ((month=="11" )and( day >= 1 or day <= 3))   ):
            t="1"
            if c_id1!=False:
                course1 = Course.objects.get(Course_ID=int(c_id1))
                section1 = Section.objects.get(Course_ID=int(c_id1),Section=int(sec1)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
                    
            if c_id2!=False:
                course2 = Course.objects.get(Course_ID=int(c_id2))
                section2 = Section.objects.get(Course_ID=int(c_id2),Section=int(sec2)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check2=Grade.objects.get(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),Grade='')
                    admin_check2.check= "ดรอป"
                    admin_check2.save()
                    context['success']= "success"
                    
            if c_id3!=False:
                course3 = Course.objects.get(Course_ID=int(c_id3))
                section3 = Section.objects.get(Course_ID=int(c_id3),Section=int(sec3)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check3=Grade.objects.get(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),Grade='')
                    admin_check3.check= "ดรอป"
                    admin_check3.save()
                    context['success']= "success"
                    
            if c_id4!=False:
                course4 = Course.objects.get(Course_ID=int(c_id4))
                section4 = Section.objects.get(Course_ID=int(c_id4),Section=int(sec4)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check4=Grade.objects.get(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t),Grade='')
                    admin_check4.check= "ดรอป"
                    admin_check4.save()
                    context['success']= "success"
                    
        elif(   (month=="01" and (day>=11 or day <= 31))    or  ((month=="02" or month=="03")and( day >= 1 or day <= 31))  or  ((month=="04" )and( day >= 1 or day <= 5))           ):
            t="2"
            if c_id1!=False:
                course1 = Course.objects.get(Course_ID=int(c_id1))
                section1 = Section.objects.get(Course_ID=int(c_id1),Section=int(sec1)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
                    
            if c_id2!=False:
                course2 = Course.objects.get(Course_ID=int(c_id2))
                section2 = Section.objects.get(Course_ID=int(c_id2),Section=int(sec2)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check2=Grade.objects.get(std_id=studentObj ,Course_ID=course2,Section=section2,year=year,term=int(t),Grade='')
                    admin_check2.check= "ดรอป"
                    admin_check2.save()
                    context['success']= "success"
                    
            if c_id3!=False:
                course3 = Course.objects.get(Course_ID=int(c_id3))
                section3 = Section.objects.get(Course_ID=int(c_id3),Section=int(sec3)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check3=Grade.objects.get(std_id=studentObj ,Course_ID=course3,Section=section3,year=year,term=int(t),Grade='')
                    admin_check3.check= "ดรอป"
                    admin_check3.save()
                    context['success']= "success"
                    
            if c_id4!=False:
                course4 = Course.objects.get(Course_ID=int(c_id4))
                section4 = Section.objects.get(Course_ID=int(c_id4),Section=int(sec4)  )
                 
                if  Grade.objects.filter(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t),check='ดรอป'):
                    context['duplicate_drop']= "duplicate_drop"
                else:            
                    admin_check4=Grade.objects.get(std_id=studentObj ,Course_ID=course4,Section=section4,year=year,term=int(t),Grade='')
                    admin_check4.check= "ดรอป"
                    admin_check4.save()
                    context['success']= "success"
                    
        else:
                      
            context['error_date']= "error_date"
            
    return render(
        request,
        template,
        context
    )


def Find_Admin_check_register(request):
    template = 'group2/registeration_admin.html'    # get template
    context = {}

    if request.method == 'POST':
        c_id=request.POST["c1"]
        sec=request.POST["s1"]
 
        if c_id=="":

                context['error_course']= "error_course"
        else:

                if Course.objects.filter(Course_ID=int(c_id)):
                    course = Course.objects.get(Course_ID=int(c_id))
                    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))

                    date=time.strftime("%x")
                    month,day,year = date.split("/")

                    day=int(day)
                    year=int(year)
                    year=year+2543

                
                    if ( ((month=="07" or month=="08")and( day >= 10 or day <= 31))  or ((month=="09")and( day==1))        ):
                        t="1"
                        if Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year  ):
                            table_show=Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year)
                            number_std=len(table_show)   
                            
                            if number_std==1 :   
                                context = {'table_show1': table_show[0]}
                            elif number_std==2:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1]}
                            elif number_std==3:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]}
                            elif number_std==4:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3]}
                            elif number_std==5:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4]}
                            elif number_std==6:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]}                               
                            elif number_std==7:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6]}                                  
                            elif number_std==8:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7]}                                  
                            elif number_std==9:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]}                                
                            elif number_std==10:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9]}                                  
                                
                            elif number_std==11:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10]}
                                
                            elif number_std==12:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]}

                            elif number_std==13:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12]}
                                
                            elif number_std==14:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13]}                                 
                           
                            elif number_std==15:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]}
                                
                            elif number_std==16:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15]}                                

                            elif number_std==17:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16]}
                                
                            elif number_std==18:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]}
                                
                            elif number_std==19:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18]}
                                
                            elif number_std==20:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19]} 

                            elif number_std==21:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]}
                                
                            elif number_std==22:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21]}
                                
                            elif number_std==23:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22]}                               
                                
                            elif number_std==24:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]}
                                
                            elif number_std==25:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24]}                                
                                
                            elif number_std==26:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25]}                                
                                
                            elif number_std==27:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]}

                            elif number_std==28:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27]}
                                
                            elif number_std==29:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28]}
                                
                            elif number_std==30:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]}
                                
                            elif number_std==31:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30]}                                 

                            elif number_std==32:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31]}
                                
                            elif number_std==33:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]}
                                
                            elif number_std==34:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33]}
                                
                            elif number_std==35:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34]}
                                
                            elif number_std==36:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]}
                                
                            elif number_std==37:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36]}
                                
                            elif number_std==38:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37]}
                                
                            elif number_std==39:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]}
                                
                            elif number_std==40:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]
                                           ,'table_show40': table_show[39]}                               
                        else:
                              context['error_data']= "error_data" 
            
            
            

                    elif(   (month=="01" and (day>=11 or day <= 31))  or  ((month=="02" )and (day>=1 or day <=2))           ):
                        t="2"
                        if Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year  ):
                            table_show=Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year)
                            number_std=len(table_show)   
                            
                            if number_std==1 :   
                                context = {'table_show1': table_show[0]}
                            elif number_std==2:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1]}
                            elif number_std==3:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]}
                            elif number_std==4:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3]}
                            elif number_std==5:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4]}
                            elif number_std==6:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]}                               
                            elif number_std==7:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6]}                                  
                            elif number_std==8:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7]}                                  
                            elif number_std==9:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]}                                
                            elif number_std==10:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9]}                                  
                                
                            elif number_std==11:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10]}
                                
                            elif number_std==12:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]}

                            elif number_std==13:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12]}
                                
                            elif number_std==14:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13]}                                 
                           
                            elif number_std==15:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]}
                                
                            elif number_std==16:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15]}                                

                            elif number_std==17:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16]}
                                
                            elif number_std==18:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]}
                                
                            elif number_std==19:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18]}
                                
                            elif number_std==20:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19]} 

                            elif number_std==21:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]}
                                
                            elif number_std==22:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21]}
                                
                            elif number_std==23:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22]}                               
                                
                            elif number_std==24:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]}
                                
                            elif number_std==25:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24]}                                
                                
                            elif number_std==26:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25]}                                
                                
                            elif number_std==27:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]}

                            elif number_std==28:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27]}
                                
                            elif number_std==29:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28]}
                                
                            elif number_std==30:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]}
                                
                            elif number_std==31:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30]}                                 

                            elif number_std==32:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31]}
                                
                            elif number_std==33:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]}
                                
                            elif number_std==34:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33]}
                                
                            elif number_std==35:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34]}
                                
                            elif number_std==36:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]}
                                
                            elif number_std==37:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36]}
                                
                            elif number_std==38:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37]}
                                
                            elif number_std==39:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]}
                                
                            elif number_std==40:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]
                                           ,'table_show40': table_show[39]}                               
                        else:
                            
                            context['error_data']= "error_data" 
               
                    else:
                                context['error_date']= "error_date" 
               



            




 
    return render(
        request,
        template,
        context
    )


def Find_Admin_check_drop(request):
    template = 'group2/drop_admin.html'    # get template
    context = {}

    if request.method == 'POST':
        c_id=request.POST["c1"]
        sec=request.POST["s1"]
 
        if c_id=="":

                context['error_find_course']= "error_find_course"
        else:

                if Course.objects.filter(Course_ID=int(c_id)):
                    course = Course.objects.get(Course_ID=int(c_id))
                    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))

                    date=time.strftime("%x")
                    month,day,year = date.split("/")
                    year=int(year)
                    year=year+2543

                
                    if (    ((month=="07" or month=="08")and( day >= 10 or day <= 31)) or  ((month=="09" or month=="10")and( day >= 1 or day <= 31)) or  ((month=="11" )and( day >= 1 or day <= 3))   ):
                        t="1"
                        if Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year,check='ดรอป' or 'อนุมัติดรอป'  ):
                            table_show=Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year,check='ดรอป' or 'อนุมัติดรอป' )
                            number_std=len(table_show)   
                            
                            if number_std==1 :   
                                context = {'table_show1': table_show[0]}
                            elif number_std==2:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1]}
                            elif number_std==3:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]}
                            elif number_std==4:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3]}
                            elif number_std==5:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4]}
                            elif number_std==6:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]}                               
                            elif number_std==7:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6]}                                  
                            elif number_std==8:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7]}                                  
                            elif number_std==9:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]}                                
                            elif number_std==10:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9]}                                  
                                
                            elif number_std==11:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10]}
                                
                            elif number_std==12:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]}

                            elif number_std==13:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12]}
                                
                            elif number_std==14:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13]}                                 
                           
                            elif number_std==15:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]}
                                
                            elif number_std==16:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15]}                                

                            elif number_std==17:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16]}
                                
                            elif number_std==18:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]}
                                
                            elif number_std==19:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18]}
                                
                            elif number_std==20:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19]} 

                            elif number_std==21:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]}
                                
                            elif number_std==22:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21]}
                                
                            elif number_std==23:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22]}                               
                                
                            elif number_std==24:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]}
                                
                            elif number_std==25:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24]}                                
                                
                            elif number_std==26:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25]}                                
                                
                            elif number_std==27:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]}

                            elif number_std==28:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27]}
                                
                            elif number_std==29:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28]}
                                
                            elif number_std==30:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]}
                                
                            elif number_std==31:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30]}                                 

                            elif number_std==32:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31]}
                                
                            elif number_std==33:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]}
                                
                            elif number_std==34:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33]}
                                
                            elif number_std==35:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34]}
                                
                            elif number_std==36:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]}
                                
                            elif number_std==37:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36]}
                                
                            elif number_std==38:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37]}
                                
                            elif number_std==39:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]}
                                
                            elif number_std==40:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]
                                           ,'table_show40': table_show[39]}                               
                        else:
                              context['error_data']= "error_data" 
            
            
            

                    elif(   (month=="01" and (day>=11 or day <= 31))    or  ((month=="02" or month=="03")and( day >= 1 or day <= 31))  or  ((month=="04" )and( day >= 1 or day <= 5))           ):
                        t="2"
                        if Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year,check='ดรอป' or 'อนุมัติดรอป' ):
                            table_show=Grade.objects.filter(Course_ID=course ,Section=secc,term=int(t),year=year,check='ดรอป' or 'อนุมัติดรอป' )
                            number_std=len(table_show)   
                            
                            if number_std==1 :   
                                context = {'table_show1': table_show[0]}
                            elif number_std==2:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1]}
                            elif number_std==3:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]}
                            elif number_std==4:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3]}
                            elif number_std==5:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4]}
                            elif number_std==6:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]}                               
                            elif number_std==7:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6]}                                  
                            elif number_std==8:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7]}                                  
                            elif number_std==9:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]}                                
                            elif number_std==10:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9]}                                  
                                
                            elif number_std==11:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10]}
                                
                            elif number_std==12:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]}

                            elif number_std==13:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12]}
                                
                            elif number_std==14:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13]}                                 
                           
                            elif number_std==15:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]}
                                
                            elif number_std==16:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15]}                                

                            elif number_std==17:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16]}
                                
                            elif number_std==18:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]}
                                
                            elif number_std==19:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18]}
                                
                            elif number_std==20:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19]} 

                            elif number_std==21:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]}
                                
                            elif number_std==22:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21]}
                                
                            elif number_std==23:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22]}                               
                                
                            elif number_std==24:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]}
                                
                            elif number_std==25:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24]}                                
                                
                            elif number_std==26:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25]}                                
                                
                            elif number_std==27:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]}

                            elif number_std==28:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27]}
                                
                            elif number_std==29:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28]}
                                
                            elif number_std==30:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]}
                                
                            elif number_std==31:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30]}                                 

                            elif number_std==32:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31]}
                                
                            elif number_std==33:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]}
                                
                            elif number_std==34:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33]}
                                
                            elif number_std==35:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34]}
                                
                            elif number_std==36:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]}
                                
                            elif number_std==37:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36]}
                                
                            elif number_std==38:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37]}
                                
                            elif number_std==39:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]}
                                
                            elif number_std==40:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]
                                           ,'table_show40': table_show[39]}                               
                        else:
                            
                            context['error_data']= "error_data" 
               
                    else:
                                context['error_date']= "error_date" 

    return render(
        request,
        template,
        context
    )




def Admin_drop(request):
    template = 'group2/drop_admin.html'    # get template
    context = {}


	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}


    return render(
        request,
        template,
        context
    )


def Find_school_record_admin(request):
    template = 'group2/school_record_admin.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)

    except: # can't get a Student object
        context = {}



    if request.method == 'POST':
        c_id=request.POST["c_id"]
        sec=request.POST["sec"]
        term=request.POST["t"]
        year=request.POST["y"]
        

        if (c_id=="" and year=="")or c_id=="" or year=="":

                context['error_find_course']= "error_find_course"
                context['error_find_year']= "error_find_year"


        elif c_id!="" and year!="" :
                if Course.objects.filter(Course_ID=int(c_id)):
                        course = Course.objects.get(Course_ID=int(c_id))
                        secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))
                    
                        if Grade.objects.filter(Course_ID=course ,Section=secc,term=int(term),year=int(year),check='อนุมัติ' ):
                            table_show=Grade.objects.filter(Course_ID=course ,Section=secc,term=int(term),year=int(year),check='อนุมัติ' )
                            number_std=len(table_show)   
                            
                            if number_std==1 :   
                                context = {'table_show1': table_show[0]}
                            elif number_std==2:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1]}
                            elif number_std==3:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]}
                            elif number_std==4:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3]}
                            elif number_std==5:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4]}
                            elif number_std==6:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]}                               
                            elif number_std==7:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6]}                                  
                            elif number_std==8:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7]}                                  
                            elif number_std==9:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]}                                
                            elif number_std==10:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9]}                                  
                                
                            elif number_std==11:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10]}
                                
                            elif number_std==12:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]}

                            elif number_std==13:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12]}
                                
                            elif number_std==14:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13]}                                 
                           
                            elif number_std==15:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]}
                                
                            elif number_std==16:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15]}                                

                            elif number_std==17:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16]}
                                
                            elif number_std==18:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]}
                                
                            elif number_std==19:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18]}
                                
                            elif number_std==20:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19]} 

                            elif number_std==21:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]}
                                
                            elif number_std==22:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21]}
                                
                            elif number_std==23:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22]}                               
                                
                            elif number_std==24:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]}
                                
                            elif number_std==25:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24]}                                
                                
                            elif number_std==26:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25]}                                
                                
                            elif number_std==27:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]}

                            elif number_std==28:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27]}
                                
                            elif number_std==29:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28]}
                                
                            elif number_std==30:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]}
                                
                            elif number_std==31:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30]}                                 

                            elif number_std==32:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31]}
                                
                            elif number_std==33:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]}
                                
                            elif number_std==34:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33]}
                                
                            elif number_std==35:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34]}
                                
                            elif number_std==36:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]}
                                
                            elif number_std==37:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36]}
                                
                            elif number_std==38:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37]}
                                
                            elif number_std==39:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]}
                                
                            elif number_std==40:
                                context = {'table_show1': table_show[0],'table_show2': table_show[1],'table_show3': table_show[2]
                                           ,'table_show4': table_show[3],'table_show5': table_show[4],'table_show6': table_show[5]
                                           ,'table_show7': table_show[6],'table_show8': table_show[7],'table_show9': table_show[8]
                                           ,'table_show10': table_show[9],'table_show11': table_show[10],'table_show12': table_show[11]
                                           ,'table_show13': table_show[12],'table_show14': table_show[13],'table_show15': table_show[14]
                                           ,'table_show16': table_show[15],'table_show17': table_show[16],'table_show18': table_show[17]
                                           ,'table_show19': table_show[18],'table_show20': table_show[19],'table_show21': table_show[20]
                                           ,'table_show22': table_show[21],'table_show23': table_show[22],'table_show24': table_show[23]
                                           ,'table_show25': table_show[24],'table_show26': table_show[25],'table_show27': table_show[26]
                                           ,'table_show28': table_show[27],'table_show29': table_show[28],'table_show30': table_show[29]
                                           ,'table_show31': table_show[30],'table_show32': table_show[31],'table_show33': table_show[32]
                                           ,'table_show34': table_show[33],'table_show35': table_show[34],'table_show36': table_show[35]
                                           ,'table_show37': table_show[36],'table_show38': table_show[37],'table_show39': table_show[38]
                                           ,'table_show40': table_show[39]}
                        else:
                            context['error_data']= "error_data"  
                else:
                    context['error_data']= "error_data"  
        
    return render(
        request,
        template,
        context
    )

def Edit_school_record_admin(request):
    template = 'group2/school_record_admin.html'    # get template
    context = {}

    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)

    except: # can't get a Student object
        context = {}

    if request.method == 'POST':
        
        
                c_id=request.POST["c_id"]
                sec=request.POST["sec"]
                term=request.POST["t"]
                year=request.POST["y"]
        
                s_id1=request.POST.get("s_id1", False);
                state1=request.POST.get("state1", False);
        
                s_id2=request.POST.get("s_id2", False);
                state2=request.POST.get("state2", False);
                
                s_id3=request.POST.get("s_id3", False);
                state3=request.POST.get("state3", False);
                
                s_id4=request.POST.get("s_id4", False);
                state4=request.POST.get("state4", False);
                
                s_id5=request.POST.get("s_id5", False);
                state5=request.POST.get("state5", False);
                
                s_id6=request.POST.get("s_id6", False);
                state6=request.POST.get("state6", False);
                
                s_id7=request.POST.get("s_id7", False);
                state7=request.POST.get("state7", False);
                
                s_id8=request.POST.get("s_id8", False);
                state8=request.POST.get("state8", False);
                
                s_id9=request.POST.get("s_id9", False);
                state9=request.POST.get("state9", False);
                
                s_id10=request.POST.get("s_id10", False);
                state10=request.POST.get("state10", False);

                s_id11=request.POST.get("s_id11", False);
                state11=request.POST.get("state11", False);
        
                s_id12=request.POST.get("s_id12", False);
                state12=request.POST.get("state12", False);
                
                s_id13=request.POST.get("s_id13", False);
                state13=request.POST.get("state13", False);
                
                s_id14=request.POST.get("s_id14", False);
                state14=request.POST.get("state14", False);
                
                s_id15=request.POST.get("s_id15", False);
                state15=request.POST.get("state15", False);
                
                s_id16=request.POST.get("s_id16", False);
                state16=request.POST.get("state16", False);
                
                s_id17=request.POST.get("s_id17", False);
                state17=request.POST.get("state17", False);
                
                s_id18=request.POST.get("s_id18", False);
                state18=request.POST.get("state18", False);
                
                s_id19=request.POST.get("s_id19", False);
                state19=request.POST.get("state19", False);
                
                s_id20=request.POST.get("s_id20", False);
                state20=request.POST.get("state20", False);

                s_id21=request.POST.get("s_id21", False);
                state21=request.POST.get("state21", False);
        
                s_id22=request.POST.get("s_id22", False);
                state22=request.POST.get("state22", False);
                
                s_id23=request.POST.get("s_id23", False);
                state23=request.POST.get("state23", False);
                
                s_id24=request.POST.get("s_id24", False);
                state24=request.POST.get("state24", False);
                
                s_id25=request.POST.get("s_id25", False);
                state25=request.POST.get("state25", False);
                
                s_id26=request.POST.get("s_id26", False);
                state26=request.POST.get("state26", False);
                
                s_id27=request.POST.get("s_id27", False);
                state27=request.POST.get("state27", False);
                
                s_id28=request.POST.get("s_id28", False);
                state28=request.POST.get("state28", False);
                
                s_id29=request.POST.get("s_id29", False);
                state29=request.POST.get("state29", False);
                
                s_id30=request.POST.get("s_id30", False);
                state30=request.POST.get("state30", False);
                
                s_id31=request.POST.get("s_id31", False);
                state31=request.POST.get("state31", False);
        
                s_id32=request.POST.get("s_id32", False);
                state32=request.POST.get("state32", False);
                
                s_id33=request.POST.get("s_id33", False);
                state33=request.POST.get("state33", False);
                
                s_id34=request.POST.get("s_id34", False);
                state34=request.POST.get("state34", False);
                
                s_id35=request.POST.get("s_id35", False);
                state35=request.POST.get("state35", False);
                
                s_id36=request.POST.get("s_id36", False);
                state36=request.POST.get("state36", False);
                
                s_id37=request.POST.get("s_id37", False);
                state37=request.POST.get("state37", False);
                
                s_id38=request.POST.get("s_id38", False);
                state38=request.POST.get("state38", False);
                
                s_id39=request.POST.get("s_id39", False);
                state39=request.POST.get("state39", False);
                
                s_id40=request.POST.get("s_id40", False);
                state40=request.POST.get("state40", False);

               
                course = Course.objects.get(Course_ID=int(c_id))
                section = Section.objects.get(Course_ID=course,Section=int(sec) )
 
  
                if s_id1!=False:
                    student1 = Student.objects.get(std_id=s_id1)
                    if Grade.objects.filter(std_id=student1 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check1.Grade= state1
                            admin_check1.save()
                                
                if s_id2!=False:
                    student2 = Student.objects.get(std_id=s_id2)
                    if Grade.objects.filter(std_id=student2 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check2.Grade= state2
                            admin_check2.save()                                

                if s_id3!=False:
                    student3 = Student.objects.get(std_id=s_id3)
                    if Grade.objects.filter(std_id=student3 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check3.Grade= state3
                            admin_check3.save() 

                if s_id4!=False:
                    student4 = Student.objects.get(std_id=s_id4)
                    if Grade.objects.filter(std_id=student4 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check4.Grade= state4
                            admin_check4.save()
                            
                if s_id5!=False:
                    student5 = Student.objects.get(std_id=s_id5)
                    if Grade.objects.filter(std_id=student5 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check5=Grade.objects.get(std_id=student5 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check5.Grade= state5
                            admin_check5.save()
                            
                if s_id6!=False:
                    student6 = Student.objects.get(std_id=s_id6)
                    if Grade.objects.filter(std_id=student6 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check6=Grade.objects.get(std_id=student6 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check6.Grade= state6
                            admin_check6.save()
                            
                            
                if s_id7!=False:
                    student7 = Student.objects.get(std_id=s_id7)
                    if Grade.objects.filter(std_id=student7 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check7=Grade.objects.get(std_id=student7 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check7.Grade= state7
                            admin_check7.save()
                            
                if s_id8!=False:
                    student8 = Student.objects.get(std_id=s_id8)
                    if Grade.objects.filter(std_id=student8 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check8=Grade.objects.get(std_id=student8 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check8.Grade= state8
                            admin_check8.save()
                            
                            
                if s_id9!=False:
                    student9 = Student.objects.get(std_id=s_id9)
                    if Grade.objects.filter(std_id=student9 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check9=Grade.objects.get(std_id=student9 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check9.Grade= state9
                            admin_check9.save()
                            
                            
                if s_id10!=False:
                    student10 = Student.objects.get(std_id=s_id10)
                    if Grade.objects.filter(std_id=student10 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check10=Grade.objects.get(std_id=student10 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check10.Grade= state10
                            admin_check10.save()
                            
                if s_id11!=False:
                    student11 = Student.objects.get(std_id=s_id11)
                    if Grade.objects.filter(std_id=student11 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check11=Grade.objects.get(std_id=student11 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check11.Grade= state11
                            admin_check11.save()
                                
                if s_id12!=False:
                    student12 = Student.objects.get(std_id=s_id12)
                    if Grade.objects.filter(std_id=student12 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check12=Grade.objects.get(std_id=student12 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check12.Grade= state12
                            admin_check12.save()                                

                if s_id13!=False:
                    student13 = Student.objects.get(std_id=s_id13)
                    if Grade.objects.filter(std_id=student13 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check13=Grade.objects.get(std_id=student13 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check13.Grade= state13
                            admin_check13.save() 

                if s_id14!=False:
                    student14 = Student.objects.get(std_id=s_id14)
                    if Grade.objects.filter(std_id=student14 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check14=Grade.objects.get(std_id=student14 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check14.Grade= state14
                            admin_check14.save()
                            
                if s_id15!=False:
                    student15 = Student.objects.get(std_id=s_id15)
                    if Grade.objects.filter(std_id=student15 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check15=Grade.objects.get(std_id=student15 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check15.Grade= state15
                            admin_check15.save()
                            
                if s_id16!=False:
                    student16 = Student.objects.get(std_id=s_id16)
                    if Grade.objects.filter(std_id=student16 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check16=Grade.objects.get(std_id=student16 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check16.Grade= state16
                            admin_check16.save()
                            
                            
                if s_id17!=False:
                    student17 = Student.objects.get(std_id=s_id17)
                    if Grade.objects.filter(std_id=student17 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check17=Grade.objects.get(std_id=student17 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check17.Grade= state17
                            admin_check17.save()
                            
                if s_id18!=False:
                    student18 = Student.objects.get(std_id=s_id18)
                    if Grade.objects.filter(std_id=student18 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check18=Grade.objects.get(std_id=student18 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check18.Grade= state18
                            admin_check18.save()
                            
                            
                if s_id19!=False:
                    student19 = Student.objects.get(std_id=s_id19)
                    if Grade.objects.filter(std_id=student19 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check19=Grade.objects.get(std_id=student19 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check19.Grade= state19
                            admin_check19.save()
                            
                            
                if s_id20!=False:
                    student20 = Student.objects.get(std_id=s_id20)
                    if Grade.objects.filter(std_id=student20 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check20=Grade.objects.get(std_id=student20 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check20.Grade= state20
                            admin_check20.save()
                        
                if s_id21!=False:
                    student21 = Student.objects.get(std_id=s_id21)
                    if Grade.objects.filter(std_id=student21 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check21=Grade.objects.get(std_id=student21 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check21.Grade= state21
                            admin_check21.save()
                                
                if s_id22!=False:
                    student22 = Student.objects.get(std_id=s_id22)
                    if Grade.objects.filter(std_id=student22 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check22=Grade.objects.get(std_id=student22 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check22.Grade= state22
                            admin_check22.save()                                

                if s_id23!=False:
                    student23 = Student.objects.get(std_id=s_id23)
                    if Grade.objects.filter(std_id=student23 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check23=Grade.objects.get(std_id=student23 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check23.Grade= state23
                            admin_check23.save() 

                if s_id24!=False:
                    student24 = Student.objects.get(std_id=s_id24)
                    if Grade.objects.filter(std_id=student24 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check24=Grade.objects.get(std_id=student24 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check24.Grade= state24
                            admin_check24.save()
                            
                if s_id25!=False:
                    student25 = Student.objects.get(std_id=s_id25)
                    if Grade.objects.filter(std_id=student25 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check25=Grade.objects.get(std_id=student25 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check25.Grade= state25
                            admin_check25.save()
                            
                if s_id26!=False:
                    student26 = Student.objects.get(std_id=s_id26)
                    if Grade.objects.filter(std_id=student26 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check26=Grade.objects.get(std_id=student26 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check26.Grade= state26
                            admin_check26.save()
                            
                            
                if s_id27!=False:
                    student27 = Student.objects.get(std_id=s_id27)
                    if Grade.objects.filter(std_id=student27 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check27=Grade.objects.get(std_id=student27 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check27.Grade= state27
                            admin_check27.save()
                            
                if s_id28!=False:
                    student28 = Student.objects.get(std_id=s_id28)
                    if Grade.objects.filter(std_id=student28 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check28=Grade.objects.get(std_id=student28 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check28.Grade= state28
                            admin_check28.save()
                            
                            
                if s_id29!=False:
                    student29 = Student.objects.get(std_id=s_id29)
                    if Grade.objects.filter(std_id=student29 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check29=Grade.objects.get(std_id=student29 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check29.Grade= state29
                            admin_check29.save()
                            
                            
                if s_id30!=False:
                    student30 = Student.objects.get(std_id=s_id30)
                    if Grade.objects.filter(std_id=student30 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check30=Grade.objects.get(std_id=student30 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check30.Grade= state30
                            admin_check30.save()
                            
                if s_id31!=False:
                    student31 = Student.objects.get(std_id=s_id31)
                    if Grade.objects.filter(std_id=student31 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check31=Grade.objects.get(std_id=student31 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check31.Grade= state31
                            admin_check31.save()
                                
                if s_id32!=False:
                    student32 = Student.objects.get(std_id=s_id32)
                    if Grade.objects.filter(std_id=student32 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check32=Grade.objects.get(std_id=student32 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check32.Grade= state32
                            admin_check32.save()                                

                if s_id33!=False:
                    student33 = Student.objects.get(std_id=s_id33)
                    if Grade.objects.filter(std_id=student33 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check33=Grade.objects.get(std_id=student33 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check33.Grade= state33
                            admin_check33.save() 

                if s_id34!=False:
                    student34 = Student.objects.get(std_id=s_id34)
                    if Grade.objects.filter(std_id=student34 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check34=Grade.objects.get(std_id=student34 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check34.Grade= state34
                            admin_check34.save()
                            
                if s_id35!=False:
                    student35 = Student.objects.get(std_id=s_id35)
                    if Grade.objects.filter(std_id=student35 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check35=Grade.objects.get(std_id=student35 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check35.Grade= state35
                            admin_check35.save()
                            
                if s_id36!=False:
                    student36 = Student.objects.get(std_id=s_id36)
                    if Grade.objects.filter(std_id=student36 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check36=Grade.objects.get(std_id=student36 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check36.Grade= state36
                            admin_check36.save()
                            
                            
                if s_id37!=False:
                    student37 = Student.objects.get(std_id=s_id37)
                    if Grade.objects.filter(std_id=student37 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check37=Grade.objects.get(std_id=student37 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check37.Grade= state37
                            admin_check37.save()
                            
                if s_id38!=False:
                    student38 = Student.objects.get(std_id=s_id38)
                    if Grade.objects.filter(std_id=student38 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check38=Grade.objects.get(std_id=student38 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check38.Grade= state38
                            admin_check38.save()
                            
                            
                if s_id39!=False:
                    student39 = Student.objects.get(std_id=s_id39)
                    if Grade.objects.filter(std_id=student39 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check39=Grade.objects.get(std_id=student39 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check39.Grade= state39
                            admin_check39.save()
                            
                            
                if s_id40!=False:
                    student40 = Student.objects.get(std_id=s_id40)
                    if Grade.objects.filter(std_id=student40 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ'):
                            admin_check40=Grade.objects.get(std_id=student40 ,Course_ID=course,Section=section,year=int(year),term=int(term),check='อนุมัติ')
                            admin_check40.Grade= state40
                            admin_check40.save()
                            
                            
                            
    return render(
        request,
        template,
        context
    )

def Add_edit_viyanipon(request):
    template = 'group2/viyanipon.html'    # get template
    context = {}

    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj}

    except: # can't get a Student object
        context = {}
        

    if request.method == 'POST':

        t=request.POST.get("t", False);
        th_offer=request.POST.get("th_offer", False);
        en_offer=request.POST.get("en_offer", False);
        Date_test=request.POST.get("Date_test", False);
        Date_advance=request.POST.get("Date_advance", False);
        Date_protect=request.POST.get("Date_protect", False);        
        
        if t!=False:
            if Viyanipon.objects.filter(std_id=studentObj):
               T=Viyanipon.objects.get(std_id=studentObj)
               T.Teacher=t
               T.save()

            else:    
                T=Viyanipon(std_id=studentObj,Teacher=t)
                T.save()


        if th_offer!=False:
            if Viyanipon.objects.filter(std_id=studentObj):
               T=Viyanipon.objects.get(std_id=studentObj)
               T.Offer_th=th_offer
               T.save()

            else:    
                T=Viyanipon(std_id=studentObj,Offer_th=th_offer)
                T.save()


        if en_offer!=False:
            if Viyanipon.objects.filter(std_id=studentObj):
               T=Viyanipon.objects.get(std_id=studentObj)
               T.Offer_en=en_offer
               T.save()

            else:    
                T=Viyanipon(std_id=studentObj,Offer_en=en_offer)
                T.save()
            
        if Date_test !="" :
            year1,month1,day1 = Date_test.split("-")
            year1=int(year1)+543
            year1=str(year1)
            
            if Viyanipon.objects.filter(std_id=studentObj):
               T=Viyanipon.objects.get(std_id=studentObj) 
               T.Test=str(day1+"-"+month1+"-"+year1)
               T.save()       
            else:    
                T=Viyanipon(std_id=studentObj,Test=str(day1+"-"+month1+"-"+year1))
                T.save()
        
        if Date_advance !="" :
            year2,month2,day2 = Date_advance.split("-")
            year2=int(year2)+543
            year2=str(year2)
            
            if Viyanipon.objects.filter(std_id=studentObj):
               T=Viyanipon.objects.get(std_id=studentObj) 
               T.Advance_Test=str(day2+"-"+month2+"-"+year2)
               T.save()       
            else:    
                T=Viyanipon(std_id=studentObj,Advance_Test=str(day2+"-"+month2+"-"+year2))
                T.save()
                
        if Date_protect !="" :
            year3,month3,day3 = Date_protect.split("-")
            year3=int(year3)+543
            year3=str(year3)
            
            if Viyanipon.objects.filter(std_id=studentObj):
               T=Viyanipon.objects.get(std_id=studentObj) 
               T.Protect_Test=str(day3+"-"+month3+"-"+year3)
               T.save()       
            else:    
                T=Viyanipon(std_id=studentObj,Protect_Test=str(day3+"-"+month3+"-"+year3))
                T.save()

        table_show=Viyanipon.objects.filter(std_id=studentObj) 
        context = {'table_show': table_show,'studentObj': studentObj}

    return render(
        request,
        template,
        context
    )

def viyanipon(request):
    template = 'group2/viyanipon.html'    # get template
    context = {}

    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj}

    except: # can't get a Student object
        context = {}
        

    table_show=Viyanipon.objects.filter(std_id=studentObj) 
    context = {'table_show': table_show,'studentObj': studentObj}



    return render(
        request,
        template,
        context
    )

def edit_viyanipon(request):
    template = 'group2/edit_viyanipon.html'    # get template
    context = {}

    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context = {'studentObj': studentObj}

    except: # can't get a Student object
        context = {}

    table_show=Viyanipon.objects.filter(std_id=studentObj) 
    context = {'table_show': table_show,'studentObj': studentObj}


    return render(
        request,
        template,
        context
    )

