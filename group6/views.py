#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group6.models import *
from login.models import *
from datetime import datetime

month = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
department = ['','วิศวกรรมไฟฟ้าและคอมพิวเตอร์']
faculty = ['','วิศวกรรมศาสตร์']
scheme = ['หลักสูตรปรับปรุง Cpr.E 54','หลักสูตรปรับปรุง EE 51','หลักสูตรปรับปรุง ECE 55']
main = ['Cpr.E','G','U','C']

def index(request):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type == '0':
            s = Student.objects.get(userprofile=u)
            project = s.projectg6_set.all()
            research = []
            offer = []
            approve = []
            timeLine = []
            for p in project:
                research.append(ResearchProjectForm.objects.get(project=p))
                offer.append(OfferProjectForm.objects.get(project=p))
                approve.append(ApproveProjectForm.objects.get(project=p))
                timeLine.append(TimeLineForm.objects.get(project=p))
            return render(request, 'group6/index.html', {'project_list': project, 'research': research, 'offer': offer, 'approve': approve, 'timeLine': timeLine},)
        elif u.type == '1':
            t = Teacher.objects.get(userprofile=u)
            project = ProjectG6.objects.filter(teacher=t)
            research = []
            offer = []
            approve = []
            timeLine = []
            for p in project:
                research.append(ResearchProjectForm.objects.get(project=p))
                offer.append(OfferProjectForm.objects.get(project=p))
                approve.append(ApproveProjectForm.objects.get(project=p))
                timeLine.append(TimeLineForm.objects.get(project=p))
            return render(request, 'group6/index_teacher.html', {'project_list': project, 'research': research, 'offer': offer, 'approve': approve, 'timeLine': timeLine},)
        elif u.type == '2':
            project = ProjectG6.objects.all()
            research = []
            offer = []
            approve = []
            timeLine = []
            categories_id = []
            for p in project:
                research.append(ResearchProjectForm.objects.get(project=p))
                offer.append(OfferProjectForm.objects.get(project=p))
                approve.append(ApproveProjectForm.objects.get(project=p))
                timeLine.append(TimeLineForm.objects.get(project=p))
                categories_temp = CategoriesProject.objects.filter(project=p)
                if len(categories_temp)==0:
                    categories_id.append('')
                else:
                    categories_id.append(categories_temp[0].id)
            return render(request, 'group6/index_officer.html', {'project_list': project, 'research': research, 'offer': offer, 'approve': approve, 'timeLine': timeLine, 'categories_id':categories_id},)
    else:
        return render(request, 'base.html')

def create_3forms(request):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '0':
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถสร้างฟอร์มได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            s = Student.objects.get(userprofile=u)
            teachers = Teacher.objects.all()
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'numOP': 1, 'yearOE': int(datetime.now().year + 543), 'edit': '1'},)
    else:
        return render(request, 'base.html')

def create_3forms_add(request):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '0':
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถสร้างฟอร์มได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        s = Student.objects.get(userprofile=u)
        s_list, myCheck, process, myCheck1, myCheck2, myCheck3, myCheck4, myCheck5, myCheck6, myCheck7, myCheck8 = [], [], [], [], [], [], [], [], [], [], []
        s_list.append(s)
        yearOE, nameTH, nameEN, numOP, adv, obj, scopes, benefits, reasons, priceOM, priceOO, credits, courses, semester, yearEN, dateST, process1, process2, process3, process4, process5, process6, process7, process8, note = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        error_yearOE, error_nameTH, error_nameEN, error_numOP, error_adv, error_obj, error_scopes, error_benefits, error_reasons, error_priceOM, error_priceOO, error_credits, error_courses, error_semester, error_yearEN, error_process, error_dateST = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        error_student, date = [], []
        error_student.append("")
        error = False
        try:
            if 'yearOfEducation' and 'name_thai' and 'name_eng' and 'numberOfPeople' and 'adviser' and 'objective' and 'scope' and 'benefit' and 'reason' and 'priceOfMaterial' and 'priceOfOther' and 'credit' and 'course' and 'semesterEnd' and 'yearEnd' and 'startDate' and 'process1' and 'process2' and 'process3' and 'process4' and 'process5' and 'process6' and 'process7' and 'process8' and 'notation' in request.POST: #Check key in POST
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
                dateST = request.POST['startDate']
                process1 = request.POST['process1']
                process2 = request.POST['process2']
                process3 = request.POST['process3']
                process4 = request.POST['process4']
                process5 = request.POST['process5']
                process6 = request.POST['process6']
                process7 = request.POST['process7']
                process8 = request.POST['process8']
                note = request.POST['notation']
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
                if int(yearOE) > int(datetime.now().year + 543) or int(yearOE) < int(datetime.now().year + 535) or yearOE == "":
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If user_name is in use set error message and error to true
                    error = True
                if int(numOP) > 5 or int(numOP) < 1 or numOP == "":
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
                        float(priceOM) #Check price is float???
                    except ValueError:
                        error_priceOM = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
                        error = True
                if priceOO == "" : #Check age is empty???
                    error_priceOO = "*กรุณากรอกค่าใช้จ่ายเบ็ดเตล็ด" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        float(priceOO) #Check age is float???
                    except ValueError:
                        error_priceOO = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
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
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if 'studentID2' and 'studentNAME2' in request.POST:
                    studentID = request.POST['studentID2']
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if 'studentID3' and 'studentNAME3' in request.POST:
                    studentID = request.POST['studentID3']
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if 'studentID4' and 'studentNAME4' in request.POST:
                    studentID = request.POST['studentID4']
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if int(numOP) != len(s_list):
                    error = True
                if dateST == "":
                    error = True
                    error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                else:
                    date = dateST.split("-")
                    if len(date) != 3:
                        error = True
                        error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                if process1 == "":
                    error_process = "*กรุณาระบุขั้นตอนการดำเนินงาน อย่างน้อย 1 ขั้นตอน" #If empty set error message and error to true
                    error = True
                else:
                    for i in range(1,13):
                        if ('myCheck1/'+str(i)) in request.POST:
                            myCheck1.append(True)
                        else:
                            myCheck1.append(False)
                if process2 != "":
                    for i in range(1,13):
                        if ('myCheck2/'+str(i)) in request.POST:
                            myCheck2.append(True)
                        else:
                            myCheck2.append(False)
                if process3 != "":
                    for i in range(1,13):
                        if ('myCheck3/'+str(i)) in request.POST:
                            myCheck3.append(True)
                        else:
                            myCheck3.append(False)
                if process4 != "":
                    for i in range(1,13):
                        if ('myCheck4/'+str(i)) in request.POST:
                            myCheck4.append(True)
                        else:
                            myCheck4.append(False)
                if process5 != "":
                    for i in range(1,13):
                        if ('myCheck5/'+str(i)) in request.POST:
                            myCheck5.append(True)
                        else:
                            myCheck5.append(False)
                if process6 != "":
                    for i in range(1,13):
                        if ('myCheck6/'+str(i)) in request.POST:
                            myCheck6.append(True)
                        else:
                            myCheck6.append(False)
                if process7 != "":
                    for i in range(1,13):
                        if ('myCheck7/'+str(i)) in request.POST:
                            myCheck7.append(True)
                        else:
                            myCheck7.append(False)
                if process8 != "":
                    for i in range(1,13):
                        if ('myCheck8/'+str(i)) in request.POST:
                            myCheck8.append(True)
                        else:
                            myCheck8.append(False)
                myCheck.append(myCheck1)
                myCheck.append(myCheck2)
                myCheck.append(myCheck3)
                myCheck.append(myCheck4)
                myCheck.append(myCheck5)
                myCheck.append(myCheck6)
                myCheck.append(myCheck7)
                myCheck.append(myCheck8)
                process.append(process1)
                process.append(process2)
                process.append(process3)
                process.append(process4)
                process.append(process5)
                process.append(process6)
                process.append(process7)
                process.append(process8)
                if error == True: #Check if error is true raise exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            teachers = Teacher.objects.all()
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'error_yearOE': error_yearOE, 'error_nameTH': error_nameTH, 'error_nameEN': error_nameEN, 'error_numOP': error_numOP, 'error_adv': error_adv, 'error_obj': error_obj, 'error_scopes': error_scopes, 'error_benefits': error_benefits, 'error_reasons': error_reasons, 'error_priceOM': error_priceOM, 'error_priceOO': error_priceOO, 'error_credits': error_credits, 'error_courses': error_courses, 'error_semester': error_semester, 'error_yearEN': error_yearEN, 'error_student': error_student, 'nameTH': nameTH, 'nameEN': nameEN, 'obj': obj, 'scopes': scopes, 'benefits': benefits, 'reasons': reasons, 'priceOM': priceOM, 'priceOO': priceOO, 'credits': credits, 'courses': courses, 'semester': semester, 'yearEN': yearEN, 'student_list': s_list, 'numOP': numOP, 'yearOE': yearOE, 'edit': '1', 'error_dateST': error_dateST, 'startDate': dateST, 'error_process': error_process, 'note': note, 'process1': process1, 'checkList1': myCheck1, 'process2': process2, 'checkList2': myCheck2, 'process3': process3, 'checkList3': myCheck3, 'process4': process4, 'checkList4': myCheck4, 'process5': process5, 'checkList5': myCheck5, 'process6': process6, 'checkList6': myCheck6, 'process7': process7, 'checkList7': myCheck7, 'process8': process8, 'checkList8': myCheck8},)
        project = ProjectG6(teacher = Teacher.objects.get(id=int(adv)), name_thai = nameTH, name_eng = nameEN, yearOfEducation = yearOE, objective = obj, reason = reasons, scope = scopes, benefit = benefits)
        project.save()
        project.student = s_list
        research = ResearchProjectForm(project = project, numberOfPeople = numOP)
        research.save()
        offer = OfferProjectForm(project = project, priceOfMaterial = priceOM, priceOfOther = priceOO)
        offer.save()
        approve = ApproveProjectForm(project = project, student = s, course = courses, semesterEnd = semester, yearEnd = yearEN, credit = credits)
        approve.save()
        timeline = TimeLineForm(project = project, day = date[2], month = month[int(date[1])-1], year = int(date[0])+543, note = note)
        timeline.save()
        for i in range(8):
            if process[i] != '':
                step = StepInTimeLine(timeline = timeline, numberOfProcess = i+1, processDescription = process[i], month1 = myCheck[i][0], month2 = myCheck[i][1], month3 = myCheck[i][2], month4 = myCheck[i][3], month5 = myCheck[i][4], month6 = myCheck[i][5], month7 = myCheck[i][6], month8 = myCheck[i][7], month9 = myCheck[i][8], month10 = myCheck[i][9], month11 = myCheck[i][10], month12 = myCheck[i][11])
                step.save()
        messages.add_message(request, messages.INFO, "การสร้างฟอร์มของโปรเจคสำเร็จ")
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html')

def checkNotInList(storeList, item):
    for i in storeList:
        if i != "":
            if i.std_id == item:
                return False
    return True

def edit_3forms(request, pjID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '0':
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถแก้ไขฟอร์มได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            s = Student.objects.get(userprofile=u)
            p = ProjectG6.objects.get(id=pjID)
            for student in p.student.all():
                if student.std_id == s.std_id:
                    error = False
                    break
            if error == True:
                return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
            process, myCheck = [], []
            teachers = Teacher.objects.all()
            research = ResearchProjectForm.objects.get(project=p)
            offer = OfferProjectForm.objects.get(project=p)
            approve = ApproveProjectForm.objects.get(project=p)
            timeLine = TimeLineForm.objects.get(project=p)
            for i in range(8):
                pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1)
                if len(pro) == 0:
                    process.append("")
                    myCheck.append([])
                else:
                    process.append(pro[0].processDescription)
                    myCheck.append([pro[0].month1, pro[0].month2, pro[0].month3, pro[0].month4, pro[0].month5, pro[0].month6, pro[0].month7, pro[0].month8, pro[0].month9, pro[0].month10, pro[0].month11, pro[0].month12])
            startDate = str(timeLine.year-543)+'-'
            if month.index(timeLine.month.encode("utf-8"))+1 < 10:
                startDate += '0'+str(month.index(timeLine.month.encode("utf-8"))+1)+'-'
            else:
                startDate += str(month.index(timeLine.month.encode("utf-8"))+1)+'-'
            if timeLine.day < 10:
                startDate += '0'+str(timeLine.day)
            else:
                startDate += str(timeLine.day)
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'nameTH': p.name_thai, 'nameEN': p.name_eng, 'obj': p.objective, 'scopes': p.scope, 'benefits': p.benefit, 'reasons': p.reason, 'priceOM': offer.priceOfMaterial, 'priceOO': offer.priceOfOther, 'credits': approve.credit, 'courses': approve.course, 'semester': approve.semesterEnd, 'yearEN': approve.yearEnd, 'student_list': p.student.all(), 'numOP': research.numberOfPeople, 'yearOE': p.yearOfEducation, 'edit': '0', 'project_id': p.id, 'startDate': startDate, 'note': timeLine.note, 'process1': process[0], 'checkList1': myCheck[0], 'process2': process[1], 'checkList2': myCheck[1], 'process3': process[2], 'checkList3': myCheck[2], 'process4': process[3], 'checkList4': myCheck[3], 'process5': process[4], 'checkList5': myCheck[4], 'process6': process[5], 'checkList6': myCheck[5], 'process7': process[6], 'checkList7': myCheck[6], 'process8': process[7], 'checkList8': myCheck[7]},)
    else:
        return render(request, 'base.html')

def edit_3forms_update(request, pjID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '0':
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถแก้ไขฟอร์มได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        s = Student.objects.get(userprofile=u)
        p = ProjectG6.objects.get(id=pjID)
        s_list, myCheck, process, myCheck1, myCheck2, myCheck3, myCheck4, myCheck5, myCheck6, myCheck7, myCheck8 = [], [], [], [], [], [], [], [], [], [], []
        s_list.append(s)
        yearOE, nameTH, nameEN, numOP, adv, obj, scopes, benefits, reasons, priceOM, priceOO, credits, courses, semester, yearEN, dateST, process1, process2, process3, process4, process5, process6, process7, process8, note = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        error_yearOE, error_nameTH, error_nameEN, error_numOP, error_adv, error_obj, error_scopes, error_benefits, error_reasons, error_priceOM, error_priceOO, error_credits, error_courses, error_semester, error_yearEN, error_process, error_dateST = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        error_student, date = [], []
        error_student.append("")
        error = False
        try:
            if 'yearOfEducation' and 'name_thai' and 'name_eng' and 'numberOfPeople' and 'adviser' and 'objective' and 'scope' and 'benefit' and 'reason' and 'priceOfMaterial' and 'priceOfOther' and 'credit' and 'course' and 'semesterEnd' and 'yearEnd' and 'startDate' and 'process1' and 'process2' and 'process3' and 'process4' and 'process5' and 'process6' and 'process7' and 'process8' and 'notation' in request.POST: #Check key in POST
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
                dateST = request.POST['startDate']
                process1 = request.POST['process1']
                process2 = request.POST['process2']
                process3 = request.POST['process3']
                process4 = request.POST['process4']
                process5 = request.POST['process5']
                process6 = request.POST['process6']
                process7 = request.POST['process7']
                process8 = request.POST['process8']
                note = request.POST['notation']
                if nameTH == "" : #Check user_name is empty???
                    error_nameTH = "*กรุณาใส่ชื่อโครงงาน (ภาษาไทย)" #If empty set error message and error to true
                    error = True
                elif len(ProjectG6.objects.filter(name_thai=nameTH)) != 0 and p.name_thai != nameTH:
                    error_nameTH = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาไทย)" #If user_name is in use set error message and error to true
                    error = True
                if nameEN == "" : #Check name is empty???
                    error_nameEN = "*กรุณาใส่ชื่อโครงงาน (ภาษาอังกฤษ)" #If empty set error message and error to true
                    error = True
                elif len(ProjectG6.objects.filter(name_eng=nameEN)) != 0 and p.name_eng != nameEN:
                    error_nameEN = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาไทย)" #If user_name is in use set error message and error to true
                    error = True
                if len(Teacher.objects.filter(id=int(adv))) == 0:
                    error_adv = "*กรุณาเลือกที่ปรึกษาใหม่" #If user_name is in use set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 543) or int(yearOE) < int(datetime.now().year + 535) or yearOE == "":
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If user_name is in use set error message and error to true
                    error = True
                if int(numOP) > 5 or int(numOP) < 1 or numOP == "":
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
                        float(priceOM) #Check price is float???
                    except ValueError:
                        error_priceOM = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
                        error = True
                if priceOO == "" : #Check age is empty???
                    error_priceOO = "*กรุณากรอกค่าใช้จ่ายเบ็ดเตล็ด" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        float(priceOO) #Check age is float???
                    except ValueError:
                        error_priceOO = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
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
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if 'studentID2' and 'studentNAME2' in request.POST:
                    studentID = request.POST['studentID2']
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if 'studentID3' and 'studentNAME3' in request.POST:
                    studentID = request.POST['studentID3']
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if 'studentID4' and 'studentNAME4' in request.POST:
                    studentID = request.POST['studentID4']
                    no_add = checkNotInList(s_list, studentID)
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add:
                        s_list.append(Student.objects.get(std_id=studentID))
                        error_student.append("")
                    else:
                        s_list.append("")
                        if no_add:
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True
                if int(numOP) != len(s_list):
                    error == True
                if dateST == "":
                    error = True
                    error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                else:
                    date = dateST.split("-")
                    if len(date) != 3:
                        error = True
                        error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                if process1 == "":
                    error_process = "*กรุณาระบุขั้นตอนการดำเนินงาน อย่างน้อย 1 ขั้นตอน" #If empty set error message and error to true
                    error = True
                else:
                    for i in range(1,13):
                        if ('myCheck1/'+str(i)) in request.POST:
                            myCheck1.append(True)
                        else:
                            myCheck1.append(False)
                if process2 != "":
                    for i in range(1,13):
                        if ('myCheck2/'+str(i)) in request.POST:
                            myCheck2.append(True)
                        else:
                            myCheck2.append(False)
                if process3 != "":
                    for i in range(1,13):
                        if ('myCheck3/'+str(i)) in request.POST:
                            myCheck3.append(True)
                        else:
                            myCheck3.append(False)
                if process4 != "":
                    for i in range(1,13):
                        if ('myCheck4/'+str(i)) in request.POST:
                            myCheck4.append(True)
                        else:
                            myCheck4.append(False)
                if process5 != "":
                    for i in range(1,13):
                        if ('myCheck5/'+str(i)) in request.POST:
                            myCheck5.append(True)
                        else:
                            myCheck5.append(False)
                if process6 != "":
                    for i in range(1,13):
                        if ('myCheck6/'+str(i)) in request.POST:
                            myCheck6.append(True)
                        else:
                            myCheck6.append(False)
                if process7 != "":
                    for i in range(1,13):
                        if ('myCheck7/'+str(i)) in request.POST:
                            myCheck7.append(True)
                        else:
                            myCheck7.append(False)
                if process8 != "":
                    for i in range(1,13):
                        if ('myCheck8/'+str(i)) in request.POST:
                            myCheck8.append(True)
                        else:
                            myCheck8.append(False)
                myCheck.append(myCheck1)
                myCheck.append(myCheck2)
                myCheck.append(myCheck3)
                myCheck.append(myCheck4)
                myCheck.append(myCheck5)
                myCheck.append(myCheck6)
                myCheck.append(myCheck7)
                myCheck.append(myCheck8)
                process.append(process1)
                process.append(process2)
                process.append(process3)
                process.append(process4)
                process.append(process5)
                process.append(process6)
                process.append(process7)
                process.append(process8)
                if error == True: #Check if error is true raise exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            teachers = Teacher.objects.all()
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'error_yearOE': error_yearOE, 'error_nameTH': error_nameTH, 'error_nameEN': error_nameEN, 'error_numOP': error_numOP, 'error_adv': error_adv, 'error_obj': error_obj, 'error_scopes': error_scopes, 'error_benefits': error_benefits, 'error_reasons': error_reasons, 'error_priceOM': error_priceOM, 'error_priceOO': error_priceOO, 'error_credits': error_credits, 'error_courses': error_courses, 'error_semester': error_semester, 'error_yearEN': error_yearEN, 'error_student': error_student, 'nameTH': nameTH, 'nameEN': nameEN, 'obj': obj, 'scopes': scopes, 'benefits': benefits, 'reasons': reasons, 'priceOM': priceOM, 'priceOO': priceOO, 'credits': credits, 'courses': courses, 'semester': semester, 'yearEN': yearEN, 'student_list': s_list, 'numOP': numOP, 'yearOE': yearOE, 'edit': '0', 'project_id': p.id, 'error_yearST': error_yearST, 'error_dateST': error_dateST, 'error_monthST': error_monthST, 'dateST': dateST, 'monthST': monthST, 'yearST': yearST, 'error_process': error_process, 'note': note, 'process1': process1, 'checkList1': myCheck1, 'process2': process2, 'checkList2': myCheck2, 'process3': process3, 'checkList3': myCheck3, 'process4': process4, 'checkList4': myCheck4, 'process5': process5, 'checkList5': myCheck5, 'process6': process6, 'checkList6': myCheck6, 'process7': process7, 'checkList7': myCheck7, 'process8': process8, 'checkList8': myCheck8},)
        p.teacher = Teacher.objects.get(id=int(adv))
        p.name_thai = nameTH
        p.name_eng = nameEN
        p.yearOfEducation = yearOE
        p.objective = obj
        p.reason = reasons
        p.scope = scopes
        p.benefit = benefits
        p.student = s_list
        p.save()
        research = ResearchProjectForm.objects.get(project=p)
        research.numberOfPeople = numOP
        research.save()
        offer = OfferProjectForm.objects.get(project=p)
        offer.priceOfMaterial = priceOM
        offer.priceOfOther = priceOO
        offer.save()
        approve = ApproveProjectForm.objects.get(project=p)
        approve.student = s
        approve.course = courses
        approve.semesterEnd = semester
        approve.yearEnd = yearEN
        approve.credit = credits
        approve.save()
        timeline = TimeLineForm.objects.get(project=p)
        timeline.day = date[2]
        timeline.month = month[int(date[1])-1]
        timeline.year = int(date[0])+543
        timeline.note = note
        timeline.save()
        for i in range(8):
            step_list = StepInTimeLine.objects.filter(timeline=timeline, numberOfProcess=i+1)
            if process[i] != '':
                if len(step_list) == 0:
                    step = StepInTimeLine(timeline = timeline, numberOfProcess = i+1, processDescription = process[i], month1 = myCheck[i][0], month2 = myCheck[i][1], month3 = myCheck[i][2], month4 = myCheck[i][3], month5 = myCheck[i][4], month6 = myCheck[i][5], month7 = myCheck[i][6], month8 = myCheck[i][7], month9 = myCheck[i][8], month10 = myCheck[i][9], month11 = myCheck[i][10], month12 = myCheck[i][11])
                    step.save()
                else:
                    step_list[0].processDescription = process[i]
                    step_list[0].month1 = myCheck[i][0]
                    step_list[0].month2 = myCheck[i][1]
                    step_list[0].month3 = myCheck[i][2]
                    step_list[0].month4 = myCheck[i][3]
                    step_list[0].month5 = myCheck[i][4]
                    step_list[0].month6 = myCheck[i][5]
                    step_list[0].month7 = myCheck[i][6]
                    step_list[0].month8 = myCheck[i][7]
                    step_list[0].month9 = myCheck[i][8]
                    step_list[0].month10 = myCheck[i][9]
                    step_list[0].month11 = myCheck[i][10]
                    step_list[0].month12 = myCheck[i][11]
                    step_list[0].save()
            else:
                if len(step_list) == 1:
                    step_list[0].delete()
        messages.add_message(request, messages.INFO, "การแก้ไขฟอร์มของโปรเจคสำเร็จ")
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html')

def approveProject(request, apID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        approve = ApproveProjectForm.objects.get(id=apID)
        if u.type == '0':
            s = Student.objects.get(userprofile=u)
            year = int(datetime.now().year - 2000 + 43) - int(s.std_id[:2])
            return render(request, 'group6/approveProject_view.html', {'approve': approve, 'scheme': scheme[int(s.scheme)], 'department': department[int(s.userprofile.department)], 'main': main[int(s.main)], 'currentYear': year, 'student': s},)
        else:
            year = int(datetime.now().year - 2000 + 43) - int(approve.student.std_id[:2])
            return render(request, 'group6/approveProject_view.html', {'approve': approve, 'scheme': scheme[int(approve.student.scheme)], 'department': department[int(approve.student.userprofile.department)], 'main': main[int(approve.student.main)], 'currentYear': year},)
    else:
        return render(request, 'base.html')

def offerProject(request, opID):
    if request.user.is_authenticated():
        offer = OfferProjectForm.objects.get(id=opID)
        sumofprice = offer.priceOfMaterial + offer.priceOfOther
        return render(request, 'group6/offerProject_view.html', {'offer': offer, 'priceOfTotal': sumofprice},)
    else:
        return render(request, 'base.html')

def researchProject(request, rpID):
    if request.user.is_authenticated():
        research = ResearchProjectForm.objects.get(id=rpID)
        return render(request, 'group6/researchProject_view.html', {'research': research},)
    else:
        return render(request, 'base.html')

def timeLineProject(request, tlID):
    if request.user.is_authenticated():
        timeLine = TimeLineForm.objects.get(id=tlID)
        processList = []
        for i in range(8):
            pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1)
            if len(pro) == 0:
                processList.append([])
            else:
                processList.append(pro[0])
        return render(request, 'group6/timeLineProject_view.html', {'timeLine': timeLine, 'processList': processList},)
    else:
        return render(request, 'base.html')

def deleteForm(request, pjID):
    if request.user.is_authenticated():
        error = True
        u = UserProfile.objects.get(user=request.user)
        s = Student.objects.get(userprofile=u)
        p = ProjectG6.objects.get(id=pjID)
        for student in p.student.all():
            if student.std_id == s.std_id:
                error = False
                break
        if error == True:
            messages.add_message(request, messages.INFO, "นักศึกษาในกลุ่มเท่านั้นที่สามารถลบฟอร์มได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        p.delete()
        messages.add_message(request, messages.INFO, "การลบฟอร์มของโปรเจคสำเร็จ")
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html')

def approveProjectPrint(request, apID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        approve = ApproveProjectForm.objects.get(id=apID)
        if u.type == '0':
            s = Student.objects.get(userprofile=u)
            year = int(datetime.now().year - 2000 + 43) - int(s.std_id[:2])
            return render(request, 'group6/approveProject_view_print.html', {'approve': approve, 'scheme': scheme[int(s.scheme)], 'department': department[int(s.userprofile.department)], 'main': main[int(s.main)], 'currentYear': year, 'student': s},)
        else:
            year = int(datetime.now().year - 2000 + 43) - int(approve.student.std_id[:2])
            return render(request, 'group6/approveProject_view_print.html', {'approve': approve, 'scheme': scheme[int(approve.student.scheme)], 'department': department[int(approve.student.userprofile.department)], 'main': main[int(approve.student.main)], 'currentYear': year},)
    else:
        return render(request, 'base.html')

def offerProjectPrint(request, opID):
    if request.user.is_authenticated():
        offer = OfferProjectForm.objects.get(id=opID)
        sumofprice = offer.priceOfMaterial + offer.priceOfOther
        return render(request, 'group6/offerProject_view_print.html', {'offer': offer, 'priceOfTotal': sumofprice},)
    else:
        return render(request, 'base.html')

def researchProjectPrint(request, rpID):
    if request.user.is_authenticated():
        research = ResearchProjectForm.objects.get(id=rpID)
        return render(request, 'group6/researchProject_view_print.html', {'research': research},)
    else:
        return render(request, 'base.html')

def timeLineProjectPrint(request, tlID):
    if request.user.is_authenticated():
        timeLine = TimeLineForm.objects.get(id=tlID)
        processList = []
        for i in range(8):
            pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1)
            if len(pro) == 0:
                processList.append([])
            else:
                processList.append(pro[0])
        return render(request, 'group6/timeLineProject_view_print.html', {'timeLine': timeLine, 'processList': processList},)
    else:
        return render(request, 'base.html')

def timeLineProjectPrintCheck(request, tlID):
    if request.user.is_authenticated():
        timeLine = TimeLineForm.objects.get(id=tlID)
        processList = []
        for i in range(8):
            pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1)
            if len(pro) == 0:
                processList.append([])
            else:
                processList.append(pro[0])
        return render(request, 'group6/timeLineProject_view_print_check.html', {'timeLine': timeLine, 'processList': processList},)
    else:
        return render(request, 'base.html')

def add_categories_tester(request, pjID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '2':
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถกำหนด Categories กับอาจารย์สอบโปรเจคได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            p = ProjectG6.objects.get(id=pjID)
            if len(CategoriesProject.objects.filter(project=p)) != 0:
                messages.add_message(request, messages.INFO, "โครงงานนี้ได้กำหนด Categories กับอาจารย์สอบโปรเจคแล้ว")
                return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
            teachers = Teacher.objects.all()
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '1', 'teacher_project': p.teacher, 'project_id': p.id, 'teachers': teachers, 'numOT': '1', 'yearOE': int(datetime.now().year + 43 - 2000), 'projNum':"01", 'main':'Cpr.E', 'semester':'1',})
    else:
        return render(request, 'base.html')

def checkNotInListTeacher(storeList, item):
    for t in storeList:
        if t != "":
            if t.id == int(item):
                return False
    return True

def add_categories_tester_add(request, pjID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '2':
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถกำหนด Categories กับอาจารย์สอบโปรเจคได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        p = ProjectG6.objects.get(id=pjID)
        if len(CategoriesProject.objects.filter(project=p)) != 0:
            messages.add_message(request, messages.INFO, "โครงงานนี้ได้กำหนด Categories กับอาจารย์สอบโปรเจคแล้ว")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        t_list = []
        t_list.append(p.teacher)
        yearOE, numOT, projNum, main, semester = "", "", "", "", ""
        error_yearOE, error_numOT, error_projNum, error_main, error_semester = "", "", "", "", ""
        error_teacher = []
        error_teacher.append("")
        error = False
        try:
            if 'numberOfTester' and 'projectOfMain' and 'yearOfEducation' and 'semesterNum' and 'projectNum' in request.POST: #Check key in POST
                yearOE = request.POST['yearOfEducation'] #Get Value from key
                numOT = request.POST['numberOfTester']
                projNum = request.POST['projectNum']
                main = request.POST['projectOfMain']
                semester = request.POST['semesterNum']
                if main == "" : #Check user_name is empty???
                    error_main = "*กรุณาเลือกกลุ่มสาขาใหม่" #If empty set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 43 - 2000) or int(yearOE) < int(datetime.now().year + 35 - 2000) or yearOE == "":
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If user_name is in use set error message and error to true
                    error = True
                if int(projNum) > 35 or int(projNum) < 1 or projNum == "" : #Check name is empty???
                    error_projNum = "*กรุณาเลือกเลขโครงงานใหม่" #If empty set error message and error to true
                    error = True
                if int(semester) > 2 or int(semester)<1:
                    error_semester = "*กรุณาเลือกภาคเรียนใหม่"
                    error = True
                if len(CategoriesProject.objects.filter(number=projNum, project_catagories=main, year=yearOE, semester=semester)) != 0 and error == False:
                    error_projNum = "*เลขโครงงานนี้ถูกใช้ไปแล้ว" #If empty set error message and error to true
                    error = True
                if int(numOT) > 5 or int(numOT) < 1 or numOT == "":
                    error_numOT = "*กรุณาเลือกจำนวนคนใหม่" #If user_name is in use set error message and error to true
                    error = True
                if 'testerNAME1' in request.POST:
                    testerNAMEID = request.POST['testerNAME1']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if 'testerNAME2' in request.POST:
                    testerNAMEID = request.POST['testerNAME2']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if 'testerNAME3' in request.POST:
                    testerNAMEID = request.POST['testerNAME3']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if 'testerNAME4' in request.POST:
                    testerNAMEID = request.POST['testerNAME4']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if int(numOT) != len(t_list):
                    error = True
                if error == True: #Check if error is true raise exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            teachers = Teacher.objects.all()
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '1', 'teacher_project': p.teacher, 'project_id': p.id, 'error_yearOE': error_yearOE, 'error_teacher': error_teacher, 'error_numOT': error_numOT, 'error_projNum': error_projNum, 'error_main': error_main, 'error_semester': error_semester, 'teacher_list': t_list, 'numOT': numOT, 'yearOE': yearOE, 'projNum':projNum, 'main':main, 'semester':semester, 'teachers':teachers},)
        cp = CategoriesProject(project=p, project_catagories=main, number=projNum, year=yearOE, semester=semester)
        cp.save()
        cp.teacher = t_list
        messages.add_message(request, messages.INFO, "การกำหนด Categories กับอาจารย์สอบโปรเจคสำเร็จ")
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html')

def edit_categories_tester(request, cpID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '2':
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถแก้ไข Categories กับอาจารย์สอบโปรเจคได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            cp = CategoriesProject.objects.get(id=cpID)
            teachers = Teacher.objects.all()
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '0', 'teacher_project': cp.project.teacher, 'project_id': cp.project.id, 'teachers': teachers, 'numOT': len(cp.teacher.all()), 'yearOE': cp.year, 'projNum': cp.number, 'main': cp.project_catagories, 'semester': cp.semester, 'teacher_list': cp.teacher.all(), 'categories_id': cp.id})
    else:
        return render(request, 'base.html')

def edit_categories_tester_update(request, cpID):
    if request.user.is_authenticated():
        u = UserProfile.objects.get(user=request.user)
        if u.type != '2':
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถแก้ไข Categories กับอาจารย์สอบโปรเจคได้")
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        cp = CategoriesProject.objects.get(id=cpID)
        t_list = []
        t_list.append(cp.project.teacher)
        yearOE, numOT, projNum, main, semester = "", "", "", "", ""
        error_yearOE, error_numOT, error_projNum, error_main, error_semester = "", "", "", "", ""
        error_teacher = []
        error_teacher.append("")
        error = False
        try:
            if 'numberOfTester' and 'projectOfMain' and 'yearOfEducation' and 'semesterNum' and 'projectNum' in request.POST: #Check key in POST
                yearOE = request.POST['yearOfEducation'] #Get Value from key
                numOT = request.POST['numberOfTester']
                projNum = request.POST['projectNum']
                main = request.POST['projectOfMain']
                semester = request.POST['semesterNum']
                if main == "" : #Check user_name is empty???
                    error_main = "*กรุณาเลือกกลุ่มสาขาใหม่" #If empty set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 43 - 2000) or int(yearOE) < int(datetime.now().year + 35 - 2000) or yearOE == "":
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If user_name is in use set error message and error to true
                    error = True
                if int(projNum) > 35 or int(projNum) < 1 or projNum == "" : #Check name is empty???
                    error_projNum = "*กรุณาเลือกเลขโครงงานใหม่" #If empty set error message and error to true
                    error = True
                if int(semester) > 2 or int(semester)<1:
                    error_semester = "*กรุณาเลือกภาคเรียนใหม่"
                    error = True
                if cp.number != projNum or cp.project_catagories != main or cp.year != yearOE or cp.semester != int(semester):
                    if len(CategoriesProject.objects.filter(number=projNum, project_catagories=main, year=yearOE, semester=semester)) != 0 and error == False:
                        error_projNum = "*เลขโครงงานนี้ถูกใช้ไปแล้ว" #If empty set error message and error to true
                        error = True
                if int(numOT) > 5 or int(numOT) < 1 or numOT == "":
                    error_numOT = "*กรุณาเลือกจำนวนคนใหม่" #If user_name is in use set error message and error to true
                    error = True
                if 'testerNAME1' in request.POST:
                    testerNAMEID = request.POST['testerNAME1']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if 'testerNAME2' in request.POST:
                    testerNAMEID = request.POST['testerNAME2']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if 'testerNAME3' in request.POST:
                    testerNAMEID = request.POST['testerNAME3']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if 'testerNAME4' in request.POST:
                    testerNAMEID = request.POST['testerNAME4']
                    no_add = checkNotInListTeacher(t_list, testerNAMEID)
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add:
                        t_list.append(Teacher.objects.get(id=testerNAMEID))
                        error_teacher.append("")
                    else:
                        t_list.append("")
                        if no_add:
                            error_teacher.append("*ไม่พบอาจารย์")
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว"))
                        error = True
                if int(numOT) != len(t_list):
                    error = True
                if error == True: #Check if error is true raise exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            teachers = Teacher.objects.all()
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '0', 'teacher_project': cp.project.teacher, 'project_id': cp.project.id, 'error_yearOE': error_yearOE, 'error_teacher': error_teacher, 'error_numOT': error_numOT, 'error_projNum': error_projNum, 'error_main': error_main, 'error_semester': error_semester, 'teacher_list': t_list, 'numOT': numOT, 'yearOE': yearOE, 'projNum':projNum, 'main':main, 'semester':semester, 'teachers':teachers, 'categories_id': cp.id},)
        cp.teacher = t_list
        cp.semester = int(semester)
        cp.project_catagories = main
        cp.number = projNum
        cp.year = yearOE
        cp.save()
        messages.add_message(request, messages.INFO, "การแก้ไข Categories กับอาจารย์สอบโปรเจคสำเร็จ")
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html')
