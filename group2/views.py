#--coding: utf-8--
import datetime
import time
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group2.models import *
from login.models import *
from datetime import datetime
from django.utils import timezone
from datetime import datetime
from array import array


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
	
def data_student_admin(request, id):
    template = "group2/data_student.html"
    context = {}
    print id
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        context['currentUser'] = currentUser
        studentObj = Student.objects.all()
        studentCur = Student.objects.get(std_id=id)
        context = {'studentObj': studentObj, 'studentCur': studentCur}
        context['studentObj'] = studentObj
        print studentObj

    except: # can't get a Student object
        context = {}

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
    table_show=Grade.objects.filter(std_id=studentObj ,check="อนุมัติ")
    context = {'table_show': table_show,'studentObj':studentObj}
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
		
	
    
    #DS = detailStudy(grade=grade)
    #DS.save()
		
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

    
    year=int(year)
    year=year+2543





    number_table1=Grade.objects.filter(std_id=studentObj ,year=year,term=1)
    number_table2=Grade.objects.filter(std_id=studentObj ,year=year,term=2)
    context['studentObj'] = studentObj
    context['number_table1'] = number_table1
    context['number_table2'] = number_table2

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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )
		#Course = Course.objects.get(Course_ID = )
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}

    
    if request.method == 'POST':
        c1=request.POST["c1"]
        s1=request.POST["s1"]
        
        c2=request.POST["c2"]
        s2=request.POST["s2"]
        
        c3=request.POST["c3"]
        s3=request.POST["s3"]
        
        c4=request.POST["c4"]
        s4=request.POST["s4"]

 
        if c1!="":
           if Section.objects.filter(Section=int(s1),Course_ID=int(c1) ):
              number_table1=Section.objects.filter(Section=int(s1),Course_ID=int(c1) )
              if c2=="":
                    context={'number_table1': number_table1,'studentObj':studentObj}
              else:
                    if Section.objects.filter(Section=int(s2),Course_ID=int(c2) ):
                        number_table2=Section.objects.filter(Section=int(s2),Course_ID=int(c2) )
                        if c3=="":
                            context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2}
                        else:
                            if Section.objects.filter(Section=int(s3),Course_ID=int(c3) ):
                                number_table3=Section.objects.filter(Section=int(s3),Course_ID=int(c3) )
                                if c4=="":
                                    context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2}
                                else: 
                                    if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                        number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2,'number_table3': number_table3,'number_table4': number_table4}
                                    else:
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2,'number_table3': number_table3}
          
                            else:
                                if c4=="":
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2}
                                else:  
                                    if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                        number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2,'number_table4': number_table4}
                                    else:
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table2': number_table2}
                    
                    else:
                        if c3=="":
                            context={'number_table1': number_table1,'studentObj':studentObj}
                        else:               
                            if Section.objects.filter(Section=int(s3),Course_ID=int(c3) ):
                                number_table3=Section.objects.filter(Section=int(s3),Course_ID=int(c3) )
                                if c4=="":
                                    context={'number_table1': number_table1,'studentObj':studentObj,'number_table3': number_table3}
                                else:
                                    if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                        number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table3': number_table3,'number_table4': number_table4}
                                    else:
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table3': number_table3}
                            else:
                                if c4=="":
                                        context={'number_table1': number_table1,'studentObj':studentObj}
                                else:                   
                                    if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                        number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                        context={'number_table1': number_table1,'studentObj':studentObj,'number_table4': number_table4}
                                    else:
                                        context={'number_table1': number_table1,'studentObj':studentObj}
           
           
           
           else:
              if c2=="":
                 context={'studentObj':studentObj}
              else:
               if Section.objects.filter(Section=int(s2),Course_ID=int(c2) ):
                  number_table2=Section.objects.filter(Section=int(s2),Course_ID=int(c2) )
                  if c3=="":
                   context={'number_table2': number_table2,'studentObj':studentObj}
                  else: 
                        if Section.objects.filter(Section=int(s3),Course_ID=int(c3) ):
                            number_table3=Section.objects.filter(Section=int(s3),Course_ID=int(c3) )
                            if c4=="":
                               context={'number_table2': number_table2,'studentObj':studentObj,'number_table3': number_table3}
                            else: 
                                    if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                          number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                          context={'studentObj':studentObj,'number_table2': number_table2,'number_table3': number_table3,'number_table4': number_table4}
                                    else:
                                        context={'studentObj':studentObj,'number_table2': number_table2,'number_table3': number_table3}
          
                        else:
                            if c4=="":
                               context={'number_table2': number_table2,'studentObj':studentObj}
                            else:                            
                                    if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                        number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                        context={'studentObj':studentObj,'number_table2': number_table2,'number_table4': number_table4}
                                    else:
                                        context={'studentObj':studentObj,'number_table2': number_table2}
               else:
                 if c3=="":
                    context={'studentObj':studentObj}
                 else:
                   if Section.objects.filter(Section=int(s3),Course_ID=int(c3) ):
                      number_table3=Section.objects.filter(Section=int(s3),Course_ID=int(c3) )
                      if c4=="":
                            context={'studentObj':studentObj,'number_table3': number_table3}
                      else:
                            if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                context={'studentObj':studentObj,'number_table3': number_table3,'number_table4': number_table4}
                            else:
                                context={'studentObj':studentObj,'number_table3': number_table3}
                   else:
                      if c4=="":
                            context={'studentObj':studentObj}
                      else:
                            if Section.objects.filter(Section=int(s4),Course_ID=int(c4) ):
                                number_table4=Section.objects.filter(Section=int(s4),Course_ID=int(c4) )
                                context={'studentObj':studentObj,'number_table4': number_table4}
                            else:
                                context={'studentObj':studentObj}
        
        else:
            
             context['put_frist']= "put_frist"    
                


        
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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )
		#Course = Course.objects.get(Course_ID = )
        context['studentObj'] = studentObj
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}

    
    if request.method == 'POST':
        c1=request.POST["c1"]
        s1=request.POST["s1"]
        


 
        if c1!="":
           if Section.objects.filter(Section=int(s1),Course_ID=int(c1) ):
              number_table1=Section.objects.filter(Section=int(s1),Course_ID=int(c1) )
              context={'number_table1': number_table1,'studentObj':studentObj}
           
           
           else:
              
                context={'studentObj':studentObj}
        
        else:
            
             context['error_course']= "error_course"    
                


        
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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

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

    
    if request.method == 'POST':
        
        c_id=request.POST["c_id"]
        sec=request.POST["sec"]
        
        s_id1=request.POST["s_id1"]
        state1=request.POST["state1"]
        
        s_id2=request.POST["s_id2"]
        state2=request.POST["state2"]
        
        s_id3=request.POST["s_id3"]
        state3=request.POST["state3"]
        
        s_id4=request.POST["s_id4"]
        state4=request.POST["state4"]
        
        date=time.strftime("%x")
        month,day,year = date.split("/")

        day=int(day)
        year=int(year)
        year=year+2543
    

        if month=="07":
           if day >= 10 & day <= 31:
                t="1"
                if c_id=="":
                   context['error_course']= "error_course"
                else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save() 
                                
                            
           
                    else:
            
                        context['put_frist']= "put_frist"    
                
                
                
                
                
                
                
                
                
           else:
            context['error_date']= "error_date" 
            
        elif month=="01":
            if day>=11 & day<= 31:
               t="2"
               if c_id=="":
                   context['error_course']= "error_course"
               else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save()                
               
               
               
            else:
                 context['error_date']= "error_date"
    
    
    
    
        elif month=="02":
             if day==1: 
                t="2"
                if c_id=="":
                   context['error_course']= "error_course"
                else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save() 





             else:
                 context['error_date']= "error_date" 
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

    
    if request.method == 'POST':
        
        c_id=request.POST["c_id"]
        sec=request.POST["sec"]
        
        s_id1=request.POST["s_id1"]
        state1=request.POST["state1"]
        
        s_id2=request.POST["s_id2"]
        state2=request.POST["state2"]
        
        s_id3=request.POST["s_id3"]
        state3=request.POST["state3"]
        
        s_id4=request.POST["s_id4"]
        state4=request.POST["state4"]
        
        date=time.strftime("%x")
        month,day,year = date.split("/")

        day=int(day)
        year=int(year)
        year=year+2543
    

        if month=="07" or  month=="08":
           if day >= 10 & day <= 31:
                t="1"
                if c_id=="":
                   context['error_course']= "error_course"
                else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save() 
                                
                            
           
                    else:
            
                        context['put_frist']= "put_frist"                
                
           else:
            context['error_date']= "error_date" 
            
            
        elif month=="09" or month=="10":
            if day>=1 & day<= 31:
               t="1"
               if c_id=="":
                   context['error_course']= "error_course"
               else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save()                
               
               
               
            else:
                 context['error_date']= "error_date"            
            
            
        elif month=="11" :
            if day>=1 & day<= 2:
               t="1"
               if c_id=="":
                   context['error_course']= "error_course"
               else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save()                
               
               
               
            else:
                 context['error_date']= "error_date"            
                       
            
            
            
            
            
        elif month=="01":
            if day>=11 & day<= 31:
               t="2"
               if c_id=="":
                   context['error_course']= "error_course"
               else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save()                
               
               
               
            else:
                 context['error_date']= "error_date"
    
    
    
    
        elif month=="02"  or month=="03":
             if day>=11 & day<= 31:
                t="2"
                if c_id=="":
                   context['error_course']= "error_course"
                else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save() 

        elif month=="04"  :
             if day>=1 & day<= 4:
                t="2"
                if c_id=="":
                   context['error_course']= "error_course"
                else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check1.check= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                admin_check2.check= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check1.check= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check2.check= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                   admin_check3.check= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check1.check= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check2.check= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check3.check= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),Grade='0')
                                    admin_check4.check= state4
                                    admin_check4.save() 



             else:
                 context['error_date']= "error_date" 
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
        
        
        #a=len(Section.objects.all() )
        
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

        #a=len(Section.objects.all() )
        
#Course_ID.Credit=course

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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

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
        if month=="07":
           if day >= 10 & day <= 31:
                t="1"
                grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc ,check='เรียน')
                grade_put.save()
                context['success']= "success" 
           else:
            context['error_date']= "error_date" 
            
        elif month=="01":
            if day>=11 & day<= 31:
               t="2"
               grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc ,check='เรียน')
               grade_put.save()
               context['success']= "success" 
               
            else:
                 context['error_date']= "error_date" 
    
        elif month=="02":
             if day==1: 
                t="2"
                grade_put=Grade(std_id=studentObj,Course_ID=course ,year=year,term=int(t),Grade='0',Section=secc ,check='เรียน')
                grade_put.save()
                context['success']= "success" 
        
                
             else:
                   context['error_date']= "error_date" 
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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}



    
    if request.method == 'POST':
        

        
        c_id1=request.POST["c_id1"]
        sec1=request.POST["sec1"]
        
        date=time.strftime("%x")
        month,day,year = date.split("/")

        day=int(day)
        year=int(year)
        year=year+2543
        
        

        if month=="07" or month=="08" :
                if day >= 10 & day <= 31:
                    t="1"
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1))
                    
                        
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='0')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
                    
        elif month=="09" or month=="10" :
                if day >= 1 & day <= 31:
                    t="1"
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1))
                    
                        
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='0')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
        elif  month=="11":
                if day >= 1 & day <= 2:
                    t="1"
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1))
                    
                        
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='0')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
                    
        elif  month=="01":
                if day >= 11 & day <= 31:
                    t="2"
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1))
                    
                        
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='0')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
        elif  month=="02" or month=="03":
                if day >= 1 & day <= 31:
                    t="2"
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1))
                    
                        
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='0')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
                    context['success']= "success"
                    
        elif  month=="04":
                if day >= 1 & day <= 4:
                    t="2"
                    course1 = Course.objects.get(Course_ID=int(c_id1))
                    section1 = Section.objects.get(Course_ID=int(c_id1))
                    
                        
                    admin_check1=Grade.objects.get(std_id=studentObj ,Course_ID=course1,Section=section1,year=year,term=int(t),Grade='0')
                    admin_check1.check= "ดรอป"
                    admin_check1.save()
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


	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}


    if request.method == 'POST':
        c_id=request.POST["c1"]
        sec=request.POST["s1"]
 


   
    
     
        if c_id=="":
            if sec==" ":
                context['error_find_course']= "error_find_course"
                context['error_find_sec']= "error_find_sec"
            else:
                context['error_find_course']= "error_find_course"
        else:
            if sec==" ":
                context['error_find_sec']= "error_find_sec"
            else:
                if Course.objects.filter(Course_ID=int(c_id)):
                    course = Course.objects.get(Course_ID=int(c_id))
                    
                    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))

                    date=time.strftime("%x")
                    month,day,year = date.split("/")

                    day=int(day)
                    year=int(year)
                    year=year+2543
                    if Grade.objects.filter(Course_ID=course ,Section=secc  ):
                
                        if month=="07":
                            if day >= 10 & day <= 31:
                                t="1"
                         
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
                        
                            else:
                                context['error_date']= "error_date" 
            
                        elif month=="01":
                            if day>=11 & day<= 31:
                                t="2"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
               
                            else:
                                context['error_date']= "error_date" 
    
                        elif month=="02":
                            if day==1: 
                                t="2"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
        
                
                            else:
                                context['error_date']= "error_date"                
              
                    else:

                        context['error_data']= "error_data" 

                else:
                    context['error_data']= "error_data" 
            




 
    return render(
        request,
        template,
        context
    )


def Find_Admin_check_drop(request):
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


    if request.method == 'POST':
        c_id=request.POST["c1"]
        sec=request.POST["s1"]
 


   
    
     
        if c_id=="":
            if sec==" ":
                context['error_find_course']= "error_find_course"
                context['error_find_sec']= "error_find_sec"
            else:
                context['error_find_course']= "error_find_course"
        else:
            if sec==" ":
                context['error_find_sec']= "error_find_sec"
            else:
                if Course.objects.filter(Course_ID=int(c_id)):
                    course = Course.objects.get(Course_ID=int(c_id))
                    
                    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))

                    date=time.strftime("%x")
                    month,day,year = date.split("/")

                    day=int(day)
                    year=int(year)
                    year=year+2543
                    if Grade.objects.filter(Course_ID=course ,Section=secc  ):
                
                        if month=="08" or month=="07":
                            if day >= 10 & day <= 31:
                                t="1"
                         
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
                        
                            else:
                                context['error_date']= "error_date" 
            
                        elif month=="09"  or month=="10":
                            if day>=1 & day<= 31:
                                t="1"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
               
                            else:
                                context['error_date']= "error_date" 
            
            
                        elif month=="11"  :
                            if day>=1 & day<= 2:
                                t="1"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
               
                            else:
                                context['error_date']= "error_date" 
            
                        elif month=="01":
                            if day>=11 & day<= 31:
                                t="2"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
               
                            else:
                                context['error_date']= "error_date" 
    
                        elif month=="02" or month=="03"  :
                            if day>=1 & day<= 31:
                                t="2"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
        
                
                            else:
                                context['error_date']= "error_date"                
              
                        elif month=="04"   :
                            if day>=1 & day<= 4:
                                t="2"
                                table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                                context = {'table_show': table_show}
        
                
                            else:
                                context['error_date']= "error_date" 
              
                    else:

                        context['error_data']= "error_data" 

                else:
                    context['error_data']= "error_data" 
            




 
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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}



    if request.method == 'POST':
        c_id=request.POST["c_id"]
        sec=request.POST["sec"]
 


   
    
     
        if c_id=="":
            if sec==" ":
                context['error_find_course']= "error_find_course"
                context['error_find_sec']= "error_find_sec"
            else:
                context['error_find_course']= "error_find_course"
        else:
            if sec==" ":
                context['error_find_sec']= "error_find_sec"
            else:
                if Course.objects.filter(Course_ID=int(c_id)):
                    course = Course.objects.get(Course_ID=int(c_id))
                    
                    secc = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))
                    table_show=Grade.objects.filter(Course_ID=course ,Section=secc  )
                    context = {'table_show': table_show}
                        
                else:
                    context['error_date']= "error_date" 
            
        
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
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}

    if request.method == 'POST':
        
        
                c_id=request.POST["c_id"]
                sec=request.POST["sec"]
                t=request.POST["t"]
        
                s_id1=request.POST["s_id1"]
                state1=request.POST["state1"]
        
                s_id2=request.POST["s_id2"]
                state2=request.POST["state2"]
        
                s_id3=request.POST["s_id3"]
                state3=request.POST["state3"]
        
                s_id4=request.POST["s_id4"]
                state4=request.POST["state4"]
                
                date=time.strftime("%x")
                month,day,year = date.split("/")

                
                year=int(year)
                year=year+2543
                
                section = Section.objects.get(Section=int(sec) ,Course_ID=int(c_id))
        

                if c_id=="":
                    context['error_course']= "error_course"
                else:    
                    if s_id1!="":
                        #have data
                        course = Course.objects.get(Course_ID=int(c_id))
                        section = Section.objects.get(Course_ID=int(c_id))
                        student1 = Student.objects.get(std_id=s_id1)
                        #student2 = Student.objects.get(std_id=s_id2)
                        #student3 = Student.objects.get(std_id=s_id3)
                        #student4 = Student.objects.get(std_id=s_id4)
                        
                        if s_id2=="":
                            if Grade.objects.filter(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ'):
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                admin_check1.Grade= state1
                                admin_check1.save()
                            else:
                                context['error_data']= "error_data"
                

                        else:
                            if s_id3=="":
                                admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                admin_check1.Grade= state1
                                admin_check1.save()
                                
                                student2 = Student.objects.get(std_id=s_id2)
                                admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                admin_check2.Grade= state2
                                admin_check2.save()                                  
                

                            else:
                                if s_id4=="":
                                   admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                   admin_check1.Grade= state1
                                   admin_check1.save()
                                
                                   student2 = Student.objects.get(std_id=s_id2)
                                   admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                   admin_check2.Grade= state2
                                   admin_check2.save()                                  

                                   
                                   student3 = Student.objects.get(std_id=s_id3)
                                   admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                   admin_check3.Grade= state3
                                   admin_check3.save() 
                
                                else:
                                    admin_check1=Grade.objects.get(std_id=student1 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                    admin_check1.Grade= state1
                                    admin_check1.save()
                                
                                    student2 = Student.objects.get(std_id=s_id2)
                                    admin_check2=Grade.objects.get(std_id=student2 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                    admin_check2.Grade= state2
                                    admin_check2.save()                                  

                                   
                                    student3 = Student.objects.get(std_id=s_id3)
                                    admin_check3=Grade.objects.get(std_id=student3 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                    admin_check3.Grade= state3
                                    admin_check3.save()
                                    
                                    student4 = Student.objects.get(std_id=s_id4)
                                    admin_check4=Grade.objects.get(std_id=student4 ,Course_ID=course,Section=section,year=year,term=int(t),check='อนุมัติ')
                                    admin_check4.Grade= state4
                                    admin_check4.save() 
                                
                            
           
                    else:
            
                        context['put_frist']= "put_frist"    
                
                
                
                
                
                


            
        
    return render(
        request,
        template,
        context
    )








	


	

def viyanipon(request):
    template = 'group2/viyanipon.html'    # get template
    context = {}
    #this = request.user
    #current = UserProfile.objects.get(user = this)
    #adviser = viyanipon_adviser.objects.get(std_id = current)
    #print adviser.std_id, adviser.teach_name,adviser.adviser
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}
    
    
    thisuser = request.user
    currentUser = UserProfile.objects.get(user = thisuser)
    studentObj = Student.objects.get(userprofile = currentUser)
    template = 'group2/viyanipon_show.html'
    table_show=viyanipon_adviser.objects.filter(std_id=studentObj.std_id)
    table_name=viyanipon_name.objects.filter(std_id=studentObj.std_id )
    table_project=viyanipon_project.objects.filter(std_id=studentObj.std_id )
    table_test=viyanipon_test.objects.filter(std_id=studentObj.std_id )
    table_testend=viyanipon_testend.objects.filter(std_id=studentObj.std_id )
    context = {'table_show':table_show,'table_name':table_name,'studentObj':studentObj,'table_project':table_project,'table_test':table_test,'table_testend':table_testend}
    
    return render(
        request,
        template,
        context
    )

def viyaniponshow(request):
    template = 'group2/viyanipon_show.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/error.html'
        return render(request, template, {})
    
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj
    
    except: # can't get a Student object
        context = {}
    
    thisuser = request.user
    currentUser = UserProfile.objects.get(user = thisuser)
    studentObj = Student.objects.get(userprofile = currentUser)
    if request.method == 'POST':
        teach = request.POST['teach_name']
        viyanipon = request.POST['viyanipon_name']
        project = request.POST['project_name']
        test = request.POST['test']
        testend = request.POST['testend']
        if teach == 'true' :
            adviser = request.POST['adviser']
            q = viyanipon_adviser(std_id=studentObj.std_id,teach_name=teach,adviser=adviser)
            q.save()
        if viyanipon == 'true' :
            name_th = request.POST['name_thai']
            name_eng = request.POST['name_eng']
            p = viyanipon_name(std_id=studentObj.std_id,name=viyanipon,name_thai=name_th,name_eng=name_eng)
            p.save()
        if project == 'true' :
            #date = request.POST['date']
            #valid_date = datetime.strptime(date, '%d-%m-%Y').date()
            #print ">>> ", valid_date, " ", type(valid_date), " <<<"
            name_day = request.POST['name_day']
            name_month = request.POST['name_month']
            name_year = request.POST['name_year']
            # date = request.POST['date']
            q = viyanipon_project(std_id=studentObj.std_id,project_name=project,name_day=name_day,name_month=name_month,name_year=name_year)
            q.save()
        if test == 'true' :
            test_day = request.POST['test_day']
            test_month = request.POST['test_month']
            test_year = request.POST['test_year']
            q = viyanipon_test(std_id=studentObj.std_id,test=test,test_day=test_day,test_month=test_month,test_year=test_year)
            q.save()
        if testend == 'true' :
            day = request.POST['testend_day']
            month = request.POST['testend_month']
            year = request.POST['testend_year']
            q = viyanipon_testend(std_id=studentObj.std_id,testend=testend,testend_day=day,testend_month=month,testend_year=year)
            q.save()
        
        table_show=viyanipon_adviser.objects.filter(std_id=studentObj.std_id )
        table_name=viyanipon_name.objects.filter(std_id=studentObj.std_id )
        table_project=viyanipon_project.objects.filter(std_id=studentObj.std_id )
        table_test=viyanipon_test.objects.filter(std_id=studentObj.std_id )
        table_testend=viyanipon_testend.objects.filter(std_id=studentObj.std_id )
        template = 'group2/viyanipon.html'
        context = {'table_show': table_show,'table_name':table_name,'studentObj':studentObj,'table_project':table_project,'table_test':table_test,'table_testend':table_testend}
        
    return render(
        request,
        template,
        context
    )



def viyanipon_admin(request):
    template = 'group2/viyanipon_admin.html'    # get template
    context = {}
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}
    if request.method == 'POST':
        search = request.POST['search']
        if search != '' :
            table_std = Student.objects.filter(std_id=search )
            table_stdobj = UserProfile.objects.all()#filter(user_id=search)
            table_show=viyanipon_adviser.objects.filter(std_id=search )
            table_name=viyanipon_name.objects.filter(std_id=search )
            table_project=viyanipon_project.objects.filter(std_id=search )
            table_test=viyanipon_test.objects.filter(std_id=search )
            table_testend=viyanipon_testend.objects.filter(std_id=search )
            template = 'group2/viyanipon_admin2.html'
            context = {'table_stdobj':table_stdobj,'table_show': table_show,'table_name':table_name,'studentObj':table_std,'table_project':table_project,'table_test':table_test,'table_testend':table_testend}
        
    return render(
        request,
        template,
        context
    )

def viyanipon_admin2(request):
    template = 'group2/viyanipon_admin2.html'    # get template
    context = {}
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj

    except: # can't get a Student object
        context = {}
    print 'sdscdscw3435465786432'
    #if request.method == 'POST':
    #    search = request.POST['search']
    #    #thisuser = request.user
    #    #currentUser = UserProfile.objects.get(user = thisuser)
    #    #studentObj = Student.objects.get(userprofile = currentUser)
    #    table_std = Student.objects.filter(std_id=search )
    #    print table_std
    #    table_show=viyanipon_adviser.objects.filter(std_id=search )
    #    table_name=viyanipon_name.objects.filter(std_id=search )
    #    table_project=viyanipon_project.objects.filter(std_id=search )
    #    table_test=viyanipon_test.objects.filter(std_id=search )
    #    table_testend=viyanipon_testend.objects.filter(std_id=search )
    #    context = {'table_show': table_show,'table_name':table_name,'studentObj':table_std,'table_project':table_project,'table_test':table_test,'table_testend':table_testend}
    #else :
    #    thisuser = request.user
    #    currentUser = UserProfile.objects.get(user = thisuser)
    #    studentObj = Student.objects.get(userprofile = currentUser)
    #    table_show=viyanipon_adviser.objects.filter(std_id=studentObj.std_id)
    #    table_name=viyanipon_name.objects.filter(std_id=studentObj.std_id )
    #    table_project=viyanipon_project.objects.filter(std_id=studentObj.std_id )
    #    table_test=viyanipon_test.objects.filter(std_id=studentObj.std_id )
    #    table_testend=viyanipon_testend.objects.filter(std_id=studentObj.std_id )
    #    context = {'table_show':table_show,'table_name':table_name,'studentObj':studentObj,'table_project':table_project,'table_test':table_test,'table_testend':table_testend}
    #template = 'group2/viyanipon_admin2.html'
    #print 'dsvdsfbfgbfbdfghjkl'
    if request.method == 'POST':
        template = 'group2/viyanipon_admin.html'
    return render(
        request,
        template,
        context
    )
