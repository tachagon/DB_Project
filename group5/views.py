#-*- coding: utf-8 -*-
# !/usr/bin/env python

from django.shortcuts import render, render_to_response
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
import time

createdDate = datetime.now()

# count1 =0

def getUserType(request):
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user=user)
        return userprofile.type
    except:
        return 'admin'

def table_status(request):          # เป็นฟังก์ชั่นที่จะส่งค่าต่างๆไปยัง หน้า status.html
    if getUserType(request) == '0':         # ถ้าเป็น User
        date = Date.objects.all()
        dateShow = ''
        thisuser = request.user
        currentUser = UserProfile.objects.get(user=thisuser)
        stu = Student.objects.get(userprofile_id=currentUser.id)    # ดึงข้อมูลจากตาราง Student โดยดึงจาก CurrentUser.id ซึ่งจะเป็น ลำดับของนักศึกษาที่ทำการลงทะเบียน
        stuG5 = studentG5.objects.all()                             # ดึงข้อมูลจากตาราง studentG5
        pet = StatusPetition.objects.filter(studentG5_id=stuG5)     # ดึงข้อมูลจากตาราง StatusPetition

        name_month =['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']    # เดือนไทย


        for i in date:                                              # for สำหรับ ตาราง วันที่ที่ต้องมารับเอกสาร ของนักศึกษาทุกคน
            if i.studentID == stu.std_id:                           # เลือกนักศึกษาที่ login เข้าระบบมา ดูได้จาก CurrentUser.id ซึ่งจะเป็น ลำดับของนักศึกษาที่ทำการลงทะเบียน
                dateShow = i.DateEnd                                # ให้ dateShow รับค่าวันที่ต้องมารับเอกสาร
                year1, month1, day1 = str(i.DateEnd).split("-")                         # ทำการ split ค่าวันที่พิมพ์แบบคำร้อง ออกมา
                year1 = int(year1)  + 543                                               # ทำให้เป็น พ.ศ.
                date_end = str(day1) + ' '+ name_month[int(month1)-1] + ' ' +str(year1) # นำเอาวัน เดือน ปี ให้อยู่ในรูปแบบ "02 ก.ค. 2558"
            else:
                date_end =""

        for item in pet:                                            # for สำหรับ ตาราง StatusPetition
            if item.studentG5_id == stu.std_id:                     # เลือกนักศึกษาที่ login เข้าระบบมา ดูได้จาก CurrentUser.id ซึ่งจะเป็น ลำดับของนักศึกษาที่ทำการลงทะเบียน
                year1, month1, day1 = str(item.created_at).split("-")                   # ทำการ split ค่าวันที่พิมพ์แบบคำร้อง ออกมา
                year1 = int(year1)  + 543                                               # ทำให้เป็น พ.ศ.
                createdat = str(day1[:2]) + ' '+ name_month[int(month1)-1] + ' ' +str(year1)    # นำเอาวัน เดือน ปี ให้อยู่ในรูปแบบ "02 ก.ค. 2558"

        context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'pet': pet, 'dateShow': dateShow,'date_end':date_end,'createdat':createdat, }
        return render(request, 'group5/status.html', context)       # จะเรียกหน้า .html แล้วส่งค่า context ไปยังหน้านั้นด้วย
    else:                                                           # ถ้าเป็น admin
        return render(request, 'group5/error.html')                 # จะเรียกหน้า .html


def table_company(request):
    com = Internship.objects.all()
    context = {'com': com}
    return render(request, 'group5/company.html', context)


def table_addpet(request):
    if getUserType(request) == '0':
        stu_id = request.GET.get('id_student', '')                  # รับค่า id_student มาจาก form1new.html
        to = request.GET.get('to', '')                              # รับค่า to มาจาก form1new.html
        stu_year = request.GET.get('stu_year', '')                  # รับค่า stu_year มาจาก form1new.html

        office = request.GET.get('office', '')                      # รับค่า office มาจาก form1new.html
        address = request.GET.get('address', '')                    # รับค่า address มาจาก form1new.html
        tel = request.GET.get('tel', '')                            # รับค่า tel มาจาก form1new.html
        fax = request.GET.get('fax', '')                            # รับค่า fax มาจาก form1new.html

        Date_since      = request.GET.get('Date_since','')          # รับค่า Date_since มาจาก form1new.html
        Date_until      = request.GET.get('Date_until','')          # รับค่า Date_until มาจาก form1new.html

        send = request.GET.get('send', '')                          # รับค่า send มาจาก form1new.html ตรงปุ่มกด
        Submit1 = request.GET.get('Submit', '')                     # รับค่า Submit มาจาก form1new.html
        created_at = datetime.now()                                 # ดึงค่าวันที่ ที่ได้ทำการสร้างฟอร์ม
        global createdDate
        createdDate = created_at
        updated_at = datetime.now()

        prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']            # คำนำหน้าชื่อ

        bf = Date_since                                             # ส่งค่า Date_since ไปให้ bf
        at = Date_until                                             # ส่งค่า Date_until ไปให้ at

        thisuser = request.user                                     # รับค่า user
        currentUser = UserProfile.objects.get(user=thisuser)        # ดึงตาราง UserProfile โดยดูจากค่า User
        stu = Student.objects.get(userprofile_id=currentUser.id)    # ดึงข้อมูลจากตาราง Student โดยดึงจาก CurrentUser.id ซึ่งจะเป็น ลำดับของนักศึกษาที่ทำการลงทะเบียน
        stuG5 = studentG5.objects.all()                             # ดึงข้อมูลจากตาราง studentG5
        stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))    # ดึงข้อมูลจากตาราง StatusPetition
        pet = StatusPetition.objects.filter(studentG5_id=stuG5)             # ดึงข้อมูลจากตาราง StatusPetition โดยจะดึงจากข้อมูลที่มี id = studentG5
        j = stat.values()
        j = j[0]
        if j == None:
            j = 0

        state_open = 'ยื่นคำร้อง'                                     # ให้ status แรกเมื่อทำการส่งแบบฟอร์มเป็น 'ยื่นคำร้อง'
        state_open = state_open.decode("utf-8", "ignore")
        count1 = 0
        if stu_year != '':                                          # ถ้าข้อมูลใน stu_year มี ก็คือ มีการส่งแบบฟอร์มมา
            if len(StatusPetition.objects.filter(studentG5_id=stu_id)) == 0:    # ถ้า id นั้นๆ ไม่มีข้อมูลในตาราง StatusPetition
                p = studentG5(studentID=stu_id, studentYear=stu_year)           # นำข้อมูล stu_id , stu_year ใส่ลงในตาราง studentG5
                p.save()

                q = Internship(name_Internship=office.upper(), add_Internship=address, Tel=tel, Fax=fax)        # นำข้อมูล office,address,tel,fax ใส่ลงในตาราง Intership
                q.save()

                office = office.upper()
                if count1 == 0:
                    r = StatusPetition(NoPetition=j + 1, StatusPetition=state_open, Date=bf, Date2=at,          # ใส่ข้อมูลต่างๆ ลงในตาราง StatusPetition
                                       Internship_id=office,
                                       studentG5_id=stu_id, send=send, to=to, updated_at=updated_at,
                                       created_at=created_at)
                    r.save()
                count1 = 2

        for item in pet:                        # for สำหรับ ตาราง StatusPetition
            if item.studentG5_id == stu.std_id: # เลือก id student ที่ login เข้าระบบมา
                check = str(item.Date)          # ส่งค่า Date ไปให้ check
            else:
                check = 'NULL'                  # ส่งค่า 'NULL' ไปให้ check

        # ถ้ามีการกดปุ่ม "บันทึก" จะเปลี่ยนหน้าไปยังหน้า status
        if Submit1 != '':                       # ถ้ามีการกด Submit(กดส่งแบบฟอร์ม)
            return table_status(request)        # จะให้แสดงหน้า status.html
        context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'stat': stat,'check':check,
                   'prefix_name1': prefix_name1[int(currentUser.prefix_name)]}
        return render(request, 'group5/form1new.html', context)     # จะเรียกหน้า .html แล้วส่งค่า context ไปยังหน้านั้นด้วย
    else:                                                           # ถ้าเป็น admin
        return render(request, 'group5/error.html')                 # จะเรียกหน้า .html

def empty(variable):
    if not variable:
        return True
    return False

def printForm(request):
    pjID = request.GET.get('id', '')
    thisuser = request.user                                     # รับค่า user
    currentUser = UserProfile.objects.get(user=thisuser)        # ดึงตาราง UserProfile โดยดูจากค่า User
    stu = Student.objects.get(userprofile_id=currentUser.id)    # ดึงข้อมูลจากตาราง Student โดยดึงจาก CurrentUser.id ซึ่งจะเป็น ลำดับของนักศึกษาที่ทำการลงทะเบียน
    stuG5 = studentG5.objects.all()                             # ดึงข้อมูลจากตาราง studentG5
    stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))    # ดึงข้อมูลจากตาราง StatusPetition
    pet = StatusPetition.objects.filter(studentG5_id=stuG5)             # ดึงข้อมูลจากตาราง StatusPetition โดยจะดึงจากข้อมูลที่มี id = studentG5
    Intern = Internship.objects.all()                                   # ดึงข้อมูลจากตาราง Internship

    #prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    #name_month =['มกราคม','กพ','มีค','เมย','พค','มิย','กค','สค','กย','ตค','พย','ธค']




    date_1 = time.strftime("%x")
    month,day, year = date_1.split("/")
    year = int(year) + 2000 + 543
   # print 'month :' + month
    #print 'int mouth-1 :' +str(int(month)-1)
    #print str(name_month[int(month)-1])
    #date_print = day + " " + str(name_month[int(month)-1]) + " " + str(year)
    #print "stu.std_id :"+str(stu.std_id)

    for item in pet:
        if item.studentG5_id == stu.std_id:
            id_student = stu.std_id[:2]+'-'+ stu.std_id[2:-1] +'-'+stu.std_id[-1:]

            date1 = item.Date
            date2 = item.Date2

            """
            year1, month1, day1 = str(item.Date).split("-")
            year1 = int(year1) + 543
            date_since = str(day1) + ' '+ name_month[int(month1)-1] + ' ' +str(year1)


            year2, month2, day2 = str(item.Date2).split("-")
            year2 = int(year2)+ 543
            date_until = str(day2) + ' '+ name_month[int(month2)-1] + ' ' +str(year2)
            """

        if item.send == "send by department":
            send = "- ขอให้ภาควิชาฯ จัดส่งหนังสือขอความอนุเคราะห์ฝึกงานไปตามที่อยู่ข้างบนนี้"
        if item.send == "send by student":
            send = "- ขอรับหนังสืออนุเคราะห์ฝึกงานไปยื่นด้วยตนเอง"

    context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'stat': stat, 'pet': pet,
               'date_print': date_1, 'send': send, 'Intern': Intern,'date_since':date1,'date_until':date2,'id_student':id_student,
               }
    return render(request, 'group5/form1new_print.html', context)

def printForm_ALL(request):
    pjID = request.GET.get('id', '')
    stuG5 = studentG5.objects.all()
    stu = Student.objects.get(std_id=pjID)
    currentUser = UserProfile.objects.get(user=int(stu.userprofile_id)+1)

    stat = StatusPetition.objects.all().aggregate(Max('NoPetition'))
    Intern = Internship.objects.all()
    pet = StatusPetition.objects.filter(studentG5_id=stuG5)

    #วันที่ ที่ทำการพิมพ์แบบฟอร์ม
    date_1 = time.strftime("%x")
    month,day, year = date_1.split("/")
    year = int(year) + 2000 + 543

    for item in pet:
        if item.studentG5_id == pjID:
            id_student = pjID[:2]+'-'+ pjID[2:-1] +'-'+pjID[-1:]            # ปรับรูปแบบของ id student
            date1 = item.Date
            date2 = item.Date2
        if item.send == "send by department":                               #ถ้าค่าของsend มีค่าเท่ากับ "send by department"
            send = "- ขอให้ภาควิชาฯ จัดส่งหนังสือขอความอนุเคราะห์ฝึกงานไปตามที่อยู่ข้างบนนี้"   #จะทำการส่งข้อความไปยังหน้า form1new_print.html
        if item.send == "send by student":                                  #ถ้าค่าของsend มีค่าเท่ากับ "send by student"
            send = "- ขอรับหนังสืออนุเคราะห์ฝึกงานไปยื่นด้วยตนเอง"              #จะทำการส่งข้อความไปยังหน้า form1new_print.html

    context = { 'currentUser': currentUser, 'stu': stu,'stuG5': stuG5, 'stat': stat, 'pet': pet,
               'date_print': date_1, 'send': send, 'Intern': Intern,'date_since':date1,'date_until':date2,'id_student':id_student,
               }
    return render(request, 'group5/form1new_print.html', context)           #จะเรียกหน้า .html แล้วส่งค่า context ไปยังหน้านั้นด้วย


def editForm(request, pjID):
    stu_id = request.GET.get('id_student', '')
    to = request.GET.get('to', '')
    stu_year = request.GET.get('stu_year', '')

    office = request.GET.get('office', '')
    address = request.GET.get('address', '')
    tel = request.GET.get('tel', '')
    fax = request.GET.get('fax', '')

    Date_since      = request.GET.get('Date_since','')
    Date_until      = request.GET.get('Date_until','')

    send = request.GET.get('send', '')
    Submit1 = request.GET.get('Submit', '')
    Cancel1 = request.GET.get('Cancel', '')
    global createdDate
    created_at = createdDate
    updated_at = datetime.now()
    prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']

    bf = Date_since
    at = Date_until

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
    pdf.cell(0, 10, u'ข้าพเจ้า' + stu_year)
    pdf.ln(10)  # new line
    pdf.output("group5/exam.pdf", "F")
    state_open = 'ยื่นคำร้อง'
    state_open = state_open.decode("utf-8", "ignore")

    if (stu_year != ''):
        p = studentG5(studentID=str(stu_id), studentYear=int(stu_year))
        p.save()

        q = Internship(name_Internship=office.upper(), add_Internship=address, Tel=tel, Fax=fax)
        q.save()

        r = StatusPetition(NoPetition=j, StatusPetition=state_open, Date=bf, Date2=at, Internship_id=office.upper(),
                           studentG5_id=stu_id, send=send, to=to, created_at=created_at, updated_at=updated_at)
        r.save()
    if Submit1 != '':
        return table_status(request)

    context = {'currentUser': currentUser, 'stu': stu, 'stuG5': stuG5, 'stat': stat,
               'prefix_name1': prefix_name1[int(currentUser.prefix_name)], 'Intern': Intern}
    return render(request, 'group5/form2new.html', context)


# vvvvvvvvvvvvvvv  new  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def main_dep(request):
    state = StatusPetition.objects.all()
    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro}
    return render(request, 'group5/main.html', context)


def main_dep2(request):
    id = request.GET.get('id', '')
    state = StatusPetition.objects.get(studentG5_id=id)

    stu = Student.objects.all()
    Pro = UserProfile.objects.all()
    context = {'state': state, 'stu': stu, 'Pro': Pro}
    return render(request, 'group5/main2.html', context)


def main_dep3(request):
    id = request.GET.get('id2', '')
    state = StatusPetition.objects.get(studentG5_id=id)

    stu = Student.objects.get(std_id=state.studentG5_id)
    Pro = UserProfile.objects.get(id=stu.userprofile_id)
    context = {'state': state, 'stu': stu, 'Pro': Pro}
    return render(request, 'group5/student1.html', context)

# ---------------------------------------------new aom-----------------------------------------

G_sid = ''
G_status = ''
#function mainG5 for mainG5.html
def table_mainG5(request):
    if getUserType(request) != '0':                                 #if user type don't Student
        state = StatusPetition.objects.all()                        #create objects StatusPetition[from group5:models.py]
        stu = Student.objects.all()                                 #create objects Student [from login:models.py]
        Pro = UserProfile.objects.all()                             #create objects UserProfile [from login:models.py]
        stuG5 = studentG5.objects.all()                             #create objects StudentG5 [from group5:models.py]
        finish = 'เสร็จสิ้น'
        finish = finish.decode("utf-8", "ignore")
        context = {'state': state, 'stu': stu, 'Pro': Pro, 'stuG5': stuG5, 'finish': finish, }  #context for html
        input = ''                                                  #create variable input
        input = request.GET.get('input')                            #get data from mainG5.html in id ='input'

        if empty(input) == False:                                   #recieved data from input
            input1 = input.split(':')                               #split input [student id : status]
            sid = input1[0]                                         #sid = student id [from input]
            status = ''
            status = input1[1]                                      #status = status[from input]
            status1 = 'ยื่นคำร้อง'
            status2 = 'กำลังดำเนินการ'
            status3 = 'ได้รับการอนุมัติเข้าฝึกงาน'
            status4 = 'ไม่ได้รับการอนุมัติเข้าฝึกงาน'
            status5 = 'เสร็จสิ้น'
            status6 = 'พิมพ์เอกสาร'
            status = status.encode("utf-8", "ignore")               #encode status
            for i in state:
                if i.studentG5_id == sid:
                    if status == status1 :                          #if status = 'ยื่นคำร้อง' then call table_status1 function
                        return table_status1(request, i.studentG5_id, status)
                    if status == status2:                           #if status = 'กำลังดำเนินการ' then call table_status2 function
                        return table_status2(request, i.studentG5_id, status)
                    if status == status3:                           #if status = 'ได้รับการอนุมัติเข้าฝึกงาน' then call table_status3 function
                        return table_status3(request, i.studentG5_id, status)
                    if status == status5:                           #if status = 'เสร็จสิ้น' then call table_finish function
                        return table_finish(request, i.studentG5_id, status)
                    if status == status6:                           #if status = 'พิมพ์เอกสาร' then call table_printAll function
                        return table_printAll(request, i.studentG5_id, status)

        return render(request, 'group5/mainG5.html', context)       #render mainG5.html
    else:                                                           #usertpye is student['0']
        return render(request, 'group5/error.html')                 #render error.html
#function for change date format
def dateFormat(date):
    dateFormat=date                                                 #create dateFormat from date
    if dateFormat[1] == '1':                                        #dateFormat[1]=month if dateFormat[1]='1' then month = 'มกราคม'
         dateFormat[1] = "มกราคม"
    elif dateFormat[1] == '2':                                      #if dateFormat[1]='2' then month = 'กุมภาพันธ์'
        dateFormat[1] = "กุมภาพันธ์"
    elif dateFormat[1] == '3':                                      #if dateFormat[1]='3' then month = 'มีนาคม'
        dateFormat[1] = "มีนาคม"
    elif dateFormat[1] == '4':                                      #if dateFormat[1]='4' then month = 'เมษายน'
        dateFormat[1] = "เมษายน"
    elif dateFormat[1] == '5':                                      #if dateFormat[1]='5' then month = 'พฤษภาคม'
        dateFormat[1] = "พฤษภาคม"
    elif dateFormat[1] == '6':                                      #if dateFormat[1]='6' then month = 'มิถุนายน'
        dateFormat[1] = "มิถุนายน"
    elif dateFormat[1] == '7':                                      #if dateFormat[1]='6' then month = 'กรกฎาคม'
        dateFormat[1] = "กรกฎาคม"
    elif dateFormat[1] == '8':                                      #if dateFormat[1]='6' then month = 'สิงหาคม'
        dateFormat[1] = "สิงหาคม"
    elif dateFormat[1] == '9':                                      #if dateFormat[1]='6' then month = 'กันยายน'
        dateFormat[1] = "กันยายน"
    elif dateFormat[1] == '10':                                     #if dateFormat[1]='6' then month = 'ตุลาคม'
        dateFormat[1] = "ตุลาคม"
    elif dateFormat[1] == '11':                                     #if dateFormat[1]='6' then month = 'พฤศจิกายน'
        dateFormat[1] = "พฤศจิกายน"
    elif dateFormat[1] == '12':                                     #if dateFormat[1]='6' then month = 'ธันวาคม'
        dateFormat[1] = "ธันวาคม"

    dateFormat[2] = int(dateFormat[2])+543                          # change Year A.D -> B.E
    dateFormat[2]=str(dateFormat[2])

    return dateFormat                                               #return dateFormat

#function table_status1 for status1.html
def table_status1(request, sid, status):
    global G_sid, G_status                                          #global variable
    G_sid = sid                                                     #insert value to G_sid[studentID]
    G_status = status                                               #insert value to G_statustudentID]
    if request.user.is_authenticated():                             #for user is authenticated
        if getUserType(request) != '0':                             #if user type don't Student
            state = StatusPetition.objects.all()                    #create objects StatusPetition[from group5:models.py]
            stu = Student.objects.all()                             #create objects Student [from login:models.py]
            Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
            stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
            d1 = StatusPetition.objects.get(studentG5_id=sid)       #d1 get objects StatusPetition at Student_id=sid
            d=d1.updated_at                                         #insert value d from updated time of d1
            dateFormat1 =  "%s %s %s" % (d.day, d.month, d.year)    #dateFormat1 get data Date from d and keep in format 'day month year'
            dateFormat1 = dateFormat1.split(' ')                    #split ' ' from dateFormat1
            dFormat=dateFormat(dateFormat1)                         #call function dateFormat(dateFormate1)
            dFormat = "วันที่ %s เดือน %s พ.ศ.%s " %(dFormat[0],dFormat[1],dFormat[2])              #dFormat = dateFormat was Change

            dStart=d1.Date                                          #insert value dStart from Date of d1
            dateStart1="%s %s %s" % (dStart.day, dStart.month, dStart.year)                       #dateStart1 get data Date from dStart and keep in format 'day month year'
            dateStart1 = dateStart1.split(' ')                      #split ' ' from dateStart1
            dStart=dateFormat(dateStart1)                           #call function dateFormat(dateStart1)
            dStart = "วันที่ %s เดือน %s พ.ศ.%s " %(dStart[0],dStart[1],dStart[2])  #dStart = dStart was Change

            dEnd=d1.Date2                                           #insert value dEnd from Date2 of d1
            dateEnd1="%s %s %s" % (dEnd.day, dEnd.month, dEnd.year) #dateEnd1 get data Date from dEnd and keep in format 'day month year'
            dateEnd1 = dateEnd1.split(' ')                          #split ' ' from dateEnd1
            dEnd=dateFormat(dateEnd1)                               #call function dateFormat(dateEnd1)
            dEnd = "วันที่ %s เดือน %s พ.ศ.%s " %(dEnd[0],dEnd[1],dEnd[2]) #dEnd = dEnd  changed format

            hour = int(d.hour)+7                                    #GMT+7 Bangkok
            if int(hour) > 24 :                                     #re value if > 24
                hour = int(hout)-24
            hour = str(hour)
            if int(d.minute) < 10 :                                 #insert '0' before string_minute when minute < 10
                minute = "0%s" %(d.minute)
            else:
                minute = "%s" %(d.minute)
            timeFormat = "%s:%s:%s" %(hour,minute,d.second)         #show time formatin H:M:S
            context = {'state': state, 'stu': stu, 'Pro': Pro, 'sid': sid, 'status': status, 'stuG5': stuG5,'dFormat':dFormat,'tFormat':timeFormat,
                      'dStart':dStart,'dEnd':dEnd,}                 #context for html
            return render(request, 'group5/status1.html', context)  #render sttus1.html
        else:                                                       #usertype is student
            return render(request, 'group5/error.html')             #render error.html


def table_ChangeStatus(request):
    global G_status, G_sid                                          #global variable
    sid = G_sid                                                     #sid = G_sid
    status = request.GET.get('input')                               #get status from status`.html in id ='input'
    state = StatusPetition.objects.all()                            #create objects state from StatusPetition
    if request.method == 'GET':                                     #if request.method == 'GET'
        if empty(status) == False:                                  #recieved status from input
            status = status.encode("utf-8", "ignore")               #encode status
            for i in state:                                         #loop for each objects in state
                if i.studentG5_id == sid:                           #if state.studentG5_id = sid
                    st = StatusPetition.objects.get(studentG5_id=sid)  #create objects st from StatusPetition at studentG5_id=sid[this Student]
                    st.StatusPetition = status                      #insert StatusPetition = status
                    st.save()                                       #save table
                    if i.send == 'send by student':                 #if send format ='send by student'
                        date = request.GET.get('date')              #get date from status.html in id = 'date'
                        dateSave = Date()                           #create objects Date()[group5:models.py]
                        dateSave = Date(studentID=sid, DateEnd=date)#insert value objects dateSave in field studentID and DateEnd
                        dateSave.save()                             #save objects dateSave
                    return HttpResponseRedirect('/group5/mainG5/')  #redirect to /group5/mainG5/


def table_status2(request, sid, status):
    global G_sid, G_status                                          #global variable
    G_sid = sid                                                     #insert value to G_sid[studentID]
    G_status = status                                               #insert value to G_statustudentID]
    if request.user.is_authenticated():                             #for user is authenticated
        if getUserType(request) != '0':                             #if user type don't Student
            state = StatusPetition.objects.all()                    #create objects StatusPetition[from group5:models.py]
            stu = Student.objects.all()                             #create objects Student [from login:models.py]
            Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
            stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
            d1 = StatusPetition.objects.get(studentG5_id=sid)       #d1 get objects StatusPetition at Student_id=sid
            d=d1.updated_at                                         #insert value d from updated time of d1
            dateFormat1 =  "%s %s %s" % (d.day, d.month, d.year)    #dateFormat1 get data Date from d and keep in format 'day month year'
            dateFormat1 = dateFormat1.split(' ')                    #split ' ' from dateFormat1
            dFormat=dateFormat(dateFormat1)                         #call function dateFormat(dateFormate1)
            dFormat = "วันที่ %s เดือน %s พ.ศ.%s " %(dFormat[0],dFormat[1],dFormat[2])              #dFormat = dateFormat was Change

            dStart=d1.Date                                          #insert value dStart from Date of d1
            dateStart1="%s %s %s" % (dStart.day, dStart.month, dStart.year)                       #dateStart1 get data Date from dStart and keep in format 'day month year'
            dateStart1 = dateStart1.split(' ')                      #split ' ' from dateStart1
            dStart=dateFormat(dateStart1)                           #call function dateFormat(dateStart1)
            dStart = "วันที่ %s เดือน %s พ.ศ.%s " %(dStart[0],dStart[1],dStart[2])  #dStart = dStart was Change

            dEnd=d1.Date2                                           #insert value dEnd from Date2 of d1
            dateEnd1="%s %s %s" % (dEnd.day, dEnd.month, dEnd.year) #dateEnd1 get data Date from dEnd and keep in format 'day month year'
            dateEnd1 = dateEnd1.split(' ')                          #split ' ' from dateEnd1
            dEnd=dateFormat(dateEnd1)                               #call function dateFormat(dateEnd1)
            dEnd = "วันที่ %s เดือน %s พ.ศ.%s " %(dEnd[0],dEnd[1],dEnd[2]) #dEnd = dEnd  changed format

            hour = int(d.hour)+7                                    #GMT+7 Bangkok
            if int(hour) > 24 :                                     #re value if > 24
                hour = int(hout)-24
            hour = str(hour)
            if int(d.minute) < 10 :                                 #insert '0' before string_minute when minute < 10
                minute = "0%s" %(d.minute)
            else:
                minute = "%s" %(d.minute)
            timeFormat = "%s:%s:%s" %(hour,minute,d.second)         #show time formatin H:M:S
            context = {'state': state, 'stu': stu, 'Pro': Pro, 'sid': sid, 'status': status, 'stuG5': stuG5,'dFormat':dFormat,'tFormat':timeFormat,
                      'dStart':dStart,'dEnd':dEnd,}                 #context for html
            return render(request, 'group5/status2.html', context)  #render status2.html
        else:                                                       #user type = student

            return render(request, 'group5/error.html')             #render error.html

def table_ChangeStatus2(request):
    global G_status, G_sid                                          #global variable
    sid = G_sid                                                     #sid = G_sid
    status = request.GET.get('input2')                              #get status from status2.html in id ='input2'
    state = StatusPetition.objects.all()                            #create objects state from StatusPetition
    stu = Student.objects.all()                             #create objects Student [from login:models.py]
    Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
    stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
    if empty(status) == False:
        status = status.encode("utf-8", "ignore")                   #encode status
        for i in state:                                             #loop for each objects in state
            if i.studentG5_id == sid:                              #if state.studentG5_id = sid
              #  return render(request, 'group5/error.html')
                st = StatusPetition.objects.get(studentG5_id=sid)   #create objects st from StatusPetition at studentG5_id=sid[this Student]
                if status == 'ได้รับการอนุมัติเข้าฝึกงาน':              #if status = 'ได้รับการอนุมัติเข้าฝึกงาน' then save status in table
                    #return HttpResponseRedirect('/group5/printDocument/')
                    st.StatusPetition = status
                    st.save()
                    return HttpResponseRedirect('/group5/printDocument/')   #Redirect to /group5/printDocument/
                if status == 'ไม่ได้รับการอนุมัติเข้าฝึกงาน':           #if status = 'ไม่ได้รับการอนุมัติเข้าฝึกงาน' then save status in table
                    st.StatusPetition = status
                    st.save()
                    return HttpResponseRedirect('/group5/mainG5/')          #Redirect to /group5/mainG5/

def table_status3(request, sid, status):
    global G_sid, G_status                                          #global variable
    G_sid = sid                                                     #insert value to G_sid[studentID]
    G_status = status                                               #insert value to G_statustudentID]
    if request.user.is_authenticated():                             #for user is authenticated
        if getUserType(request) != '0':                             #if user type don't Student
            estimate = Estimate.objects.all()                       #create objects Estimate[from group5:models.py]
            state = StatusPetition.objects.all()                    #create objects StatusPetition[from group5:models.py]
            stu = Student.objects.all()                             #create objects Student [from login:models.py]
            Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
            stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
            d1 = StatusPetition.objects.get(studentG5_id=sid)       #d1 get objects StatusPetition at Student_id=sid
            d=d1.updated_at                                         #insert value d from updated time of d1
            dateFormat1 =  "%s %s %s" % (d.day, d.month, d.year)    #dateFormat1 get data Date from d and keep in format 'day month year'
            dateFormat1 = dateFormat1.split(' ')                    #split ' ' from dateFormat1
            dFormat=dateFormat(dateFormat1)                         #call function dateFormat(dateFormate1)
            dFormat = "วันที่ %s เดือน %s พ.ศ.%s " %(dFormat[0],dFormat[1],dFormat[2])              #dFormat = dateFormat was Change

            dStart=d1.Date                                          #insert value dStart from Date of d1
            dateStart1="%s %s %s" % (dStart.day, dStart.month, dStart.year)                       #dateStart1 get data Date from dStart and keep in format 'day month year'
            dateStart1 = dateStart1.split(' ')                      #split ' ' from dateStart1
            dStart=dateFormat(dateStart1)                           #call function dateFormat(dateStart1)
            dStart = "วันที่ %s เดือน %s พ.ศ.%s " %(dStart[0],dStart[1],dStart[2])  #dStart = dStart was Change

            dEnd=d1.Date2                                           #insert value dEnd from Date2 of d1
            dateEnd1="%s %s %s" % (dEnd.day, dEnd.month, dEnd.year) #dateEnd1 get data Date from dEnd and keep in format 'day month year'
            dateEnd1 = dateEnd1.split(' ')                          #split ' ' from dateEnd1
            dEnd=dateFormat(dateEnd1)                               #call function dateFormat(dateEnd1)
            dEnd = "วันที่ %s เดือน %s พ.ศ.%s " %(dEnd[0],dEnd[1],dEnd[2]) #dEnd = dEnd  changed format

            hour = int(d.hour)+7                                    #GMT+7 Bangkok
            if int(hour) > 24 :                                     #re value if > 24
                hour = int(hout)-24
            hour = str(hour)
            if int(d.minute) < 10 :                                 #insert '0' before string_minute when minute < 10
                minute = "0%s" %(d.minute)
            else:
                minute = "%s" %(d.minute)
            timeFormat = "%s:%s:%s" %(hour,minute,d.second)         #show time formatin H:M:S
            form = PictureForm()                                    #from=Pictureform
            return render_to_response("group5/estimate.html", {'estimate': estimate,
                                                               'form': form, 'state': state, 'stu': stu, 'stuG5': stuG5,
                                                               'dFormat':dFormat,'tFormat':timeFormat,
                                                               'Pro': Pro, 'sid': sid, 'status': status, 'dStart':dStart,'dEnd':dEnd,},
                                      RequestContext(request))      #render to estimate.html
        else:                                                       #user typr = student
            return render(request, 'group5/error.html')             #render error.html


def table_finish(request, sid, status):
    global G_sid, G_status                                          #global variable
    G_sid = sid                                                     #insert value to G_sid[studentID]
    G_status = status                                               #insert value to G_statustudentID]
    if request.user.is_authenticated():                             #for user is authenticated
        if getUserType(request) != '0':                             #if user type don't Student
            estimate = Estimate.objects.all()                       #create objects Estimate[from group5:models.py]
            state = StatusPetition.objects.all()                    #create objects StatusPetition[from group5:models.py]
            stu = Student.objects.all()                             #create objects Student [from login:models.py]
            Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
            stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
            d1 = StatusPetition.objects.get(studentG5_id=sid)       #d1 get objects StatusPetition at Student_id=sid
            d=d1.updated_at                                         #insert value d from updated time of d1
            dateFormat1 =  "%s %s %s" % (d.day, d.month, d.year)    #dateFormat1 get data Date from d and keep in format 'day month year'
            dateFormat1 = dateFormat1.split(' ')                    #split ' ' from dateFormat1
            dFormat=dateFormat(dateFormat1)                         #call function dateFormat(dateFormate1)
            dFormat = "วันที่ %s เดือน %s พ.ศ.%s " %(dFormat[0],dFormat[1],dFormat[2])              #dFormat = dateFormat was Change

            dStart=d1.Date                                          #insert value dStart from Date of d1
            dateStart1="%s %s %s" % (dStart.day, dStart.month, dStart.year)                       #dateStart1 get data Date from dStart and keep in format 'day month year'
            dateStart1 = dateStart1.split(' ')                      #split ' ' from dateStart1
            dStart=dateFormat(dateStart1)                           #call function dateFormat(dateStart1)
            dStart = "วันที่ %s เดือน %s พ.ศ.%s " %(dStart[0],dStart[1],dStart[2])  #dStart = dStart was Change

            dEnd=d1.Date2                                           #insert value dEnd from Date2 of d1
            dateEnd1="%s %s %s" % (dEnd.day, dEnd.month, dEnd.year) #dateEnd1 get data Date from dEnd and keep in format 'day month year'
            dateEnd1 = dateEnd1.split(' ')                          #split ' ' from dateEnd1
            dEnd=dateFormat(dateEnd1)                               #call function dateFormat(dateEnd1)
            dEnd = "วันที่ %s เดือน %s พ.ศ.%s " %(dEnd[0],dEnd[1],dEnd[2]) #dEnd = dEnd  changed format

            hour = int(d.hour)+7                                    #GMT+7 Bangkok
            if int(hour) > 24 :                                     #re value if > 24
                hour = int(hout)-24
            hour = str(hour)
            if int(d.minute) < 10 :                                 #insert '0' before string_minute when minute < 10
                minute = "0%s" %(d.minute)
            else:
                minute = "%s" %(d.minute)
            timeFormat = "%s:%s:%s" %(hour,minute,d.second)         #show time format in H:M:S
            context = {'state': state, 'stu': stu, 'Pro': Pro, 'sid': sid, 'status': status, 'stuG5': stuG5,'dFormat':dFormat,'tFormat':timeFormat,
                       'dStart':dStart,'dEnd':dEnd,
                       'estimate': estimate, }                     #context for html
            return render(request, 'group5/StudentData.html', context) # render StudentData.html
        else:                                                       #user type = student
            return render(request, 'group5/error.html')             #render error.html


def table_printDoc(request):
    global G_sid, G_status                                          #global variable
    sid = G_sid                                                     #insert value to G_sid[studentID]
    #G_status = status                                               #insert value to G_statustudentID]
    if request.user.is_authenticated():                             #for user is authenticated
        if getUserType(request) != '0':                             #if user type don't Student
            estimate = Estimate.objects.all()                       #create objects Estimate[from group5:models.py]
            state = StatusPetition.objects.all()                    #create objects StatusPetition[from group5:models.py]
            stu = Student.objects.all()                             #create objects Student [from login:models.py]
            Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
            stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
            return render_to_response("group5/printDoc.html", {'estimate': estimate,
                                                                'state': state, 'stu': stu, 'stuG5': stuG5,
                                                               'Pro': Pro, 'sid': sid,},
                                      RequestContext(request))      #render PrintDoc.html
        else:                                                       #user type = student
            return render(request, 'group5/error.html')             #render error.html


def table_printAll(request, sid, status):
    global G_sid, G_status                                          #global variable
    G_sid = sid                                                     #insert value to G_sid[studentID]
    G_status = status                                               #insert value to G_statustudentID]
    if request.user.is_authenticated():                             #for user is authenticated
        if getUserType(request) != '0':                             #if user type don't Student
            estimate = Estimate.objects.all()                       #create objects Estimate[from group5:models.py]
            state = StatusPetition.objects.all()                    #create objects StatusPetition[from group5:models.py]
            stu = Student.objects.all()                             #create objects Student [from login:models.py]
            Pro = UserProfile.objects.all()                         #create objects UserProfile [from login:models.py]
            stuG5 = studentG5.objects.all()                         #create objects StudentG5 [from group5:models.py]
            context = {'state': state, 'stu': stu, 'Pro': Pro, 'sid': sid, 'status': status, 'stuG5': stuG5,} #contex for html
            return render(request, 'group5/printAll.html', context) #render to printAll.html
        else:                                                       #user type = student
            return render(request, 'group5/error.html')             #render error.html

def upload(request):
    global G_sid, G_status                                          #global variable
    sid = G_sid                                                     #insert value to G_sid[studentID]
    #G_status = status                                               #insert value to G_statustudentID]
    state = StatusPetition.objects.all()                            #create objects StatusPetition[from group5:models.py]
    for i in state:                                                 #loop for each objects in state
        if i.studentG5_id == sid:                                   #if state.studentG5_id = sid
            st = StatusPetition.objects.get(studentG5_id=sid)       #create objects st from StatusPetition at studentG5_id=sid[this Student]
            st.StatusPetition = 'เสร็จสิ้น'                            #insert StatusPetition = 'เสร็จสิ้น'
            st.save()                                               #save table StatusPetition
    form = PictureForm(request.POST, request.FILES)                 #create objects form from PictureForm(request.POST, request.FILES)
    if form.is_valid():                                             #check form is valid
        imagefile = form.cleaned_data['image_estimate']             #cleaned data from id = 'image_estimate'
        imagefile2 = form.cleaned_data['image_time']                #cleaned data from id = 'image_time'
        new_upload = Estimate()                                     #create objects Estimate to new_upload
        new_upload = Estimate(studentID=sid)                        #insert value studentId
        new_upload.image_estimate.save(imagefile.name, imagefile)   #insert image_estimate
        new_upload.image_time.save(imagefile2.name, imagefile2)     #insert image_time
        new_upload.save()                                           #save table Estimate
    return HttpResponseRedirect('/group5/mainG5/')                  #redirect /group5/mainG%/


#class PictureForm for create form to estimate.html
class PictureForm(forms.Form):
    image_estimate = forms.ImageField(label='เพิ่มแบบประเมิณ')       #create ImageField of image_estimate
    image_time = forms.ImageField(label='เพิ่มบัญชีเวลา')             #create ImageField of image_time

#function search for search box in mainG5/mainG5_2.html
def search(request):
    id = request.GET.get('id', '')                                  #get studentID from id ='id'
    have_student = False                                            #create variable have_student  for check studentId is valid
    stu = Student.objects.all()                                     #create objects Student[from login:models.py]
    Pro = UserProfile.objects.all()                                 #create objects UserProfile[from login:models.py]
    stateAll = StatusPetition.objects.all()                         #create objects StatusPetition[from group5:models.py]
    for i in stateAll:                                              #loop for each objects in stateAll
     if i.studentG5_id==id :                                        #if state.studentG5_id = sid
        have_student= True                                          #have student [id is valid]
    if have_student==True :                                         #if have student [id is valid]
        state = StatusPetition.objects.get(studentG5_id=id)         #create objects st from StatusPetition at studentG5_id=sid[this Student]
        context = {'state': state, 'stu': stu, 'Pro': Pro,'have_student':have_student} #context for html

    else :                                                          #don't have student [id is invalid]
        context = { 'stu': stu, 'Pro': Pro,'have_student':have_student}  #context for html
    return render(request, 'group5/mainG5_2.html', context)         #render mainG5_2.html

def form1(request):
    id = request.GET.get('id', '')
    date = request.GET.get('date', '')
    state = StatusPetition.objects.get(studentG5_id=id)
    stu = Student.objects.get(std_id = id)
    Pro = UserProfile.objects.get(id=stu.userprofile_id)
    stuG5 = studentG5.objects.get(studentID=id)
    
    now = datetime.now()
    M = int(now.strftime("%m"))
    Y = str(int(now.strftime("%Y"))+543)
    num = ['๐','๑','๒','๓','๔','๕','๖','๗','๘','๙']
    a = ''
    for i in range(0, len(Y)):
        for j in range(0, 10):
            if str(j)==Y[i]:
                a += num[j]
                
    D1 = str(int(state.Date.strftime("%d")))
    M1 = int(state.Date.strftime("%m"))
    Y1 = str(int(state.Date.strftime("%Y"))+543)
    a1 = ''
    for i in range(0, len(D1)):
        for j in range(0, 10):
            if str(j)==D1[i]:
                a1 += num[j]
    
    a2 = ''
    for i in range(0, len(Y1)):
        for j in range(0, 10):
            if str(j)==Y1[i]:
                a2 += num[j]

    D2 = str(int(state.Date2.strftime("%d")))
    M2 = int(state.Date2.strftime("%m"))
    Y2 = str(int(state.Date2.strftime("%Y"))+543)
    a3 = ''
    for i in range(0, len(D2)):
        for j in range(0, 10):
            if str(j)==D2[i]:
                a3 += num[j]
    
    a4 = ''
    for i in range(0, len(Y2)):
        for j in range(0, 10):
            if str(j)==Y2[i]:
                a4 += num[j]
    
    a5 = ''
    for i in range(0, len(id)):
        for j in range(0, 10):
            if str(j)==id[i]:
                a5 += num[j]
    
    a6 = ''
    for j in range(0, 10):
        if str(j)==str(stuG5.studentYear):
            a6 += num[j]
    
    prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    Pre_n = prefix_name1[int(Pro.prefix_name)]
    name_month =['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    context = {'state': state, 'stu': stu, 'Pro': Pro, 'stuG5': stuG5,'M':name_month[M-1],'Y':a,'date':date,'D1':a1,'M1':name_month[M1-1],'Y1':a2,'D2':a3,'M2':name_month[M2-1],'Y2':a4,'Pre_n':Pre_n,'id_th':a5,'SY':a6}
    return render(request, 'group5/form1.html',context)


def accept_trainee_print(request):
    return render(request, 'group5/accept_trainee_print.html')


def form2(request):
    id = request.GET.get('id', '')
    date = request.GET.get('date', '')
    state = StatusPetition.objects.get(studentG5_id=id)
    stu = Student.objects.get(std_id = id)
    Pro = UserProfile.objects.get(id=stu.userprofile_id)
    stuG5 = studentG5.objects.get(studentID=id)
    
    now = datetime.now()
    M = int(now.strftime("%m"))
    Y = str(int(now.strftime("%Y"))+543)
    num = ['๐','๑','๒','๓','๔','๕','๖','๗','๘','๙']
    a = ''
    for i in range(0, len(Y)):
        for j in range(0, 10):
            if str(j)==Y[i]:
                a += num[j]
                
    D1 = str(int(state.Date.strftime("%d")))
    M1 = int(state.Date.strftime("%m"))
    Y1 = str(int(state.Date.strftime("%Y"))+543)
    a1 = ''
    for i in range(0, len(D1)):
        for j in range(0, 10):
            if str(j)==D1[i]:
                a1 += num[j]
    
    a2 = ''
    for i in range(0, len(Y1)):
        for j in range(0, 10):
            if str(j)==Y1[i]:
                a2 += num[j]

    D2 = str(int(state.Date2.strftime("%d")))
    M2 = int(state.Date2.strftime("%m"))
    Y2 = str(int(state.Date2.strftime("%Y"))+543)
    a3 = ''
    for i in range(0, len(D2)):
        for j in range(0, 10):
            if str(j)==D2[i]:
                a3 += num[j]
    
    a4 = ''
    for i in range(0, len(Y2)):
        for j in range(0, 10):
            if str(j)==Y2[i]:
                a4 += num[j]
    
    a5 = ''
    for i in range(0, len(id)):
        for j in range(0, 10):
            if str(j)==id[i]:
                a5 += num[j]
    
    a6 = ''
    for j in range(0, 10):
        if str(j)==str(stuG5.studentYear):
            a6 += num[j]
    
    prefix_name1 = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    Pre_n = prefix_name1[int(Pro.prefix_name)]
    name_month =['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    context = {'state': state, 'stu': stu, 'Pro': Pro, 'stuG5': stuG5,'M':name_month[M-1],'Y':a,'date':date,'D1':a1,'M1':name_month[M1-1],'Y1':a2,'D2':a3,'M2':name_month[M2-1],'Y2':a4,'Pre_n':Pre_n,'id_th':a5,'SY':a6}
    return render(request, 'group5/form2.html',context)


def reporting(request):
    return render(request, 'group5/reporting_trainee_print.html')

