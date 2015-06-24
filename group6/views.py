#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group6.models import *
from login.models import *
from datetime import datetime

def index(request):
    u = UserProfile.objects.get(user=request.user)
    s = Student.objects.get(userprofile=u)
    project = s.projectg6_set.all()
    research = []
    offer = []
    approve = []
    for p in project:
        research.append(ResearchProjectForm.objects.get(project=p))
        offer.append(OfferProjectForm.objects.get(project=p))
        approve.append(ApproveProjectForm.objects.get(project=p))
    return render(request, 'group6/index.html', {'project_list': project, 'research': research, 'offer': offer, 'approve': approve},)

def create_3forms(request):
    u = UserProfile.objects.get(user=request.user)
    if u.type != '0':
        messages.add_message(request, messages.INFO, "Only Student can create form")
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        s = Student.objects.get(userprofile=u)
        teachers = Teacher.objects.all()
        return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'numOP': 1},)

def create_3forms_add(request):
    u = UserProfile.objects.get(user=request.user)
    s = Student.objects.get(userprofile=u)
    s_list = []
    s_list.append(s)
    yearOE, nameTH, nameEN, numOP, adv, obj, scopes, benefits, reasons, priceOM, priceOO, credits, courses, semester, yearEN = "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    error_yearOE, error_nameTH, error_nameEN, error_numOP, error_adv, error_obj, error_scopes, error_benefits, error_reasons, error_priceOM, error_priceOO, error_credits, error_courses, error_semester, error_yearEN = "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    error_student = []
    error_student.append("")
    error = False
    try:
        if 'yearOfEducation' and 'name_thai' and 'name_eng' and 'numberOfPeople' and 'adviser' and 'objective' and 'scope' and 'benefit' and 'reason' and 'priceOfMaterial' and 'priceOfOther' and 'credit' and 'course' and 'semesterEnd' and 'yearEnd' in request.POST: #Check key in POST
            yearOE = request.POST['yearOfEducation'] #Get Value from key
            nameTH = request.POST['name_thai']
            nameEN = request.POST['name_eng']
            numOP = request.POST['numberOfPeople']
            adv = request.POST['adviser']
            obj = request.POST['objective']
            scopes = request.POST['scope']
            benefits = request.POST['benefit']
            reasons = request.POST['reason']
            priceOM = request.POST['priceOfMaterial']
            priceOO = request.POST['priceOfOther']
            credits = request.POST['credit']
            courses = request.POST['course']
            semester = request.POST['semesterEnd']
            yearEN = request.POST['yearEnd']
            if nameTH == "" : #Check user_name is empty???
                error_nameTH = "*กรุณาใส่ชื่อโครงงาน (ภาษาไทย)" #If empty set error message and error to true
                error = True
            elif len(ProjectG6.objects.filter(name_thai=nameTH)) != 0:
                error_nameTH = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาไทย)" #If user_name is in use set error message and error to true
                error = True
            if nameEN == "" : #Check name is empty???
                error_nameEN = "*กรุณาใส่ชื่อโครงงาน (ภาษาอังกฤษ)" #If empty set error message and error to true
                error = True
            elif len(ProjectG6.objects.filter(name_eng=nameEN)) != 0:
                error_nameEN = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาไทย)" #If user_name is in use set error message and error to true
                error = True
            if len(Teacher.objects.filter(id=int(adv))) == 0:
                error_adv = "*กรุณาเลือกที่ปรึกษาใหม่" #If user_name is in use set error message and error to true
                error = True
            if int(yearOE) > int(datetime.now().year + 543) or int(yearOE) < int(datetime.now().year + 535):
                error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If user_name is in use set error message and error to true
                error = True
            if int(numOP) > 5 or int(numOP) < 1:
                error_numOP = "*กรุณาเลือกจำนวนคนใหม่" #If user_name is in use set error message and error to true
                error = True
            if obj == "" : #check last_name is empty???
                error_obj = "*กรุณากรอกวัตถุประสงค์" #If empty set error message and error to true
                error = True
            if scopes == "" : #check last_name is empty???
                error_scopes = "*กรุณากรอกขอบเขตของการทำโครงงาน" #If empty set error message and error to true
                error = True
            if benefits == "" : #check last_name is empty???
                error_benefits = "*กรุณากรอกผลประโยชน์ที่คาดว่าจะได้รับ" #If empty set error message and error to true
                error = True
            if reasons == "" : #check last_name is empty???
                error_reasons = "*กรุณากรอกแนวเหตุผล ทฤษฏีสำคัญหรือสมมุติฐาน" #If empty set error message and error to true
                error = True
            if courses == "" : #check last_name is empty???
                error_courses = "*กรุณากรอกชื่อวิชา" #If empty set error message and error to true
                error = True
            if priceOM == "" : #Check age is empty???
                error_priceOM = "*กรุณากรอกค่าวัสดุ" #If empty set error message and error to true
                error = True
            else:
                try:
                    int(priceOM) #Check age is int???
                except ValueError:
                    error_priceOM = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                    error = True
            if priceOO == "" : #Check age is empty???
                error_priceOO = "*กรุณากรอกค่าใช้จ่ายเบ็ดเตล็ด" #If empty set error message and error to true
                error = True
            else:
                try:
                    int(priceOO) #Check age is int???
                except ValueError:
                    error_priceOO = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                    error = True
            if credits == "" : #Check age is empty???
                error_credits = "*กรุณากรอกจำนวนหน่วยกิจ" #If empty set error message and error to true
                error = True
            else:
                try:
                    int(credits) #Check age is int???
                except ValueError:
                    error_credits = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                    error = True
            if semester == "" : #Check age is empty???
                error_semester = "*กรุณากรอกภาคเรียน" #If empty set error message and error to true
                error = True
            else:
                try:
                    int(semester) #Check age is int???
                except ValueError:
                    error_semester = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                    error = True
            if yearEN == "" : #Check age is empty???
                error_yearEN = "*กรุณากรอกปีการศึกษา" #If empty set error message and error to true
                error = True
            else:
                try:
                    int(yearEN) #Check age is int???
                except ValueError:
                    error_yearEN = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                    error = True
            if 'studentID1' and 'studentNAME1' in request.POST:
                studentID = request.POST['studentID1']
                if len(Student.objects.filter(std_id=studentID)) == 1:
                    s_list.append(Student.objects.get(std_id=studentID))
                    error_student.append("")
                else:
                    s_list.append("")
                    error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                    error = True
            if 'studentID2' and 'studentNAME2' in request.POST:
                studentID = request.POST['studentID2']
                if len(Student.objects.filter(std_id=studentID)) == 1:
                    s_list.append(Student.objects.get(std_id=studentID))
                    error_student.append("")
                else:
                    s_list.append("")
                    error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                    error = True
            if 'studentID3' and 'studentNAME3' in request.POST:
                studentID = request.POST['studentID3']
                if len(Student.objects.filter(std_id=studentID)) == 1:
                    s_list.append(Student.objects.get(std_id=studentID))
                    error_student.append("")
                else:
                    s_list.append("")
                    error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                    error = True
            if 'studentID4' and 'studentNAME4' in request.POST:
                studentID = request.POST['studentID4']
                if len(Student.objects.filter(std_id=studentID)) == 1:
                    s_list.append(Student.objects.get(std_id=studentID))
                    error_student.append("")
                else:
                    s_list.append("")
                    error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                    error = True
            if error == True: #Check if error is true raise exception
                raise ValueError
        else: #If key invalid raise to exception
            raise KeyError 
    except (KeyError, ValueError): #When exception render form with error message
        teachers = Teacher.objects.all()
        return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'error_yearOE': error_yearOE, 'error_nameTH': error_nameTH, 'error_nameEN': error_nameEN, 'error_numOP': error_numOP, 'error_adv': error_adv, 'error_obj': error_obj, 'error_scopes': error_scopes, 'error_benefits': error_benefits, 'error_reasons': error_reasons, 'error_priceOM': error_priceOM, 'error_priceOO': error_priceOO, 'error_credits': error_credits, 'error_courses': error_courses, 'error_semester': error_semester, 'error_yearEN': error_yearEN, 'error_student': error_student, 'nameTH': nameTH, 'nameEN': nameEN, 'obj': obj, 'scopes': scopes, 'benefits': benefits, 'reasons': reasons, 'priceOM': priceOM, 'priceOO': priceOO, 'credits': credits, 'courses': courses, 'semester': semester, 'yearEN': yearEN, 'student_list': s_list, 'numOP': numOP},)
    project = ProjectG6(teacher = Teacher.objects.get(id=int(adv)), name_thai = nameTH, name_eng = nameEN, yearOfEducation = yearOE, objective = obj, reason = reasons, scope = scopes, benefit = benefits)
    project.save()
    project.student = s_list
    research = ResearchProjectForm(project = project, numberOfPeople = numOP)
    research.save()
    offer = OfferProjectForm(project = project, priceOfMaterial = priceOM, priceOfOther = priceOO)
    offer.save()
    approve = ApproveProjectForm(project = project, student = s, course = courses, semesterEnd = semester, yearEnd = yearEN, credit = credits)
    approve.save()
    messages.add_message(request, messages.INFO, "การสร้างฟอร์มของโปรเจคสำเร็จ")
    return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index

def approveProject(request, apID):
    department = ['','วิศวกรรมไฟฟ้าและคอมพิวเตอร์']
    faculty = ['','วิศวกรรมศาสตร์']
    scheme = ['หลักสูตรปรับปรุง Cpr.E 54','หลักสูตรปรับปรุง EE 51','หลักสูตรปรับปรุง ECE 55']
    main = ['Cpr.E','G','U','C']
    approve = ApproveProjectForm.objects.get(id=apID)
    year = int(datetime.now().year - 2000 + 43) - int(approve.student.std_id[:2])
    return render(request, 'group6/approveProject_view.html', {'approve': approve, 'scheme': scheme[int(approve.student.scheme)], 'department': department[int(approve.student.userprofile.department)], 'main': main[int(approve.student.main)], 'currentYear': year},)

def offerProject(request, opID):
    offer = OfferProjectForm.objects.get(id=opID)
    sumofprice = offer.priceOfMaterial + offer.priceOfOther
    return render(request, 'group6/offerProject_view.html', {'offer': offer, 'priceOfTotal': sumofprice},)

def researchProject(request, rpID):
    research = ResearchProjectForm.objects.get(id=rpID)
    return render(request, 'group6/researchProject_view.html', {'research': research},)

def deleteForm(request, pjID):
    p = ProjectG6.objects.get(id=pjID)
    research = ResearchProjectForm.objects.get(project=p)
    offer = OfferProjectForm.objects.get(project=p)
    approve = ApproveProjectForm.objects.get(project=p)
    messages.add_message(request, messages.INFO, "การลบฟอร์มของโปรเจคสำเร็จ")
    return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
