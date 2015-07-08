# -*- coding: utf-8 -*-
# !/usr/bin/env python

from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from group5.models import *
from django.views import generic
import django.shortcuts
from login.models import *
from django.template import RequestContext

from django import forms

from django.db.models import Max
from fpdf import FPDF
from datetime import datetime
import  time

#count1 =0

def getUserType(request):
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user=user)
        return userprofile.type
    except:
        return 'admin'


def table_status(request):
    if getUserType(request) == '0':
        thisuser = request.user
        currentUser = UserProfile.objects.get(user=thisuser)
        stu = Student.objects.get(userprofile_id=currentUser.id)
        stuG5 = studentG5.objects.all()
        # pet= StatusPetition.objects.all()
        pet = StatusPetition.objects.filter(studentG5_id=stuG5)
        context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'pet': pet}
        return render(request, 'group5/status.html', context)
    else:
        return render(request, 'group5/error.html')


def table_company(request):
    com = Internship.objects.all()
    context = {'com': com}
    return render(request, 'group5/company.html', context)


def tablef1_status(request):
    if getUserType(request) != '0':
        state = StatusPetition.objects.all()
        stu = Student.objects.all()
        Pro = UserProfile.objects.all()
        context = {'state': state, 'stu': stu, 'Pro': Pro}
        return render(request, 'group5/form1department.html', context)
    else:
        return render(request, 'group5/error.html')


def tablef4_status(request):
    if getUserType(request) != '0':
        state = StatusPetition.objects.all()
        stu = Student.objects.all()
        Pro = UserProfile.objects.all()
        context = {'state': state, 'stu': stu, 'Pro': Pro}
        return render(request, 'group5/form1department4.html', context)
    else:
        return render(request, 'group5/error.html')



def table_addpet(request):
    if getUserType(request) == '0':
        stu_id = request.GET.get('id_student', '')
        to = request.GET.get('to', '')
        stu_year = request.GET.get('stu_year', '')

        office = request.GET.get('office', '')
        address = request.GET.get('address', '')
        tel = request.GET.get('tel', '')
        fax = request.GET.get('fax', '')

        date1 = request.GET.get('date1', '')
        month1 = request.GET.get('month1', '')
        year1 = request.GET.get('year1', '')
        date2 = request.GET.get('date2', '')
        month2 = request.GET.get('month2', '')
        year2 = request.GET.get('year2', '')
        send = request.GET.get('send', '')
        Submit1 = request.GET.get('Submit', '')
        Cancel1 = request.GET.get('Cancel', '')

        prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']

        bf = str(year1) + "-" + str(month1) + "-" + str(date1)
        at = str(year2) + "-" + str(month2) + "-" + str(date2)

        thisuser = request.user
        currentUser = UserProfile.objects.get(user=thisuser)
        stu = Student.objects.get(userprofile_id=currentUser.id)
        stuG5 = studentG5.objects.all()
        stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))
        stat2 = StatusPetition.objects.all()
        j = stat.values()
        j = j[0]
        if j == None:
            j = 0

        state_open ='ยื่นคำร้อง'
        state_open = state_open.decode("utf-8","ignore")
        count1 =0
        if stu_year != '':
            if  len(StatusPetition.objects.filter( studentG5_id=stu_id)) == 0:
                p = studentG5(studentID=stu_id, studentYear=stu_year)
                p.save()

                q = Internship(name_Internship=office.upper(), add_Internship=address, Tel=tel, Fax=fax)
                q.save()

                office = office.upper()
                for i in stat2:
                    if office == i.Internship_id:
                        count1 = 1
            #if len(StatusPetition.objects.filter( studentG5_id=stu_id)) == 0:
                if count1 ==0:
                    r = StatusPetition(NoPetition=j + 1, StatusPetition=state_open, Date=bf, Date2=at, Internship_id=office,
                                   studentG5_id=stu_id, send=send,to=to)
                    r.save()
                count1 = 2
        if stu_year =='':
            if  len(StatusPetition.objects.filter( studentG5_id=stu_id)) != 0:
                messages.add_message(request, messages.INFO, "กรุณาทำการลบแบบฟอร์มก่อนทำการเพิ่มข้อมูล!")

        # if Cancel1 !=  '':
        #    return render(request, 'group5/formstudentprint.html', context)

        # ถ้ามีการกดปุ่ม "บันทึก" จะเปลี่ยนหน้าไปยังหน้า status
        if Submit1 != '':
            return table_status(request)
        context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'stat': stat,
                   'prefix_name1': prefix_name1[int(currentUser.prefix_name)]}
        return render(request, 'group5/form1new.html', context)
    else:
        return render(request, 'group5/error.html')


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvส่วนที่เพิ่มนะจ๊ะvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ปล1 เข้าไปดูในไฟล์ form1 new มีเปลี่ยนตรง<input type="radio" name="sex" value="นาย">นาย    ก่ะ     <input type="radio" name="sex" value="นางสาว">นางสาว

def table_pdf(request):
    state = StatusPetition.objects.all()
    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro}

    thisuser = request.user
    currentUser = UserProfile.objects.get(user=thisuser)
    stu_pro = Student.objects.get(userprofile_id=currentUser.id)
    stuG5 = studentG5.objects.all()
    stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))
    stat2 = StatusPetition.objects.all()
    Intern = Internship.objects.all()

    case = request.GET.get('Submit', '')
    save = request.GET.get('Submit2', '')
    status = request.GET.get('status', '')

    if empty(save) == False:
        for i in state:
            if i.NoPetition == int(save):
                r = StatusPetition(NoPetition=int(save), StatusPetition=status, Date=i.Date, Date2=i.Date2,
                                   Internship_id=i.Internship_id, studentG5_id=i.studentG5_id, send=i.send)
                r.save()

    # stu.std_id
    # pdf.cell(0, 10, u''+case)

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 12)  # 12 is font size
    # for i in state :
    #    if i.NoPetition == case :

    for j in stuG5:
        if j.studentID == stu_pro.std_id:
            pdf.image('group5/picture.png', 90, 8, 33)
            # pdf.image('group5/page.png', 0, 0, 150, 250)
            pdf.ln(10)
            pdf.ln(10)
            pdf.ln(10)
            pdf.ln(10)
            pdf.cell(0, 10,
                     u'                   ข้าพเจ้า' + ' ' + j.sex + ' ' + currentUser.firstname_th + " " + currentUser.lastname_th + u'  รหัสนักศึกษา ' + ' ' + stu_pro.std_id)
            pdf.ln(10)  # new line
            pdf.cell(0, 10, u'          นักศึกษาชั้นปีที่  ' + str(
                j.studentYear) + ' ' + u'มีความประสงค์ขอให้ภาควิชาวิศวกกรมไฟฟ้าและคอมพิวเตอร์ ออกหนังสือ ')
            pdf.ln(10)
            pdf.cell(0, 10, u'          ขอความอนุเคราะห์ฝึกงาน ตามรายละเอียด ดังต่อไปนี้')
            pdf.ln(10)
            pdf.cell(0, 10, u'                   เรียน ฝ่ายทรัพยากรบุคคล')
            pdf.ln(10)

    for i in stat2:
        if case == str(i.NoPetition):
            pdf.cell(0, 10, u'                   สถานที่ฝึกงาน' + ' ' + i.Internship_id)
            pdf.ln(10)
            for j in Intern:
                if i.Internship_id == j.name_Internship:
                    pdf.cell(0, 10, u'                   ที่อยู่' + ' ' + j.add_Internship)
                    pdf.ln(10)

                    pdf.cell(0, 10, u'                   โทรศัพท์' + ' ' + j.Tel + u' โทรสาร(FAX)' + ' ' + j.Fax)
                    pdf.ln(10)

            pdf.cell(50, 10,
                     u'                   ระยะเวลาการฝึกงาน  ตั้งแต่' + ' ' + str(i.Date) + u' ถึงวันที่' + ' ' + str(
                         i.Date2))
            pdf.ln(10)
            pdf.cell(50, 10,
                     u'                                                                           ลงชื่อ..........................................')
            pdf.ln(10)
            pdf.cell(50, 10,
                     u'                                                                               (..........................................)')
            pdf.ln(10)
            pdf.cell(50, 10,
                     u'                                                                                         ผู้ยื่นคำร้อง')
            pdf.ln(10)

    pdf.output("group5/exam.pdf", "F")

    return render(request, 'group5/form1department.html', context)


def table_waitPettition(request):
    if getUserType(request) != '0':
        state = StatusPetition.objects.all()
        stu = Student.objects.all()
        Pro = UserProfile.objects.all()
        acc = accept.objects.all()
        context = {'state': state, 'stu': stu, 'Pro': Pro}

        save = request.GET.get('Submit2', '')
        status = request.GET.get('status', '')

        #now = datetime.datetime.now()
        #Date = now.strftime("%Y-%m-%d")
        date_1=time.strftime("%x")
        day,month,year = date_1.split("/")
        year = int(year)+2000+543
        Date = str(year) +"-"+ month+"-"+day

        acc2 = accept.objects.all().aggregate(Max('No_accept'))
        num = acc2.values()
        num = num[0]
        if num == None:
            num = 0;

        if empty(save) == False:
            for i in state:
                if i.NoPetition == int(save):
                    r = StatusPetition(NoPetition=int(save), StatusPetition=status, Date=i.Date, Date2=i.Date2,
                                       Internship_id=i.Internship_id, studentG5_id=i.studentG5_id, send=i.send)
                    r.save()

                    o = accept(No_accept=num + 1, accept_status=status, Date=Date, StatusPetition_id=int(save))
                    o.save()

        return render(request, 'group5/form1department2.html', context)
    else:
        return render(request, 'group5/error.html')


def table5_waitPettition(request):
    if getUserType(request) != '0':
        state = StatusPetition.objects.all()
        stu = Student.objects.all()
        Pro = UserProfile.objects.all()
        acc = accept.objects.all()
        context = {'state': state, 'stu': stu, 'Pro': Pro}

        save = request.GET.get('Submit2', '')
        status = request.GET.get('status', '')

        now = datetime.datetime.now()
        Date = now.strftime("%Y-%m-%d")

        acc2 = accept.objects.all().aggregate(Max('No_accept'))
        num = acc2.values()
        num = num[0]
        if num == None:
            num = 0;

        if empty(save) == False:
            for i in state:
                if i.NoPetition == int(save):
                    r = StatusPetition(NoPetition=int(save), StatusPetition=status, Date=i.Date, Date2=i.Date2,
                                       Internship_id=i.Internship_id, studentG5_id=i.studentG5_id, send=i.send)
                    r.save()

                    o = accept(No_accept=num + 1, accept_status=status, Date=Date, StatusPetition_id=int(save))
                    o.save()

        return render(request, 'group5/form1department5.html', context)
    else:
        return render(request, 'group5/error.html')


def table_Finish(request):
    state = StatusPetition.objects.all()
    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    acc = accept.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro}

    save = request.GET.get('Submit', '')
    status = request.GET.get('status', '')

    now = datetime.datetime.now()
    Date = now.strftime("%Y-%m-%d")


    acc2 = accept.objects.all().aggregate(Max('No_accept'))
    num = acc2.values()
    num = num[0]
    if num == None:
        num = 0;

    if empty(save) == False:
        for i in state:
            if i.NoPetition == int(save):
                r = StatusPetition(NoPetition=int(save), StatusPetition=status, Date=i.Date, Date2=i.Date2,
                                   Internship_id=i.Internship_id, studentG5_id=i.studentG5_id, send=i.send)
                r.save()


                # o = accept(No_accept= num+1 ,accept_status = status,Date = Date,StatusPetition_id = int(save))
                # o.save()

    return render(request, 'group5/form1department3.html', context)


def empty(variable):
    if not variable:
        return True
    return False


def deleteForm(request, pjID):
    if request.user.is_authenticated():
        error = True
        thisuser = request.user
        currentUser = UserProfile.objects.get(user=thisuser)
        stu = Student.objects.get(userprofile_id=currentUser.id)
        stuG5 = studentG5.objects.all()
        pet = StatusPetition.objects.filter(studentG5_id=stuG5)
        # for student in pet :
        #    if student.std_id == stu.std_id:
        #        error = False
        #        break
        # if error == True:
        #    return HttpResponseRedirect(reverse('group5:status')) #redirect to index
        statuspet = StatusPetition.objects.filter(studentG5_id=stuG5)
        statuspet.delete()
        messages.add_message(request, messages.INFO, "การลบฟอร์มของโปรเจคสำเร็จ")
        return HttpResponseRedirect(reverse('group5:status'))  # redirect to index
    else:
        return render(request, 'base.html')


def printForm(request, pjID):
    thisuser = request.user
    currentUser = UserProfile.objects.get(user=thisuser)
    stu = Student.objects.get(userprofile_id=currentUser.id)
    stuG5 = studentG5.objects.all()
    stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))
    stat2 = StatusPetition.objects.all()
    Intern = Internship.objects.all()
    pet = StatusPetition.objects.filter(studentG5_id=stuG5)

    prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']

    case = request.GET.get('Submit', '')
    save = request.GET.get('Submit2', '')
    status = request.GET.get('status', '')
    #date_1 = pet.Date
    #date1,date2 = pet.Date2.split(",")
    #return HttpResponseRedirect(reverse('group5:form1new_print.html'))  # redirect to index
    date_1=time.strftime("%x")
    day,month,year = date_1.split("/")
    year = int(year)+2000+543
    date_print = day +"/"+ month+"/"+str(year)
    for item in pet:
        if item.send =="send by department":
            send ="ขอให้ภาควิชาฯ จัดส่งหนังสือขอความอนุเคราะห์ฝึกงานไปตามที่อยู่ข้างบนนี้"
        if item.send =="send by student":
            send ="ขอรับหนังสืออนุเคราะห์ฝึกงานไปยื่นด้วยตนเอง"
    #for item1 in pet:
    #    for i in Intern:

            #if  item1.Intership_id.upper() == i.name_Internship:
    #       address = Intern.name_Intership

    context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'stat': stat,'pet': pet,'date_print': date_print,'send':send,'Intern':Intern,#'address':address,
                   'prefix_name1': prefix_name1[int(currentUser.prefix_name)]}
    return render(request, 'group5/form1new_print.html', context)

def editForm(request, pjID):
    stu_id = request.GET.get('id_student', '')
    to = request.GET.get('to', '')
    stu_year = request.GET.get('stu_year', '')

    office = request.GET.get('office', '')
    address = request.GET.get('address', '')
    tel = request.GET.get('tel', '')
    fax = request.GET.get('fax', '')

    date1 = request.GET.get('date1', '')
    month1 = request.GET.get('month1', '')
    year1 = request.GET.get('year1', '')
    date2 = request.GET.get('date2', '')
    month2 = request.GET.get('month2', '')
    year2 = request.GET.get('year2', '')
    send = request.GET.get('send', '')
    Submit1 = request.GET.get('Submit', '')
    Cancel1 = request.GET.get('Cancel', '')

    prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']

    bf = str(year1) + "-" + str(month1) + "-" + str(date1)
    at = str(year2) + "-" + str(month2) + "-" + str(date2)

    thisuser = request.user
    currentUser = UserProfile.objects.get(user=thisuser)
    stu = Student.objects.get(userprofile_id=currentUser.id)
    stuG5 = studentG5.objects.all()
    stat = StatusPetition.objects.all()
    Intern = Internship.objects.all()
    for i in stat:
        if i.studentG5_id == stu.std_id:
            j = i.NoPetition

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 12)  # 12 is font size
    pdf.cell(0, 10,u'ข้าพเจ้า' + stu_year)
    pdf.ln(10)  # new line
    pdf.output("group5/exam.pdf", "F")
    state_open ='ยื่นคำร้อง'
    state_open = state_open.decode("utf-8","ignore")
    
    if(stu_year != ''):
        p = studentG5(studentID=str(stu_id), studentYear=int(stu_year))
        p.save()

        q = Internship(name_Internship=office.upper(), add_Internship=address, Tel=tel, Fax=fax)
        q.save()

        r = StatusPetition(NoPetition=j, StatusPetition=state_open, Date=bf, Date2=at, Internship_id=office.upper(),
            studentG5_id=stu_id, send=send,to=to)
        r.save()
    if Submit1 != '':
            return table_status(request)

    context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'stat': stat,
                'prefix_name1': prefix_name1[int(currentUser.prefix_name)],'Intern':Intern}
    return render(request, 'group5/form2new.html', context)
#vvvvvvvvvvvvvvv  new  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def main_dep(request):
    state= StatusPetition.objects.all()
    stu=Student.objects.all()
    Pro= UserProfile.objects.all()
    context = {'state': state,'stu': stu,'Pro': Pro}
    return render(request, 'group5/main.html', context)

def main_dep2(request):
    id = request.GET.get('id','')
    state= StatusPetition.objects.get(studentG5_id=id)

    stu=Student.objects.all()
    Pro= UserProfile.objects.all()
    context = {'state': state,'stu': stu,'Pro': Pro}
    return render(request, 'group5/main2.html', context)

def main_dep3(request):
    id = request.GET.get('id2','')
    state= StatusPetition.objects.get(studentG5_id=id)

    stu=Student.objects.get(std_id=state.studentG5_id)
    Pro= UserProfile.objects.get(id=stu.userprofile_id)
    context = {'state': state,'stu': stu,'Pro': Pro}
    return render(request, 'group5/student1.html', context)













#---------------------------------------------new aom-----------------------------------------
G_sid = ''
G_status=''

def table_mainG5(request):
    if getUserType(request) != '0':
        state = StatusPetition.objects.all()
        stu = Student.objects.all()
        Pro = UserProfile.objects.all()
        stuG5 = studentG5.objects.all()
        finish = 'เสร็จสิ้น'
        finish = finish.decode("utf-8","ignore")
        context = {'state': state, 'stu': stu, 'Pro': Pro,'stuG5':stuG5,'finish':finish,}
        input =''
        input = request.GET.get('input')

        if empty(input) == False:
            input1 = input.split(':')
            sid = input1[0]
            status=''
            status=input1[1]
           # status = status.format()
            status1=''
            status1='ยื่นคำร้อง'
            status1Eng='open'
            status2='กำลังดำเนินการ'
            status3='ได้รับการอนุมัติเข้าฝึกงาน'
            status4='ผ่านการฝึกงาน'
            status5='ไม่ได้รับการอนุมัติเข้าฝึกงาน'
            status6='ไม่ผ่านการฝึกงาน'
            status7='เสร็จสิ้น'
            status = status.encode("utf-8","ignore")
            for i in state:
                if i.studentG5_id == sid:
                    #return table_status1(request,i.studentG5_id,status)
                    if status == status1 or status==status1Eng:
                        #return render(request, 'group5/error.html')
                        return table_status1(request,i.studentG5_id,status)
                    if status == status2 :
                        return table_status2(request,i.studentG5_id,status)
                    if status == status3 :
                        return table_status3(request,i.studentG5_id,status)
                    if status == status7 :
                        return table_finish(request,i.studentG5_id,status)

                    #return table_lastform(request,i.studentG5_id)
        return render(request, 'group5/mainG5.html', context)
    else:
        return render(request, 'group5/error.html')


def table_status1(request,sid,status):
    global G_sid ,G_status
    G_sid = sid
    G_status = status
    if request.user.is_authenticated():
        if getUserType(request) != '0':
            state = StatusPetition.objects.all()
            stu = Student.objects.all()
            Pro = UserProfile.objects.all()
            stuG5 = studentG5.objects.all()
            send='send by student'
            send=send.decode("utf-8",'ignore')
            context = {'state': state, 'stu': stu, 'Pro': Pro,'sid':sid,'status':status,'stuG5':stuG5,'sendbyStudent':send,}
            return render(request, 'group5/status1.html', context)
        else:
            return render(request, 'group5/error.html')
def table_ChangeStatus(request):
    global G_status,G_sid
    sid=G_sid
    status = request.GET.get('input')
    state = StatusPetition.objects.all()
    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    stuG5 = studentG5.objects.all()
    dateShow = Date.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro,'sid':sid,'status':status,'stuG5':stuG5}

    if request.method == 'GET':
        if empty(status)==False:

            send='send by student'
            send=send.encode("utf-8",'ignore')
            for i in state :
                if i.studentG5_id == sid :

                   # return HttpResponseRedirect('/group5/mainG5/')
                    #return render(request, 'group5/error.html')
                    st = StatusPetition.objects.get(studentG5_id = sid) #เปลี่ยนภาษาาาาาาาาาาาาาาาาาาาา
                    st.StatusPetition = status
                    #st=StatusPetition(studentG5_id = sid , StatusPetition=status1)
                    st.save()
                    #return render(request, 'group5/error.html')
                    if i.send =='send by student':
                        #return render(request, 'group5/error.html')
                        date = request.GET.get('date')
                       # date=datetime.strptime(date, '%d-%m-%Y')
                        dateSave = Date()
                        dateSave = Date(studentID = sid,DateEnd =date)
                        dateSave.save()

              #  new_upload.image_estimate.save(imagefile.name,imagefile)

                        #return render(request, 'group5/error.html')
                    return HttpResponseRedirect('/group5/mainG5/')

def table_status2(request,sid,status):
    global G_sid ,G_status
    G_sid = sid
    G_status = status
    if request.user.is_authenticated():
        if getUserType(request) != '0':
            state = StatusPetition.objects.all()
            stu = Student.objects.all()
            Pro = UserProfile.objects.all()
            stuG5 = studentG5.objects.all()
            date = Date.objects.all()
            context = {'state': state, 'stu': stu, 'Pro': Pro,'sid':sid,'status':status,'stuG5':stuG5,'date':date,}
            return render(request, 'group5/status2.html', context)
        else:

            return render(request, 'group5/error.html')

def table_ChangeStatus2(request):
    global G_status,G_sid
    sid=G_sid
    status = request.GET.get('input2')
    state = StatusPetition.objects.all()
    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    stuG5 = studentG5.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro,'sid':sid,'status':status,'stuG5':stuG5}
    if empty(status)==False:
        status = status.encode("utf-8","ignore")
        for i in state :
            if i.studentG5_id == sid :
                st = StatusPetition.objects.get(studentG5_id = sid)
                if status == 'ได้รับการอนุมัติเข้าฝึกงาน':

                        #st = StatusPetition.objects.get(studentG5_id = sid)
                    st.StatusPetition = status
                        #st=StatusPetition(studentG5_id = sid , StatusPetition=status1)
                    st.save()
                    return HttpResponseRedirect('/group5/mainG5/')
                if status == 'ไม่ได้รับการอนุมัติเข้าฝึกงาน':
                    st.StatusPetition = status
                    st.save()
                   # st.delete()
                    return HttpResponseRedirect('/group5/mainG5/')


        #if status == 'ไม่ได้รับกรอนุมัติเข้าฝึกงาน':

        #return HttpResponseRedirect('/group5/mainG5/')

def table_status3(request,sid,status):
    global G_sid , G_state
    G_sid=sid

    if request.user.is_authenticated():
        if getUserType(request) != '0':
            estimate = Estimate.objects.all()
            state = StatusPetition.objects.all()
            stu = Student.objects.all()
            Pro = UserProfile.objects.all()
            acc = accept.objects.all()
            stuG5 = studentG5.objects.all()
            form = PictureForm()
            return render_to_response("group5/estimate.html", {'estimate': estimate,
                                                              'form':form,'state':state,'stu':stu ,'stuG5':stuG5 ,'Pro' : Pro,'sid' : sid,'status':status,}, RequestContext(request))
        else:
            return render(request, 'group5/error.html')

def table_finish(request,sid,status):
    global G_sid ,G_status
    G_sid = sid
    if request.user.is_authenticated():
        if getUserType(request) != '0':
            estimate = Estimate.objects.all()
            state = StatusPetition.objects.all()
            stu = Student.objects.all()
            Pro = UserProfile.objects.all()
            stuG5 = studentG5.objects.all()
            context = {'state': state, 'stu': stu, 'Pro': Pro,'sid':sid,'status':status,'stuG5':stuG5,'estimate':estimate,}
            return render(request, 'group5/StudentData.html', context)
        else:
            return render(request, 'group5/error.html')

def upload(request):
        global G_sid
        sid = G_sid
        state = StatusPetition.objects.all()
        for i in state:
            if i.studentG5_id == sid :
                st = StatusPetition.objects.get(studentG5_id = sid)
                st.StatusPetition = 'เสร็จสิ้น'
                st.save()

        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
                imagefile = form.cleaned_data['image_estimate']
                imagefile2 = form.cleaned_data['image_time']
                new_upload = Estimate()
                new_upload = Estimate(studentID = sid)
                new_upload.image_estimate.save(imagefile.name,imagefile)
                new_upload.image_time.save(imagefile2.name,imagefile2)
                new_upload.save()
        return HttpResponseRedirect('/group5/mainG5/')

class PictureForm(forms.Form):
    image_estimate = forms.ImageField(label= 'แบบประเมิณ')
    image_time = forms.ImageField(label= 'บัญชีเวลา')

def search(request):
    id = request.GET.get('id','')
    state= StatusPetition.objects.get(studentG5_id=id)

    stu=Student.objects.all()
    Pro= UserProfile.objects.all()
    context = {'state': state,'stu': stu,'Pro': Pro}
    return render(request, 'group5/main2.html', context)

def edit(request):
    edit = request.GET.get('edit')


def form1(request):
    state = StatusPetition.objects.all()
    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    stuG5 = studentG5.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro,'stuG5':stuG5}
    return render(request, 'group5/form1.html')

def accept_trainee_print(request):
    return render(request, 'group5/accept_trainee_print.html')

def form2(request):
    return render(request, 'group5/form2.html')

def reporting(request):
    return render(request, 'group5/reporting_trainee_print.html')