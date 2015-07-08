#--coding: utf-8--
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group2.models import *
from login.models import *
from datetime import datetime
from django.utils import timezone



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

    return render(
        request,
        template,
        context
    )
	
def registeration(request):
    template = 'group2/registeration.html'    # get template
    context = {}
    if getUserType(request) != '0':
        template = 'group2/error.html'
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
    table_show=Grade.objects.filter(std_id=studentObj )
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
        template = 'group2/search_course.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        number_table=Grade.objects.all()
        course = Course.objects.all()#get(Course_ID = number_table.Course_ID.Course_ID)
        #if len(number_table)==0 :
			#template = 'group2/error.html'
        #context = {'studentObj':studentObj,'number_table':number_table,'course':course}
        context['studentObj'] = studentObj
        context['number_table'] = number_table
        context['course'] = course
		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}


    return render(
        request,
        template,
        context
    )
	
	
def viyanipon(request):
    template = 'group2/viyanipon.html'    # get template
    context = {}

    if getUserType(request) != '0':
        template = 'group2/search_student.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
        context['studentObj'] = studentObj
        context['currentUser'] = currentUser

    except: # can't get a Student object
        context = {}

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
        
    #if 'std_id' in request.GET and request.GET['std_id'] :
    #    stdid = request.GET['std_id']
    #if 'teach_name' in request.GET and request.GET['teach_name'] :
    #    teach = request.GET['teach_name']
    #if 'adviser' in request.GET and request.GET['adviser'] :
    #    adviser = request.GET['adviser']
    stdid = request.GET.get('std_id','')
    teach = request.GET.get('teach_name','')
    adviser = request.GET.get('adviser','')
    if teach == "true" :
        q = viyanipon_adviser(std_id=stdid,teach_name=teach,adviser=adviser)
        q.save()
    
    return render(
        request,
        template,
        context
    )
	
def Find_course(request):
    template = 'group2/registeration.html'    # get template
    context = {}
    
    #number_table=Base.objects.all()
    if getUserType(request) != '0':
        template = 'group2/error.html'
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

    
    if 'c1' in request.GET and request.GET['c1']:
        c1 = request.GET['c1']
        if 's1' in request.GET and request.GET['s1']:
            s1 = request.GET['s1']



                   
                   
            if Section.objects.filter(Section=int(s1),Course_ID=int(c1) ):
               number_table=Section.objects.filter(Section=int(s1),Course_ID=int(c1) )
               context={'number_table': number_table,'studentObj':studentObj}
            else:
               context['error_data']= "error_data" 

           
        else:

            context['error_section']= "error_section"

        
    else:
        if 's1' in request.GET and request.GET['s1']:
            context['error_course_id']= "error_course_id"

            
        else:

            context['error_course_id']= "error_course_id"
            context['error_section']= "error_section"

        


    return render(
        request,
        template,
        context
    )


def Put_Grade(request):
    template = 'group2/regis_result.html'    # get template
    context = {}

    if getUserType(request) != '0':
        template = 'group2/error.html'
        return render(request, template, {})
	
    try:
        thisuser = request.user
        currentUser = UserProfile.objects.get(user = thisuser)
        studentObj = Student.objects.get(userprofile = currentUser)
		#Grade = Grade.objects.get(std_id = studentObj.std_id )


		#context['Grade'] = Grade

    except: # can't get a Student object
        context = {}





    if 'c_id' in request.GET and request.GET['c_id']:
        c_id = request.GET['c_id']
      

    if 'sec' in request.GET and request.GET['sec']:
        sec = request.GET['sec']


    course = Course.objects.get(Course_ID=int(c_id))
    secc = Section.objects.get(Section=int(sec) )

    y=timezone.now().year
    y=y+543

    m=timezone.now().month
    m=m+1
    
    if m==8:
       t=1
    if m==1:
       t=2   
         
    if Grade.objects.filter(std_id=studentObj,Course_ID=course ,Section=secc  ):
        context['duplicate']= "duplicate" 
    else:   
        grade_put=Grade(std_id=studentObj,Course_ID=course ,year=int(y),term=int(t),Grade='0',Section=secc )
        grade_put.save()
        
        table_show=Grade.objects.filter(std_id=studentObj )
        context = {'table_show': table_show,'studentObj':studentObj}



 
    return render(
        request,
        template,
        context
    )