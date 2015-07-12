#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group6.models import *
from login.models import *
from datetime import datetime

#Global variable for match data
month = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
department = ['','วิศวกรรมไฟฟ้าและคอมพิวเตอร์']
faculty = ['','วิศวกรรมศาสตร์']
scheme = ['ปรับปรุง Cpr.E 54','ปรับปรุง EE 51','ปรับปรุง ECE 55']
main = ['Cpr.E','G','U','C','EP']
main_cat = ['Cp','G','U','C','EP']

#function for render page index of this app url project_docs_index
def index(request):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type == '0': #check user type is student
            s = Student.objects.get(userprofile=u) #get Student data
            project = s.projectg6_set.all() #get all project by this student
            research = [] #create empty list to store research form from all project
            offer = [] #create empty list to store offer form from all project
            approve = [] #create empty list to store approve form from all project
            timeLine = [] #create empty list to store timeline form from all project
            project_id = [] #create empty list to store project id (number of project, year, semester, main) from all project
            notification = [] #create empty list to notification id from all project
            for p in project: #for loop to all project
                research.append(ResearchProjectForm.objects.get(project=p)) #find research data by project and add to list
                offer.append(OfferProjectForm.objects.get(project=p)) #find offer data by project and add to list
                approve.append(ApproveProjectForm.objects.get(project=p)) #find approve data by project and add to list
                timeLine.append(TimeLineForm.objects.get(project=p)) #find timeline data by project and add to list
                categories_temp = CategoriesProject.objects.filter(project=p) #find categories data by project
                noti_temp = NotificationProject.objects.filter(project=p) #find notification data by project
                if len(noti_temp)==0: #check noti_temp
                    notification.append('') #if don't have add empty string to list
                else:
                    notification.append(noti_temp) #if have add notification to list
                if len(categories_temp)==0: #check categories_temp
                    project_id.append('-') #if don't have add '-' to list
                else:
                    project_id.append(categories_temp[0].project_catagories+categories_temp[0].year+'-'+str(categories_temp[0].semester)+'-'+categories_temp[0].number) #if have add project id to list
            return render(request, 'group6/index.html', {'project_list': project, 'research': research, 'offer': offer, 'approve': approve, 'timeLine': timeLine, 'project_id': project_id, 'message': notification},) #render template with all data
        elif u.type == '1': #check user type is teacher
            t = Teacher.objects.get(userprofile=u) #get current teacher from user
            project_list, research_list, offer_list, approve_list, timeLine_list, categories_id_list, project_id_list, notification_list = [], [], [], [], [], [], [], [] #create list to store data for render
            for cat in main_cat: #for loop to all categories
                cp = CategoriesProject.objects.filter(project_catagories=cat) #filter categories project by categories name
                project = [] #create empty list to store project in each categories
                research = [] #create empty list to store research form from all project in each categories
                offer = [] #create empty list to store offer form from all project in each categories
                approve = [] #create empty list to store approve form from all project in each categories
                timeLine = [] #create empty list to store timeline form from all project in each categories
                categories_id = [] #create empty list to store categories project id in each project
                project_id = [] #create empty list to store project id (number of project, year, semester, main) from all project in each categories
                notification = [] #create empty list to notification id from all project in rach categories
                for pro in cp: #for loop to all project in each categories
                    if pro.project.teacher == t: #check project adviser is current teacher
                        project.append(pro.project) #add to project list
                        continue #skip to next for loop
                    for teach in pro.teacher.all(): #for loop to list all tester of project 
                        if teach == t: #check current teacher is one of tester
                            project.append(pro.project) #add to project list
                for p in project: #for loop to all project that teacher are adviser and tester
                    research.append(ResearchProjectForm.objects.get(project=p)) #find research data by project and add to list
                    offer.append(OfferProjectForm.objects.get(project=p)) #find offer data by project and add to list
                    approve.append(ApproveProjectForm.objects.get(project=p)) #find approve data by project and add to list
                    timeLine.append(TimeLineForm.objects.get(project=p)) #find timeline data by project and add to list
                    categories_temp = CategoriesProject.objects.filter(project=p) #find categories data by project
                    noti_temp = NotificationProject.objects.filter(project=p) #find notification data by project
                    if len(categories_temp)==0: #check categories_temp
                        categories_id.append('') #if don't have add '' to list
                        project_id.append('-') #if don't have add '-' to list
                    else:
                        categories_id.append(categories_temp[0].id) #if have add categories project id to list
                        project_id.append(categories_temp[0].project_catagories+categories_temp[0].year+'-'+str(categories_temp[0].semester)+'-'+categories_temp[0].number) #if have add project id to list
                    if len(noti_temp)==0: #check noti_temp
                        notification.append('') #if don't have add empty string to list
                    else:
                        notification.append(noti_temp) #if have add notification to list
                project_list.append(project) #add project list to all categories project
                research_list.append(research) #add research list to all categories project
                offer_list.append(offer) #add offer list to all categories project
                approve_list.append(approve) #add approve list to all categories project
                timeLine_list.append(timeLine) #add timeline list to all categories project
                categories_id_list.append(categories_id) #add categories id list to all categories project
                project_id_list.append(project_id) #add project id list to all categories project
                notification_list.append(notification) #add notification list to all categories project
            project = [] #create empty list to store project in uncategories
            research = [] #create empty list to store research form from all project in uncategories
            offer = [] #create empty list to store offer form from all project in uncategories
            approve = [] #create empty list to store approve form from all project in uncategories
            timeLine = [] #create empty list to store timeline form from all project in uncategories
            categories_id = [] #create empty list to store categories project id in each project uncategories
            project_id = [] #create empty list to store project id (number of project, year, semester, main) from all project in uncategories
            notification = [] #create empty list to notification id from all project in uncategories
            for proj in ProjectG6.objects.all():  #for loop to all project in uncategories
                if proj.teacher == t: #check teacher adviser for this project
                    if len(proj.categoriesproject_set.all()) == 0: #check project uncategories
                        project.append(proj) #add to project list
                        research.append(ResearchProjectForm.objects.get(project=proj)) #find research data by project and add to list
                        offer.append(OfferProjectForm.objects.get(project=proj)) #find offer data by project and add to list
                        approve.append(ApproveProjectForm.objects.get(project=proj)) #find approve data by project and add to list
                        timeLine.append(TimeLineForm.objects.get(project=proj)) #find timeline data by project and add to list
                        categories_temp = CategoriesProject.objects.filter(project=proj) #find categories data by project
                        noti_temp = NotificationProject.objects.filter(project=proj) #find notification data by project
                        if len(categories_temp)==0: #check categories_temp
                            categories_id.append('') #if don't have add '' to list
                            project_id.append('-') #if don't have add '-' to list
                        else:
                            categories_id.append(categories_temp[0].id) #if have add categories project id to list
                            project_id.append(categories_temp[0].project_catagories+categories_temp[0].year+'-'+str(categories_temp[0].semester)+'-'+categories_temp[0].number) #if have add project id to list
                        if len(noti_temp)==0: #check noti_temp
                            notification.append('') #if don't have add empty string to list
                        else:
                            notification.append(noti_temp) #if have add notification to list
            project_list.append(project) #add project list to all categories project
            research_list.append(research) #add research list to all categories project
            offer_list.append(offer) #add offer list to all categories project
            approve_list.append(approve) #add approve list to all categories project
            timeLine_list.append(timeLine) #add timeline list to all categories project
            categories_id_list.append(categories_id) #add categories id list to all categories project
            project_id_list.append(project_id) #add project id list to all categories project
            notification_list.append(notification) #add notification list to all categories project
            return render(request, 'group6/index_teacher.html', {'main0': main[0], 'project_list0': project_list[0], 'research0': research_list[0], 'offer0': offer_list[0], 'approve0': approve_list[0], 'timeLine0': timeLine_list[0], 'categories_id0':categories_id_list[0], 'project_id0': project_id_list[0], 'message0': notification_list[0], 'main1': main[1], 'project_list1': project_list[1], 'research1': research_list[1], 'offer1': offer_list[1], 'approve1': approve_list[1], 'timeLine1': timeLine_list[1], 'categories_id1':categories_id_list[1], 'project_id1': project_id_list[1], 'message1': notification_list[1], 'main2': main[2], 'project_list2': project_list[2], 'research2': research_list[2], 'offer2': offer_list[2], 'approve2': approve_list[2], 'timeLine2': timeLine_list[2], 'categories_id2':categories_id_list[2], 'project_id2': project_id_list[2], 'message2': notification_list[2], 'main3': main[3], 'project_list3': project_list[3], 'research3': research_list[3], 'offer3': offer_list[3], 'approve3': approve_list[3], 'timeLine3': timeLine_list[3], 'categories_id3':categories_id_list[3], 'project_id3': project_id_list[3], 'message3': notification_list[3], 'main4': main[4], 'project_list4': project_list[4], 'research4': research_list[4], 'offer4': offer_list[4], 'approve4': approve_list[4], 'timeLine4': timeLine_list[4], 'categories_id4':categories_id_list[4], 'project_id4': project_id_list[4], 'message4': notification_list[4], 'main5': 'Uncategories', 'project_list5': project_list[5], 'research5': research_list[5], 'offer5': offer_list[5], 'approve5': approve_list[5], 'timeLine5': timeLine_list[5], 'categories_id5':categories_id_list[5], 'project_id5': project_id_list[5], 'message5': notification_list[5]}) #render template with all data
        elif u.type == '2': #check user type is officer
            project_list, research_list, offer_list, approve_list, timeLine_list, categories_id_list, project_id_list, notification_list = [], [], [], [], [], [], [], [] #create list to store data for render
            for cat in main_cat: #for loop to all categories
                cp = CategoriesProject.objects.filter(project_catagories=cat) #filter categories project by categories name
                project = [] #create empty list to store project in each categories
                research = [] #create empty list to store research form from all project in each categories
                offer = [] #create empty list to store offer form from all project in each categories
                approve = [] #create empty list to store approve form from all project in each categories
                timeLine = [] #create empty list to store timeline form from all project in each categories
                categories_id = [] #create empty list to store categories project id in each project
                project_id = [] #create empty list to store project id (number of project, year, semester, main) from all project in each categories
                notification = [] #create empty list to notification id from all project in each categories
                for pro in cp: #for loop to all project in each categories
                    project.append(pro.project) #add project from categories to project list
                for p in project: #for loop to all project
                    research.append(ResearchProjectForm.objects.get(project=p)) #find research data by project and add to list
                    offer.append(OfferProjectForm.objects.get(project=p)) #find offer data by project and add to list
                    approve.append(ApproveProjectForm.objects.get(project=p)) #find approve data by project and add to list
                    timeLine.append(TimeLineForm.objects.get(project=p)) #find timeline data by project and add to list
                    categories_temp = CategoriesProject.objects.filter(project=p) #find categories data by project
                    noti_temp = NotificationProject.objects.filter(project=p) #find notification data by project
                    if len(categories_temp)==0: #check categories_temp
                        categories_id.append('') #if don't have add '' to list
                        project_id.append('-') #if don't have add '-' to list
                    else:
                        categories_id.append(categories_temp[0].id) #if have add categories project id to list
                        project_id.append(categories_temp[0].project_catagories+categories_temp[0].year+'-'+str(categories_temp[0].semester)+'-'+categories_temp[0].number) #if have add project id to list
                    if len(noti_temp)==0: #check noti_temp
                        notification.append('') #if don't have add empty string to list
                    else:
                        notification.append(noti_temp) #if have add notification to list
                project_list.append(project) #add project list to all categories project
                research_list.append(research) #add research list to all categories project
                offer_list.append(offer) #add offer list to all categories project
                approve_list.append(approve) #add approve list to all categories project
                timeLine_list.append(timeLine) #add timeline list to all categories project
                categories_id_list.append(categories_id) #add categories id list to all categories project
                project_id_list.append(project_id) #add project id list to all categories project
                notification_list.append(notification) #add notification list to all categories project
            project = [] #create empty list to store project in each categories
            research = [] #create empty list to store research form from all project in uncategories
            offer = [] #create empty list to store offer form from all project in uncategories
            approve = [] #create empty list to store approve form from all project in uncategories
            timeLine = [] #create empty list to store timeline form from all project in uncategories
            categories_id = [] #create empty list to store categories project id in each project
            project_id = [] #create empty list to store project id (number of project, year, semester, main) from all project in uncategories
            notification = [] #create empty list to notification id from all project in uncategories
            for proj in ProjectG6.objects.all(): #for loop to all project in uncategories
                if len(proj.categoriesproject_set.all()) == 0: #check project uncategories
                    project.append(proj) #add to project list
                    research.append(ResearchProjectForm.objects.get(project=proj)) #find research data by project and add to list
                    offer.append(OfferProjectForm.objects.get(project=proj)) #find offer data by project and add to list
                    approve.append(ApproveProjectForm.objects.get(project=proj)) #find approve data by project and add to list
                    timeLine.append(TimeLineForm.objects.get(project=proj)) #find timeline data by project and add to list
                    categories_temp = CategoriesProject.objects.filter(project=proj) #find categories data by project
                    noti_temp = NotificationProject.objects.filter(project=proj) #find notification data by project
                    if len(categories_temp)==0: #check categories_temp
                        categories_id.append('') #if don't have add '' to list
                        project_id.append('-') #if don't have add '-' to list
                    else:
                        categories_id.append(categories_temp[0].id) #if have add categories project id to list
                        project_id.append(categories_temp[0].project_catagories+categories_temp[0].year+'-'+str(categories_temp[0].semester)+'-'+categories_temp[0].number) #if have add project id to list
                    if len(noti_temp)==0: #check noti_temp
                        notification.append('') #if don't have add empty string to list
                    else:
                        notification.append(noti_temp) #if have add notification to list
            project_list.append(project) #add project list to all categories project
            research_list.append(research) #add research list to all categories project
            offer_list.append(offer) #add offer list to all categories project
            approve_list.append(approve) #add approve list to all categories project
            timeLine_list.append(timeLine) #add timeline list to all categories project
            categories_id_list.append(categories_id) #add categories id list to all categories project
            project_id_list.append(project_id) #add project id list to all categories project
            notification_list.append(notification) #add notification list to all categories project
            return render(request, 'group6/index_officer.html', {'main0': main[0], 'project_list0': project_list[0], 'research0': research_list[0], 'offer0': offer_list[0], 'approve0': approve_list[0], 'timeLine0': timeLine_list[0], 'categories_id0':categories_id_list[0], 'project_id0': project_id_list[0], 'message0': notification_list[0], 'main1': main[1], 'project_list1': project_list[1], 'research1': research_list[1], 'offer1': offer_list[1], 'approve1': approve_list[1], 'timeLine1': timeLine_list[1], 'categories_id1':categories_id_list[1], 'project_id1': project_id_list[1], 'message1': notification_list[1], 'main2': main[2], 'project_list2': project_list[2], 'research2': research_list[2], 'offer2': offer_list[2], 'approve2': approve_list[2], 'timeLine2': timeLine_list[2], 'categories_id2':categories_id_list[2], 'project_id2': project_id_list[2], 'message2': notification_list[2], 'main3': main[3], 'project_list3': project_list[3], 'research3': research_list[3], 'offer3': offer_list[3], 'approve3': approve_list[3], 'timeLine3': timeLine_list[3], 'categories_id3':categories_id_list[3], 'project_id3': project_id_list[3], 'message3': notification_list[3], 'main4': main[4], 'project_list4': project_list[4], 'research4': research_list[4], 'offer4': offer_list[4], 'approve4': approve_list[4], 'timeLine4': timeLine_list[4], 'categories_id4':categories_id_list[4], 'project_id4': project_id_list[4], 'message4': notification_list[4], 'main5': 'Uncategories', 'project_list5': project_list[5], 'research5': research_list[5], 'offer5': offer_list[5], 'approve5': approve_list[5], 'timeLine5': timeLine_list[5], 'categories_id5':categories_id_list[5], 'project_id5': project_id_list[5], 'message5': notification_list[5]}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render create form and project data url project_docs_create_3forms
def create_3forms(request):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '0': #check user type is not student
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถสร้างฟอร์มได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            s = Student.objects.get(userprofile=u) #get Student data
            teachers = Teacher.objects.all() #get all teacher data from database
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'numOP': 1, 'yearOE': int(datetime.now().year + 543), 'edit': '1', 'student_all': Student.objects.all(), 'yearEN': int(datetime.now().year + 543), 'semester': '1'},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for add new form and project data to database url project_docs_create_3forms_add
def create_3forms_add(request):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '0': #check user type is not student
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถสร้างฟอร์มได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        s = Student.objects.get(userprofile=u) #get Student data
        s_list, myCheck, process, myCheck1, myCheck2, myCheck3, myCheck4, myCheck5, myCheck6, myCheck7, myCheck8 = [], [], [], [], [], [], [], [], [], [], [] #create empty list to store data
        s_list.append(s) #add current student as head of project
        yearOE, nameTH, nameEN, numOP, adv, obj, scopes, benefits, reasons, priceOM, priceOO, credits, courses, semester, yearEN, dateST, process1, process2, process3, process4, process5, process6, process7, process8, note = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "" #declare variable to get from POST
        error_yearOE, error_nameTH, error_nameEN, error_numOP, error_adv, error_obj, error_scopes, error_benefits, error_reasons, error_priceOM, error_priceOO, error_credits, error_courses, error_semester, error_yearEN, error_process, error_dateST = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "" #declare variable to store error message
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
                if nameTH == "" : #Check nameTH is empty???
                    error_nameTH = "*กรุณาใส่ชื่อโครงงาน (ภาษาไทย)" #If empty set error message and error to true
                    error = True
                elif len(ProjectG6.objects.filter(name_thai=nameTH)) != 0: #check project name already have (thai)
                    error_nameTH = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาไทย)" #If nameTH is in use set error message and error to true
                    error = True
                if nameEN == "" : #Check nameEN is empty???
                    error_nameEN = "*กรุณาใส่ชื่อโครงงาน (ภาษาอังกฤษ)" #If empty set error message and error to true
                    error = True
                elif len(ProjectG6.objects.filter(name_eng=nameEN)) != 0: #check project name already have (english)
                    error_nameEN = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาอังกฤษ)" #If nameEN is in use set error message and error to true
                    error = True
                if len(Teacher.objects.filter(id=int(adv))) == 0: #check have adviser in database
                    error_adv = "*กรุณาเลือกที่ปรึกษาใหม่" #If no adviser in database set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 543) or int(yearOE) < int(datetime.now().year + 535) or yearOE == "": #check year of education
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If yearOE out of range or empty set error message and error to true
                    error = True
                if int(numOP) > 5 or int(numOP) < 1 or numOP == "": #check number of student
                    error_numOP = "*กรุณาเลือกจำนวนคนใหม่" #If numOP out of range or empty set error message and error to true
                    error = True
                if obj == "" : #check objective is empty???
                    error_obj = "*กรุณากรอกวัตถุประสงค์" #If empty set error message and error to true
                    error = True
                if scopes == "" : #check scope is empty???
                    error_scopes = "*กรุณากรอกขอบเขตของการทำโครงงาน" #If empty set error message and error to true
                    error = True
                if benefits == "" : #check benefit is empty???
                    error_benefits = "*กรุณากรอกผลประโยชน์ที่คาดว่าจะได้รับ" #If empty set error message and error to true
                    error = True
                if reasons == "" : #check reason is empty???
                    error_reasons = "*กรุณากรอกแนวเหตุผล ทฤษฏีสำคัญหรือสมมุติฐาน" #If empty set error message and error to true
                    error = True
                if courses == "" : #check course is empty???
                    error_courses = "*กรุณากรอกชื่อวิชา" #If empty set error message and error to true
                    error = True
                if priceOM == "" : #Check price of material is empty???
                    error_priceOM = "*กรุณากรอกค่าวัสดุ" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        float(priceOM) #Check price is float???
                    except ValueError:
                        error_priceOM = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
                        error = True
                if priceOO == "" : #Check price of other is empty???
                    error_priceOO = "*กรุณากรอกค่าใช้จ่ายเบ็ดเตล็ด" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        float(priceOO) #Check price is float???
                    except ValueError:
                        error_priceOO = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
                        error = True
                if credits == "" : #Check credit is empty???
                    error_credits = "*กรุณากรอกจำนวนหน่วยกิจ" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        int(credits) #Check credit is int???
                    except ValueError:
                        error_credits = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                        error = True
                if semester == "" : #Check semester is empty???
                    error_semester = "*กรุณากรอกภาคเรียน" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        int(semester) #Check semester is int???
                    except ValueError:
                        error_semester = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                        error = True
                if yearEN == "" : #Check year end is empty???
                    error_yearEN = "*กรุณากรอกปีการศึกษา" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        int(yearEN) #Check year end is int???
                    except ValueError:
                        error_yearEN = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                        error = True
                if 'studentID1' in request.POST: #check have studentID1 in POST
                    studentID = request.POST['studentID1'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True #set error to true
                if 'studentID2' in request.POST: #check have studentID2 in POST
                    studentID = request.POST['studentID2'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID))) #if no_add true
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว")) #if no_add false
                        error = True #set error to true
                if 'studentID3' in request.POST: #check have studentID3 in POST
                    studentID = request.POST['studentID3'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID))) #if no_add true
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว")) #if no_add false
                        error = True #set error to true
                if 'studentID4' in request.POST: #check have studentID4 in POST
                    studentID = request.POST['studentID4'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID))) #if no_add true
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว")) #if no_add false
                        error = True #set error to true
                if int(numOP) != len(s_list): #check numOP is not equal s_list size
                    error = True #set error to true
                if dateST == "": #Check date end is empty???
                    error = True  #If empty set error message and error to true
                    error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                else:
                    date = dateST.split("-") #split date to 3 part (year, month, day)
                    if len(date) != 3:
                        error = True  #If can't split to 3 part set error message and error to true
                        error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                if process1 == "": #Check process1 is empty???
                    error_process = "*กรุณาระบุขั้นตอนการดำเนินงาน อย่างน้อย 1 ขั้นตอน" #If empty set error message and error to true
                    error = True
                else:
                    for i in range(1,13): #read 12 month
                        if ('myCheck1/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck1.append(True) #append True to list
                        else:
                            myCheck1.append(False) #append False to list
                if process2 != "": #Check process2 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck2/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck2.append(True) #append True to list
                        else:
                            myCheck2.append(False) #append False to list
                if process3 != "": #Check process3 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck3/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck3.append(True) #append True to list
                        else:
                            myCheck3.append(False) #append False to list
                if process4 != "": #Check process4 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck4/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck4.append(True) #append True to list
                        else:
                            myCheck4.append(False) #append False to list
                if process5 != "": #Check process5 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck5/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck5.append(True) #append True to list
                        else:
                            myCheck5.append(False) #append False to list
                if process6 != "": #Check process6 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck6/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck6.append(True) #append True to list
                        else:
                            myCheck6.append(False) #append False to list
                if process7 != "": #Check process7 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck7/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck7.append(True) #append True to list
                        else:
                            myCheck7.append(False) #append False to list
                if process8 != "": #Check process8 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck8/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck8.append(True) #append True to list
                        else:
                            myCheck8.append(False) #append False to list
                myCheck.append(myCheck1) #add all process and check to store list
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
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'error_yearOE': error_yearOE, 'error_nameTH': error_nameTH, 'error_nameEN': error_nameEN, 'error_numOP': error_numOP, 'error_adv': error_adv, 'error_obj': error_obj, 'error_scopes': error_scopes, 'error_benefits': error_benefits, 'error_reasons': error_reasons, 'error_priceOM': error_priceOM, 'error_priceOO': error_priceOO, 'error_credits': error_credits, 'error_courses': error_courses, 'error_semester': error_semester, 'error_yearEN': error_yearEN, 'error_student': error_student, 'nameTH': nameTH, 'nameEN': nameEN, 'obj': obj, 'scopes': scopes, 'benefits': benefits, 'reasons': reasons, 'priceOM': priceOM, 'priceOO': priceOO, 'credits': credits, 'courses': courses, 'semester': semester, 'yearEN': yearEN, 'student_list': s_list, 'numOP': numOP, 'yearOE': yearOE, 'edit': '1', 'error_dateST': error_dateST, 'startDate': dateST, 'error_process': error_process, 'note': note, 'process1': process1, 'checkList1': myCheck1, 'process2': process2, 'checkList2': myCheck2, 'process3': process3, 'checkList3': myCheck3, 'process4': process4, 'checkList4': myCheck4, 'process5': process5, 'checkList5': myCheck5, 'process6': process6, 'checkList6': myCheck6, 'process7': process7, 'checkList7': myCheck7, 'process8': process8, 'checkList8': myCheck8, 'student_all': Student.objects.all()},) #render template with all data
        project = ProjectG6(teacher = Teacher.objects.get(id=int(adv)), name_thai = nameTH, name_eng = nameEN, yearOfEducation = yearOE, objective = obj, reason = reasons, scope = scopes, benefit = benefits) #create project data
        project.save() #save to database
        project.student = s_list #assign student from s_list
        research = ResearchProjectForm(project = project, numberOfPeople = numOP) #create research data
        research.save() #save to database
        offer = OfferProjectForm(project = project, priceOfMaterial = priceOM, priceOfOther = priceOO) #create offer data
        offer.save() #save to database
        approve = ApproveProjectForm(project = project, student = s, course = courses, semesterEnd = semester, yearEnd = yearEN, credit = credits) #create approve data
        approve.save() #save to database
        timeline = TimeLineForm(project = project, day = date[2], month = month[int(date[1])-1], year = int(date[0])+543, note = note) #create timeline data
        timeline.save() #save to database
        for i in range(8): #for loop with max range of process(8 round)
            if process[i] != '': #if process at i is not empty
                step = StepInTimeLine(timeline = timeline, numberOfProcess = i+1, processDescription = process[i], month1 = myCheck[i][0], month2 = myCheck[i][1], month3 = myCheck[i][2], month4 = myCheck[i][3], month5 = myCheck[i][4], month6 = myCheck[i][5], month7 = myCheck[i][6], month8 = myCheck[i][7], month9 = myCheck[i][8], month10 = myCheck[i][9], month11 = myCheck[i][10], month12 = myCheck[i][11]) #create stepintimeline data
                step.save() #save to database
        messages.add_message(request, messages.INFO, "การสร้างฟอร์มของโปรเจคสำเร็จ") #add message to show on index page
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for check student is not in list
def checkNotInList(storeList, item):
    for i in storeList: #for loop in list
        if i != "":
            if i.std_id == item: #check student in list and variable 
                return False #false if student is already in list
    return True #true if not found student in list

#function for render edit form and project data page url project_docs_edit
def edit_3forms(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '0': #check user type is not student
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถแก้ไขฟอร์มได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            s = Student.objects.get(userprofile=u) #get Student data
            p = ProjectG6.objects.get(id=pjID) #get current project data
            for student in p.student.all(): #for loop to check user
                if student.std_id == s.std_id: #if current user in project group
                    error = False #set error to false
                    break
            if error == True: #if error is true
                return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
            process, myCheck = [], [] #create empty list to store data
            teachers = Teacher.objects.all() #get all teacher data from database
            research = ResearchProjectForm.objects.get(project=p) #get research data by current project
            offer = OfferProjectForm.objects.get(project=p) #get offer data by current project
            approve = ApproveProjectForm.objects.get(project=p) #get approve data by current project
            timeLine = TimeLineForm.objects.get(project=p) #get timeline data by current project
            for i in range(8): #for loop with max range of process(8 round)
                pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1)  #get process from database
                if len(pro) == 0: #check have process
                    process.append("") #if not append empty string to description
                    myCheck.append([]) #if not append empty list
                else:
                    process.append(pro[0].processDescription) #if have append description string to list
                    myCheck.append([pro[0].month1, pro[0].month2, pro[0].month3, pro[0].month4, pro[0].month5, pro[0].month6, pro[0].month7, pro[0].month8, pro[0].month9, pro[0].month10, pro[0].month11, pro[0].month12]) #if have append process list
            startDate = str(timeLine.year-543)+'-' #string to set date in form4
            if month.index(timeLine.month.encode("utf-8"))+1 < 10: #check month less than 10
                startDate += '0'+str(month.index(timeLine.month.encode("utf-8"))+1)+'-' #add 0 with number of moth
            else:
                startDate += str(month.index(timeLine.month.encode("utf-8"))+1)+'-' #add number of month
            if timeLine.day < 10: #check date less than 10
                startDate += '0'+str(timeLine.day) #add 0 with date
            else:
                startDate += str(timeLine.day) #add date
            s_list = [] #create list to store student in this project
            s_list.append(approve.student) #append head of project
            for i in p.student.all(): #for loop all student in project
                if i != approve.student: #if not head of project
                    s_list.append(i) #append to list
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'nameTH': p.name_thai, 'nameEN': p.name_eng, 'obj': p.objective, 'scopes': p.scope, 'benefits': p.benefit, 'reasons': p.reason, 'priceOM': offer.priceOfMaterial, 'priceOO': offer.priceOfOther, 'credits': approve.credit, 'courses': approve.course, 'semester': approve.semesterEnd, 'yearEN': approve.yearEnd, 'student_list': s_list, 'numOP': research.numberOfPeople, 'yearOE': p.yearOfEducation, 'edit': '0', 'project_id': p.id, 'startDate': startDate, 'note': timeLine.note, 'process1': process[0], 'checkList1': myCheck[0], 'process2': process[1], 'checkList2': myCheck[1], 'process3': process[2], 'checkList3': myCheck[2], 'process4': process[3], 'checkList4': myCheck[3], 'process5': process[4], 'checkList5': myCheck[4], 'process6': process[5], 'checkList6': myCheck[5], 'process7': process[6], 'checkList7': myCheck[6], 'process8': process[7], 'checkList8': myCheck[7], 'student_all': Student.objects.all()},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for edit form and project data to database url project_docs_edit_update
def edit_3forms_update(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '0': #check user type is not student
            messages.add_message(request, messages.INFO, "นักเรียนเท่านั้นที่สามารถแก้ไขฟอร์มได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        p = ProjectG6.objects.get(id=pjID) #get current project data
        s = ApproveProjectForm.objects.get(project=p).student #get head of project student
        s_list, myCheck, process, myCheck1, myCheck2, myCheck3, myCheck4, myCheck5, myCheck6, myCheck7, myCheck8 = [], [], [], [], [], [], [], [], [], [], [] #create empty list to store data
        s_list.append(s) #add current student as head of project
        yearOE, nameTH, nameEN, numOP, adv, obj, scopes, benefits, reasons, priceOM, priceOO, credits, courses, semester, yearEN, dateST, process1, process2, process3, process4, process5, process6, process7, process8, note = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "" #declare variable to get from POST
        error_yearOE, error_nameTH, error_nameEN, error_numOP, error_adv, error_obj, error_scopes, error_benefits, error_reasons, error_priceOM, error_priceOO, error_credits, error_courses, error_semester, error_yearEN, error_process, error_dateST = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "" #declare variable to store error message
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
                if nameTH == "" : #Check nameTH is empty???
                    error_nameTH = "*กรุณาใส่ชื่อโครงงาน (ภาษาไทย)" #If empty set error message and error to true
                    error = True
                elif len(ProjectG6.objects.filter(name_thai=nameTH)) != 0 and p.name_thai != nameTH: #check project name already have (thai) when change name
                    error_nameTH = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาไทย)" #If nameTH is in use set error message and error to true
                    error = True
                if nameEN == "" : #Check nameEN is empty???
                    error_nameEN = "*กรุณาใส่ชื่อโครงงาน (ภาษาอังกฤษ)" #If empty set error message and error to true
                    error = True
                elif len(ProjectG6.objects.filter(name_eng=nameEN)) != 0 and p.name_eng != nameEN: #check project name already have (english) when change name
                    error_nameEN = "*ชื่อโครงงานนี้มีอยู่แล้ว (ภาษาอังกฤษ)" #If nameEN is in use set error message and error to true
                    error = True
                if len(Teacher.objects.filter(id=int(adv))) == 0: #check have adviser in database
                    error_adv = "*กรุณาเลือกที่ปรึกษาใหม่" #If no adviser in database set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 543) or int(yearOE) < int(datetime.now().year + 535) or yearOE == "": #check year of education
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If yearOE out of range or empty set error message and error to true
                    error = True
                if int(numOP) > 5 or int(numOP) < 1 or numOP == "": #check number of student
                    error_numOP = "*กรุณาเลือกจำนวนคนใหม่" #If numOP out of range or empty set error message and error to true
                    error = True
                if obj == "" : #check objective is empty???
                    error_obj = "*กรุณากรอกวัตถุประสงค์" #If empty set error message and error to true
                    error = True
                if scopes == "" : #check scope is empty???
                    error_scopes = "*กรุณากรอกขอบเขตของการทำโครงงาน" #If empty set error message and error to true
                    error = True
                if benefits == "" : #check benefit is empty???
                    error_benefits = "*กรุณากรอกผลประโยชน์ที่คาดว่าจะได้รับ" #If empty set error message and error to true
                    error = True
                if reasons == "" : #check reason is empty???
                    error_reasons = "*กรุณากรอกแนวเหตุผล ทฤษฏีสำคัญหรือสมมุติฐาน" #If empty set error message and error to true
                    error = True
                if courses == "" : #check course is empty???
                    error_courses = "*กรุณากรอกชื่อวิชา" #If empty set error message and error to true
                    error = True
                if priceOM == "" : #Check price of material is empty???
                    error_priceOM = "*กรุณากรอกค่าวัสดุ" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        float(priceOM) #Check price is float???
                    except ValueError:
                        error_priceOM = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
                        error = True
                if priceOO == "" : #Check price of other is empty???
                    error_priceOO = "*กรุณากรอกค่าใช้จ่ายเบ็ดเตล็ด" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        float(priceOO) #Check price is float???
                    except ValueError:
                        error_priceOO = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not float set error message and error to true
                        error = True
                if credits == "" : #Check credit is empty???
                    error_credits = "*กรุณากรอกจำนวนหน่วยกิจ" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        int(credits) #Check credit is int???
                    except ValueError:
                        error_credits = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                        error = True
                if semester == "" : #Check semester is empty???
                    error_semester = "*กรุณากรอกภาคเรียน" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        int(semester) #Check semester is int???
                    except ValueError:
                        error_semester = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                        error = True
                if yearEN == "" : #Check year end is empty???
                    error_yearEN = "*กรุณากรอกปีการศึกษา" #If empty set error message and error to true
                    error = True
                else:
                    try:
                        int(yearEN) #Check year end is int???
                    except ValueError:
                        error_yearEN = "*กรุณากรอกเฉพาะตัวเลขเท่านั้น" #If not integer set error message and error to true
                        error = True
                if 'studentID1' in request.POST: #check have studentID1 in POST
                    studentID = request.POST['studentID1'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID)))
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว"))
                        error = True #set error to true
                if 'studentID2' in request.POST: #check have studentID2 in POST
                    studentID = request.POST['studentID2'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID))) #if no_add true
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว")) #if no_add false
                        error = True #set error to true
                if 'studentID3' in request.POST: #check have studentID3 in POST
                    studentID = request.POST['studentID3'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID))) #if no_add true
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว")) #if no_add false
                        error = True #set error to true
                if 'studentID4' in request.POST: #check have studentID4 in POST
                    studentID = request.POST['studentID4'] #Get Value from key
                    no_add = checkNotInList(s_list, studentID) #check student not in list
                    if len(Student.objects.filter(std_id=studentID)) == 1 and no_add: #check student in database
                        s_list.append(Student.objects.get(std_id=studentID)) #append student list
                        error_student.append("") #append empty string to error list
                    else:
                        s_list.append("") #append empty string to student list
                        if no_add: #check no_add true
                            error_student.append(("*ไม่พบนักศึกษาเลขประจำตัว "+str(studentID))) #if no_add true
                        else:
                            error_student.append(("*เลขประจำตัว "+str(studentID)+" มีอยู่แล้ว")) #if no_add false
                        error = True #set error to true
                if int(numOP) != len(s_list): #check numOP is not equal s_list size
                    error = True #set error to true
                if dateST == "": #Check date end is empty???
                    error = True  #If empty set error message and error to true
                    error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                else:
                    date = dateST.split("-") #split date to 3 part (year, month, day)
                    if len(date) != 3:
                        error = True  #If can't split to 3 part set error message and error to true
                        error_dateST = "*กรุณาตรวจสอบวันที่ใหม่"
                if process1 == "": #Check process1 is empty???
                    error_process = "*กรุณาระบุขั้นตอนการดำเนินงาน อย่างน้อย 1 ขั้นตอน" #If empty set error message and error to true
                    error = True
                else:
                    for i in range(1,13): #read 12 month
                        if ('myCheck1/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck1.append(True) #append True to list
                        else:
                            myCheck1.append(False) #append False to list
                if process2 != "": #Check process2 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck2/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck2.append(True) #append True to list
                        else:
                            myCheck2.append(False) #append False to list
                if process3 != "": #Check process3 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck3/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck3.append(True) #append True to list
                        else:
                            myCheck3.append(False) #append False to list
                if process4 != "": #Check process4 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck4/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck4.append(True) #append True to list
                        else:
                            myCheck4.append(False) #append False to list
                if process5 != "": #Check process5 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck5/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck5.append(True) #append True to list
                        else:
                            myCheck5.append(False) #append False to list
                if process6 != "": #Check process6 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck6/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck6.append(True) #append True to list
                        else:
                            myCheck6.append(False) #append False to list
                if process7 != "": #Check process7 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck7/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck7.append(True) #append True to list
                        else:
                            myCheck7.append(False) #append False to list
                if process8 != "": #Check process8 is empty???
                    for i in range(1,13): #read 12 month
                        if ('myCheck8/'+str(i)) in request.POST: #check check at month i in POST
                            myCheck8.append(True) #append True to list
                        else:
                            myCheck8.append(False) #append False to list
                myCheck.append(myCheck1) #add all process and check to store list
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
            return render(request, 'group6/create_3forms.html', {'teachers': teachers, 'student': s, 'error_yearOE': error_yearOE, 'error_nameTH': error_nameTH, 'error_nameEN': error_nameEN, 'error_numOP': error_numOP, 'error_adv': error_adv, 'error_obj': error_obj, 'error_scopes': error_scopes, 'error_benefits': error_benefits, 'error_reasons': error_reasons, 'error_priceOM': error_priceOM, 'error_priceOO': error_priceOO, 'error_credits': error_credits, 'error_courses': error_courses, 'error_semester': error_semester, 'error_yearEN': error_yearEN, 'error_student': error_student, 'nameTH': nameTH, 'nameEN': nameEN, 'obj': obj, 'scopes': scopes, 'benefits': benefits, 'reasons': reasons, 'priceOM': priceOM, 'priceOO': priceOO, 'credits': credits, 'courses': courses, 'semester': semester, 'yearEN': yearEN, 'student_list': s_list, 'numOP': numOP, 'yearOE': yearOE, 'edit': '0', 'project_id': p.id, 'error_dateST': error_dateST, 'startDate': dateST, 'error_process': error_process, 'note': note, 'process1': process1, 'checkList1': myCheck1, 'process2': process2, 'checkList2': myCheck2, 'process3': process3, 'checkList3': myCheck3, 'process4': process4, 'checkList4': myCheck4, 'process5': process5, 'checkList5': myCheck5, 'process6': process6, 'checkList6': myCheck6, 'process7': process7, 'checkList7': myCheck7, 'process8': process8, 'checkList8': myCheck8, 'student_all': Student.objects.all()},) #render template with all data
        p.teacher = Teacher.objects.get(id=int(adv)) #project update adviser
        p.name_thai = nameTH #project update name thai
        p.name_eng = nameEN #project update name english
        p.yearOfEducation = yearOE #project update year of education
        p.objective = obj #project update objective
        p.reason = reasons #project update reason
        p.scope = scopes #project update scope
        p.benefit = benefits #project update benefit
        p.student = s_list #project update student in project
        p.save() #project data save change
        research = ResearchProjectForm.objects.get(project=p) #get research data
        research.numberOfPeople = numOP #research update number of people
        research.save() #research data save change
        offer = OfferProjectForm.objects.get(project=p) #get offer data
        offer.priceOfMaterial = priceOM #offer update price of material
        offer.priceOfOther = priceOO #offer update price of other
        offer.save() #offer data save change
        approve = ApproveProjectForm.objects.get(project=p) #get approve data
        approve.student = s #approve update student
        approve.course = courses #approve update course
        approve.semesterEnd = semester #approve update semester end
        approve.yearEnd = yearEN #approve update year end
        approve.credit = credits #approve update credit
        approve.save() #approve data save change
        timeline = TimeLineForm.objects.get(project=p) #get timeline data
        timeline.day = date[2] #timeline update day
        timeline.month = month[int(date[1])-1] #timeline update month
        timeline.year = int(date[0])+543 #timeline update year
        timeline.note = note #timeline update note
        timeline.save() #timeline data save change
        for i in range(8): #for loop with max range of process(8 round)
            step_list = StepInTimeLine.objects.filter(timeline=timeline, numberOfProcess=i+1) #get stepintimeline data at i
            if process[i] != '': #if process is not empty
                if len(step_list) == 0: #if step list is empty
                    step = StepInTimeLine(timeline = timeline, numberOfProcess = i+1, processDescription = process[i], month1 = myCheck[i][0], month2 = myCheck[i][1], month3 = myCheck[i][2], month4 = myCheck[i][3], month5 = myCheck[i][4], month6 = myCheck[i][5], month7 = myCheck[i][6], month8 = myCheck[i][7], month9 = myCheck[i][8], month10 = myCheck[i][9], month11 = myCheck[i][10], month12 = myCheck[i][11]) #create stepintimeline data
                    step.save() #stepintimeline save to database
                else:
                    step_list[0].processDescription = process[i] #update all data for stepintimeline data
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
                    step_list[0].save() #stepintimeline data save change
            else:
                if len(step_list) == 1: #if have stepintimeline already
                    step_list[0].delete() #stepintimeline delete
        messages.add_message(request, messages.INFO, "การแก้ไขฟอร์มของโปรเจคสำเร็จ") #add message to show on index page
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render approve form url project_docs_approveProject
def approveProject(request, apID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        approve = ApproveProjectForm.objects.get(id=apID) #get current approve data from database
        if u.type == '0': #check user type is student
            s = Student.objects.get(userprofile=u) #get Student data
            year = int(datetime.now().year - 2000 + 43) - int(s.std_id[:2]) #get student year
            return render(request, 'group6/approveProject_view.html', {'approve': approve, 'scheme': scheme[int(s.scheme)], 'department': department[int(s.userprofile.department)], 'main': main[int(s.main)], 'currentYear': year, 'student': s},) #render template with all data
        else:
            year = int(datetime.now().year - 2000 + 43) - int(approve.student.std_id[:2]) #get student year
            return render(request, 'group6/approveProject_view.html', {'approve': approve, 'scheme': scheme[int(approve.student.scheme)], 'department': department[int(approve.student.userprofile.department)], 'main': main[int(approve.student.main)], 'currentYear': year},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render offer form url project_docs_offerProject
def offerProject(request, opID):
    if request.user.is_authenticated(): #check user already authenticated
        offer = OfferProjectForm.objects.get(id=opID) #get current offer data from database
        sumofprice = offer.priceOfMaterial + offer.priceOfOther #calculate summary price
        student_head = ApproveProjectForm.objects.get(project=offer.project).student #get student head of project
        s_list = [] #create empty list to store student
        s_list.append(student_head) #append head of project to list
        for i in offer.project.student.all(): #for loop student
            if i != student_head: #if student not head of project
                s_list.append(i) #append student to list
        return render(request, 'group6/offerProject_view.html', {'offer': offer, 'priceOfTotal': sumofprice, 'student_list': s_list},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render research form url project_docs_researchProject
def researchProject(request, rpID):
    if request.user.is_authenticated(): #check user already authenticated
        research = ResearchProjectForm.objects.get(id=rpID) #get current research data from database
        return render(request, 'group6/researchProject_view.html', {'research': research},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render timeline form url project_docs_timeLineProject
def timeLineProject(request, tlID):
    if request.user.is_authenticated(): #check user already authenticated
        timeLine = TimeLineForm.objects.get(id=tlID) #get current timeline
        processList = [] #create empty list for store process
        for i in range(8): #for loop with max range of process(8 round)
            pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1) #get process from database
            if len(pro) == 0: #check have process
                processList.append([]) #if not append empty list
            else:
                processList.append(pro[0]) #if have append process
        return render(request, 'group6/timeLineProject_view.html', {'timeLine': timeLine, 'processList': processList, 'officer': UserProfile.objects.get(user=request.user).type},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to delete form and project data from database url project_docs_delete
def deleteForm(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        error = True #check for student in group
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            if u.type == '1': #check user type is teacher
                messages.add_message(request, messages.INFO, "นักศึกษาในกลุ่มหรือเจ้าหน้าที่ภาคเท่านั้นที่สามารถลบฟอร์มได้") #add message to show on index page
                return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
            s = Student.objects.get(userprofile=u) #get Student data
            p = ProjectG6.objects.get(id=pjID) #get current project data
            for student in p.student.all(): #for loop to check student
                if student.std_id == s.std_id: #if current user is one of student in project group
                    error = False #set error to false
                    break
            if error == True: #if user not student in group
                messages.add_message(request, messages.INFO, "นักศึกษาในกลุ่มหรือเจ้าหน้าที่ภาคเท่านั้นที่สามารถลบฟอร์มได้") #add message to show on index page
                return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
            p.delete() #delete from database
            messages.add_message(request, messages.INFO, "การลบฟอร์มของโปรเจคสำเร็จ") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            p = ProjectG6.objects.get(id=pjID) #get current project data
            p.delete() #delete from database
            messages.add_message(request, messages.INFO, "การลบฟอร์มของโปรเจคสำเร็จ") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render approve form print url project_docs_approveProject_print
def approveProjectPrint(request, apID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        approve = ApproveProjectForm.objects.get(id=apID) #get current approve data from database
        if u.type == '0': #check user type is student
            s = Student.objects.get(userprofile=u) #get Student data
            year = int(datetime.now().year - 2000 + 43) - int(s.std_id[:2]) #get student year
            return render(request, 'group6/approveProject_view_print.html', {'approve': approve, 'scheme': scheme[int(s.scheme)], 'department': department[int(s.userprofile.department)], 'main': main[int(s.main)], 'currentYear': year, 'student': s},) #render template with all data
        else:
            year = int(datetime.now().year - 2000 + 43) - int(approve.student.std_id[:2]) #get student year
            return render(request, 'group6/approveProject_view_print.html', {'approve': approve, 'scheme': scheme[int(approve.student.scheme)], 'department': department[int(approve.student.userprofile.department)], 'main': main[int(approve.student.main)], 'currentYear': year},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render offer form print url project_docs_offerProject_print
def offerProjectPrint(request, opID):
    if request.user.is_authenticated(): #check user already authenticated
        offer = OfferProjectForm.objects.get(id=opID) #get current offer data from database
        sumofprice = offer.priceOfMaterial + offer.priceOfOther #calculate summary price
        student_head = ApproveProjectForm.objects.get(project=offer.project).student #get student head of project
        s_list = [] #create empty list to store student
        s_list.append(student_head) #append head of project to list
        for i in offer.project.student.all(): #for loop student
            if i != student_head: #if student not head of project
                s_list.append(i) #append student to list
        return render(request, 'group6/offerProject_view_print.html', {'offer': offer, 'priceOfTotal': sumofprice, 'student_list': s_list},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render research form print url project_docs_researchProject_print
def researchProjectPrint(request, rpID):
    if request.user.is_authenticated(): #check user already authenticated
        research = ResearchProjectForm.objects.get(id=rpID) #get current research data from database
        return render(request, 'group6/researchProject_view_print.html', {'research': research},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render timeline form print(black tab) url project_docs_timeLineProject_print
def timeLineProjectPrint(request, tlID):
    if request.user.is_authenticated(): #check user already authenticated
        timeLine = TimeLineForm.objects.get(id=tlID) #get current timeline
        processList = [] #create empty list for store process
        for i in range(8): #for loop with max range of process(8 round)
            pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1) #get process from database
            if len(pro) == 0: #check have process
                processList.append([]) #if not append empty list
            else:
                processList.append(pro[0]) #if have append process
        return render(request, 'group6/timeLineProject_view_print.html', {'timeLine': timeLine, 'processList': processList},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function to render timeline form print(checkbox) url project_docs_timeLineProject_print_check
def timeLineProjectPrintCheck(request, tlID):
    if request.user.is_authenticated(): #check user already authenticated
        timeLine = TimeLineForm.objects.get(id=tlID) #get current timeline
        processList = [] #create empty list for store process
        for i in range(8): #for loop with max range of process(8 round)
            pro = StepInTimeLine.objects.filter(timeline=timeLine, numberOfProcess=i+1) #get process from database
            if len(pro) == 0: #check have process
                processList.append([]) #if not append empty list
            else:
                processList.append(pro[0]) #if have append process
        return render(request, 'group6/timeLineProject_view_print_check.html', {'timeLine': timeLine, 'processList': processList},) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render add categories tester page url project_docs_add_categories_tester
def add_categories_tester(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถกำหนด Categories กับอาจารย์สอบโปรเจคได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            p = ProjectG6.objects.get(id=pjID) #get project data
            if len(CategoriesProject.objects.filter(project=p)) != 0: #check project already have categories
                messages.add_message(request, messages.INFO, "โครงงานนี้ได้กำหนด Categories กับอาจารย์สอบโปรเจคแล้ว") #add message to show on index page
                return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
            teachers = Teacher.objects.all() #get all teacher from database
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '1', 'teacher_project': p.teacher, 'project_id': p.id, 'teachers': teachers, 'numOT': '1', 'yearOE': int(datetime.now().year + 43 - 2000), 'projNum':"01", 'main':'Cp', 'semester':'1',}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for check teacher is not in list
def checkNotInListTeacher(storeList, item):
    for t in storeList: #for loop in list
        if t != "":
            if t.id == int(item): #check teacher is in list
                return False #false if teacher is in list
    return True #true if teacher is not in list

#function for add new categories to database url project_docs_add_categories_tester_add
def add_categories_tester_add(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถกำหนด Categories กับอาจารย์สอบโปรเจคได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        p = ProjectG6.objects.get(id=pjID) #get project data
        if len(CategoriesProject.objects.filter(project=p)) != 0: #check project already have categories
            messages.add_message(request, messages.INFO, "โครงงานนี้ได้กำหนด Categories กับอาจารย์สอบโปรเจคแล้ว") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        t_list = [] [] #create empty list to store teacher tester
        t_list.append(p.teacher) #add adviser of project to list
        yearOE, numOT, projNum, main, semester = "", "", "", "", "" #declare variable to get from POST
        error_yearOE, error_numOT, error_projNum, error_main, error_semester = "", "", "", "", "" #declare variable to store error message
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
                if main == "" : #Check main is empty???
                    error_main = "*กรุณาเลือกกลุ่มสาขาใหม่" #If empty set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 43 - 2000) or int(yearOE) < int(datetime.now().year + 35 - 2000) or yearOE == "": #check year of education
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If empty or out of range set error message and error to true
                    error = True
                if int(projNum) > 35 or int(projNum) < 1 or projNum == "" : #Check project number
                    error_projNum = "*กรุณาเลือกเลขโครงงานใหม่" #If empty or out of range set error message and error to true
                    error = True
                if int(semester) > 2 or int(semester)<1: #check semester
                    error_semester = "*กรุณาเลือกภาคเรียนใหม่" #If empty or out of range set error message and error to true
                    error = True
                if len(CategoriesProject.objects.filter(number=projNum, project_catagories=main, year=yearOE, semester=semester)) != 0 and error == False: #check project id
                    error_projNum = "*เลขโครงงานนี้ถูกใช้ไปแล้ว" #If have project already use project id set error message and error to true
                    error = True
                if int(numOT) > 5 or int(numOT) < 1 or numOT == "": #check number of teacher
                    error_numOT = "*กรุณาเลือกจำนวนคนใหม่" #If empty or out of range set error message and error to true
                    error = True
                if 'testerNAME1' in request.POST: #check have second teacher
                    testerNAMEID = request.POST['testerNAME1'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if 'testerNAME2' in request.POST: #check have second teacher
                    testerNAMEID = request.POST['testerNAME2'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if 'testerNAME3' in request.POST: #check have second teacher
                    testerNAMEID = request.POST['testerNAME3'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if 'testerNAME4' in request.POST: #check have second teacher
                    testerNAMEID = request.POST['testerNAME4'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if int(numOT) != len(t_list): #if number of teacher not equal size of teacher list
                    error = True
                if error == True: #Check if error is true raise exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            teachers = Teacher.objects.all() #get all teacher from database
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '1', 'teacher_project': p.teacher, 'project_id': p.id, 'error_yearOE': error_yearOE, 'error_teacher': error_teacher, 'error_numOT': error_numOT, 'error_projNum': error_projNum, 'error_main': error_main, 'error_semester': error_semester, 'teacher_list': t_list, 'numOT': numOT, 'yearOE': yearOE, 'projNum':projNum, 'main':main, 'semester':semester, 'teachers':teachers},) #render template with all data
        cp = CategoriesProject(project=p, project_catagories=main, number=projNum, year=yearOE, semester=semester) #create categories project database
        cp.save() #save to database
        cp.teacher = t_list #assign teacher list
        messages.add_message(request, messages.INFO, "การกำหนด Categories กับอาจารย์สอบโปรเจคสำเร็จ") #add message to show on index page
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render edit categories page url project_docs_edit_categories_tester
def edit_categories_tester(request, cpID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถแก้ไข Categories กับอาจารย์สอบโปรเจคได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            cp = CategoriesProject.objects.get(id=cpID) #get current project categories
            teachers = Teacher.objects.all() #get all teacher object
            t_list = [] #create empty list to store teacher tester
            t_list.append('')
            for t in cp.teacher.all(): #for loop to add teacher tester to list
                if t != cp.project.teacher: #check teacher not adviser of project
                    t_list.append(t) #add teacher to list
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '0', 'teacher_project': cp.project.teacher, 'project_id': cp.project.id, 'teachers': teachers, 'numOT': len(cp.teacher.all()), 'yearOE': cp.year, 'projNum': cp.number, 'main': cp.project_catagories, 'semester': cp.semester, 'teacher_list': t_list, 'categories_id': cp.id}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for update categories and tester to database url project_docs_edit_categories_tester_update
def edit_categories_tester_update(request, cpID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถแก้ไข Categories กับอาจารย์สอบโปรเจคได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        cp = CategoriesProject.objects.get(id=cpID) #get current categories data
        t_list = [] #create empty list to store teacher become to tester
        t_list.append(cp.project.teacher) #add adviser of project to list
        yearOE, numOT, projNum, main, semester = "", "", "", "", "" #declare variable to get from POST
        error_yearOE, error_numOT, error_projNum, error_main, error_semester = "", "", "", "", "" #declare variable to store error message
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
                if main == "" : #Check main is empty???
                    error_main = "*กรุณาเลือกกลุ่มสาขาใหม่" #If empty set error message and error to true
                    error = True
                if int(yearOE) > int(datetime.now().year + 43 - 2000) or int(yearOE) < int(datetime.now().year + 35 - 2000) or yearOE == "": #check year of education
                    error_yearOE = "*กรุณาเลือกปีการศึกษาใหม่" #If empty or out of range set error message and error to true
                    error = True
                if int(projNum) > 35 or int(projNum) < 1 or projNum == "" : #Check project number
                    error_projNum = "*กรุณาเลือกเลขโครงงานใหม่" #If empty or out of range set error message and error to true
                    error = True
                if int(semester) > 2 or int(semester)<1 or semester == "": #check semester
                    error_semester = "*กรุณาเลือกภาคเรียนใหม่" #If empty or out of range set error message and error to true
                    error = True
                if cp.number != projNum or cp.project_catagories != main or cp.year != yearOE or cp.semester != int(semester): #check if project id is change
                    if len(CategoriesProject.objects.filter(number=projNum, project_catagories=main, year=yearOE, semester=semester)) != 0 and error == False:
                        error_projNum = "*เลขโครงงานนี้ถูกใช้ไปแล้ว" #If have project already use project id set error message and error to true
                        error = True
                if int(numOT) > 5 or int(numOT) < 1 or numOT == "": #check number of teacher
                    error_numOT = "*กรุณาเลือกจำนวนคนใหม่" #If empty or out of range set error message and error to true
                    error = True
                if 'testerNAME1' in request.POST: #check have second teacher
                    testerNAMEID = request.POST['testerNAME1'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if 'testerNAME2' in request.POST: #check have third teacher
                    testerNAMEID = request.POST['testerNAME2'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if 'testerNAME3' in request.POST: #check have fourth teacher
                    testerNAMEID = request.POST['testerNAME3'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if 'testerNAME4' in request.POST: #check have fifth teacher
                    testerNAMEID = request.POST['testerNAME4'] #Get Value from key
                    no_add = checkNotInListTeacher(t_list, testerNAMEID) #check not in list
                    if len(Teacher.objects.filter(id=testerNAMEID)) == 1 and no_add: #check have teacher and not add to list
                        t_list.append(Teacher.objects.get(id=testerNAMEID)) #add teacher to list
                        error_teacher.append("") #add no error to list
                    else:
                        t_list.append("") #add empty string to teacher list
                        if no_add: #check no add
                            error_teacher.append("*ไม่พบอาจารย์") #add error message to list
                        else:
                            error_teacher.append(("*อาจารย์ ("+str(Teacher.objects.get(id=testerNAMEID).shortname)+") มีอยู่แล้ว")) #add error message to list
                        error = True
                if int(numOT) != len(t_list): #if number of teacher not equal size of teacher list
                    error = True
                if error == True: #Check if error is true raise exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            teachers = Teacher.objects.all() #get all teacher data in database
            return render(request, 'group6/add_categories_exam_teacher.html', {'edit': '0', 'teacher_project': cp.project.teacher, 'project_id': cp.project.id, 'error_yearOE': error_yearOE, 'error_teacher': error_teacher, 'error_numOT': error_numOT, 'error_projNum': error_projNum, 'error_main': error_main, 'error_semester': error_semester, 'teacher_list': t_list, 'numOT': numOT, 'yearOE': yearOE, 'projNum':projNum, 'main':main, 'semester':semester, 'teachers':teachers, 'categories_id': cp.id},) #render template with all data
        cp.teacher = t_list #update teacher list
        cp.semester = int(semester) #update semester
        cp.project_catagories = main #update categories
        cp.number = projNum #update project number
        cp.year = yearOE #update year of education project
        cp.save() #save to database
        messages.add_message(request, messages.INFO, "การแก้ไข Categories กับอาจารย์สอบโปรเจคสำเร็จ") #add message to show on index page
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render add new notification page url project_docs_add_notification
def add_notification(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถสร้างข้อความแจ้งเตือนได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        else:
            return render(request, 'group6/add_notification.html', {'edit': '1', 'project_id': pjID}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for add new notification to database url project_docs_add_notification_add
def add_notification_add(request, pjID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        if u.type != '2':  #check user type is not officer
            messages.add_message(request, messages.INFO, "เจ้าหน้าที่ภาควิชาเท่านั้นที่สามารถสร้างข้อความแจ้งเตือนได้") #add message to show on index page
            return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
        p = ProjectG6.objects.get(id=pjID) #get current project data
        message = "" #declare variable to get from POST
        error_message = ""
        try:
            if 'message' in request.POST: #Check key in POST
                message = request.POST['message'] #Get Value from key
                if message == "" : #Check message is empty???
                    error_message = "*กรุณากรอกข้อความ" #If empty set error message and raise to exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            return render(request, 'group6/add_notification.html', {'edit': '1', 'project_id': pjID, 'message': message, 'error_message': error_message}) #render template with all data
        notification = NotificationProject(project = p, officer = Officer.objects.get(userprofile=u)) #create new notification data
        notification.save() #save to database
        now = datetime.now() #get time stamp
        message_db = Message(text = message, user = u, noti = notification, pub_date = now, pub_date_last= now) #create new message data
        message_db.save() #save to database
        messages.add_message(request, messages.INFO, "การสร้างข้อความแจ้งเตือนสำเร็จ") #add message to show on index page
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render view notification page url project_docs_view_notification
def view_notification(request, nID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        notification = NotificationProject.objects.get(id=nID) #get current notification
        message = Message.objects.filter(noti=notification).order_by('pub_date') #get message and sort by pub_date
        return render(request, 'group6/notification_view.html', {'notification': notification, 'message': message, 'user_now': u}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render add new reply page url project_docs_reply_message
def reply_message(request, nID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        return render(request, 'group6/add_notification.html', {'edit': '2', 'notification_id': nID}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for add new reply message to database url project_docs_reply_message_add
def reply_message_add(request, nID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        message = "" #declare variable to get from POST
        error_message = ""
        try:
            if 'message' in request.POST: #Check key in POST
                message = request.POST['message'] #Get Value from key
                if message == "" : #Check message is empty???
                    error_message = "*กรุณากรอกข้อความ" #If empty set error message and raise to exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            return render(request, 'group6/add_notification.html', {'edit': '2', 'notification_id': nID, 'message': message, 'error_message': error_message}) #render template with all data
        notification = NotificationProject.objects.get(id = nID) #get current notification data
        now = datetime.now() #get time stamp
        message_db = Message(text = message, user = u, noti = notification, pub_date = now, pub_date_last= now) #create new message data
        message_db.save() #save to database
        return HttpResponseRedirect(reverse('group6:project_docs_view_notification', args=(nID))) #redirect to view notification
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for render edit message page url project_docs_edit_notification_message
def edit_notification_message(request, nID, mID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        message = Message.objects.get(id=mID) #get curremt message data
        if u.id != message.user.id: #if current user is not user create message
            return HttpResponseRedirect(reverse('group6:project_docs_view_notification', args=(nID))) #redirect to view notification
        return render(request, 'group6/add_notification.html', {'edit': '0', 'notification_id': nID, 'message_id': mID, 'message': message.text}) #render template with all data
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for update message in notification to database url project_docs_edit_notification_message_update
def edit_notification_message_update(request, nID, mID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        message_db = Message.objects.get(id=mID) #get current message data
        if u.id != message_db.user.id: #if current user is not user create message
            return HttpResponseRedirect(reverse('group6:project_docs_view_notification', args=(nID))) #redirect to view notification
        message = "" #declare variable to get from POST
        error_message = ""
        try:
            if 'message' in request.POST: #Check key in POST
                message = request.POST['message'] #Get Value from key
                if message == "" : #Check message is empty???
                    error_message = "*กรุณากรอกข้อความ" #If empty set error message and raise to exception
                    raise ValueError
            else: #If key invalid raise to exception
                raise KeyError 
        except (KeyError, ValueError): #When exception render form with error message
            return render(request, 'group6/add_notification.html', {'edit': '0', 'notification_id': nID, 'message_id': mID, 'message': message, 'error_message': error_message}) #render template with all data
        message_db.text = message #update new message
        message_db.pub_date_last = datetime.now() #timestamp for last edit
        message_db.save() #save to database
        return HttpResponseRedirect(reverse('group6:project_docs_view_notification', args=(nID))) #redirect to view notification
    else:
        return render(request, 'base.html') #render page to warning user to login

#function for delete notification url project_docs_delete_notification
def delete_notification(request, nID):
    if request.user.is_authenticated(): #check user already authenticated
        u = UserProfile.objects.get(user=request.user) #get current user data
        notification = NotificationProject.objects.get(id=nID) #get notification data from database by id
        if u.id != notification.officer.userprofile.id: #check user command to delete is same as user that create notification
            return HttpResponseRedirect(reverse('group6:project_docs_view_notification', args=(nID))) #redirect to view notification
        notification.delete() #delete data from database
        messages.add_message(request, messages.INFO, "การลบข้อความแจ้งเตือนสำเร็จ") #add message to show on index page
        return HttpResponseRedirect(reverse('group6:project_docs_index')) #redirect to index
    else:
        return render(request, 'base.html') #render page to warning user to login
