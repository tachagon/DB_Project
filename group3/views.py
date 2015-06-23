#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from group3.models import *
from django.http import HttpResponse
from fpdf import FPDF
# Create your views here.
def prof2lang_index(request):
    template = 'group3/prof2lang_index.html'    # get template
    teachList = Teach.objects.all()     # get all Prof2Lang objects

    return render(
        request,
        template,
        {'teachList': teachList}
    )

def prof2lang_view(request, profID):
    template = 'group3/prof2lang_view.html'             # get view template
    try:
        teachObj = Teach.objects.get(pk = int(profID))  # get a Teach object
        context = {'teachObj': teachObj}
    except: # can't get a Teach object
        context = {}

    return render(
        request,
        template,
        context
    )

def prof2lang_add(request, option = '0'):
    template = 'group3/prof2lang_add.html'
    # get all Prof2Lang objects
    prof2langObj = Prof2Lang.objects.all().order_by('shortName')
    # get all Subject objects
    subjectObj = Subject.objects.all().order_by('subjectID')

    # option 0 is get prof2lang_add web page
    if request.method == 'GET' and option == '0':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
        }
    # option 1 is add Prof2Lang object success
    elif option == '1':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
            'addProfSuccess': True,
        }
    # option 2 is add Prof2Lang object not success
    elif option == '2':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
            'addProfError': True,
        }
    # option 3 is add Subject object success
    elif option == '3':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSubjectSuccess': True
        }
    # option 4 is add Subject object not success
    elif option == '4':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSubjectError': True
        }
    # option 5 is add Section object success
    elif option == '5':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSectionSuccess': True
        }
    # option 6 is add Section object not success
    elif option == '6':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSectionError': True
        }
    else:
        return prof2lang_index(request)



    return render(
        request,
        template,
        context
    )

# This function for get data and create new Prof2Lang object.
def addProf(request):
    if request.method == 'POST':
        # get data from html template
        profID      = request.POST['profID']
        firstName   = request.POST['firstName']
        lastName    = request.POST['lastName']
        shortName   = request.POST['shortName']
        tell        = request.POST['tell']
        email       = request.POST['email']
        sahakornAccount = request.POST['sahakornAccount']
        department  = request.POST['department']
        faculty     = request.POST['faculty']

        try:
            # create new Prof2Lang object
            newProf = Prof2Lang(
                profID = profID,
                firstName = firstName,
                lastName = lastName,
                shortName = shortName,
                tell = tell,
                email = email,
                sahakornAccount = sahakornAccount,
                department = department,
                faculty = faculty
            )
            # save new Prof2Lang object into database
            newProf.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['1']))
        except Exception, e:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['2']))

# This function for get data and create new Subject object.
def addSubject(request):
    if request.method == 'POST':
        try:
            # get data from HTML template
            subjectID = request.POST['subjectID']
            subjectName = request.POST['subjectName']

            # create new Subject object
            newSubject = Subject(
                subjectID = subjectID,
                subjectName = subjectName
            )
            # save new Subject object into database
            newSubject.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['3']))
        except:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['4']))

# This function for get data and create new Section object
def addSection(request):
    if request.method == 'POST':
        try:
            # get data from HTML template
            section = request.POST['section']
            subject = request.POST['subject']
            classroom = request.POST['classroom']
            startTime_hour = request.POST['startTime_hour']
            startTime_minute = request.POST['startTime_minute']
            endTime_hour = request.POST['endTime_hour']
            endTime_minute = request.POST['endTime_minute']
            date = request.POST['date']

            # create startTime
            startTime = startTime_hour + ":" + startTime_minute + ":" + "00"
            # create endTime
            endTime = endTime_hour + ":" + endTime_minute + ":" + "00"
            # get Subject object that selected
            subjectObj = Subject.objects.get(subjectID = subject)

            # create new Section object
            newSection = Section(
                section = section,
                subject = subjectObj,
                classroom = classroom,
                startTime = startTime,
                endTime = endTime,
                date = date
            )
            # save new Section object into database
            newSection.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['5']))
        except:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['6']))

def genpdf(request, profID):
    teachObj = Teach.objects.get(pk= int(profID)) 
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    
    pdf.image('group3/trarachakarn.png',20,20,20)
    pdf.ln(25)
    
    proID = ''
    firstname = ''
    lastname = ''
    shortname = ''
    department = ''
    faculty = ''
    sahakornAccount = ''
    tell = ''
    email = ''
    
    try:
        proID = teachObj.prof.profID
    except:
        proID = 'None'

    try:
        firstname = teachObj.prof.firstName
    except:
        firstname = 'None'
 
    try:
        lastname = teachObj.prof.lastName
    except:
        lastname = 'None'

    try:
        shortname  = teachObj.prof.shortName
    except:
        shortname = 'None'

    try:
        department = teachObj.prof.department
    except:
        department = 'None'
    
    try:
        faculty = teachObj.prof.faculty
    except:
        faculty = 'None'

    try:
        sahakornAccount = teachObj.prof.sahakornAccount
    except:
        sahakornAccount = 'None'

    try:
        tell = teachObj.prof.tell
    except:
        tell = 'None'

    try:
        email = teachObj.prof.email
    except:
        email = 'None'
        
    pdf.add_font('Kinnari-Bold', '', 'Kinnari-Bold.ttf', uni=True)
    pdf.set_font('Kinnari-Bold', '', 18)
    pdf.cell(0, 10, u'                         บันทึกข้อความ')
    pdf.ln(10)
    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 12)
    pdf.cell(0, 10, u'         ส่วนราชการ ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์ คณะวิศวกรรมศาสตร์  โทร. ๘๕๑๘')
    pdf.line(46,52,180,52)
    pdf.ln(8)
    pdf.cell(0, 10, u'         ที่  วฟ     /๒๕๕๘                                        วันที่  ')
    pdf.line(30,60,180,60)
    pdf.ln(8)
    pdf.cell(0, 10, u'         เรื่อง การจัดการเรียนการสอนสำหรับนักศึกษาโครงการพิเศษ(สองภาษา) ')
    pdf.line(30,68,180,68)
    pdf.ln(8)
    pdf.cell(0, 10, u'         เรียน หัวหน้าภาควิชา ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                     ตามที่ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  ได้ขอรับบริการจัดการเรียนการ')
    pdf.ln(8)
    pdf.cell(0, 10, u'         สอนจากท่านในรายวิชา                                                      สำหรับนักศึกษา')
    pdf.ln(8)
    pdf.cell(0, 10, u'         โครงการพิเศษ (สองภาษา)  ภาคเรียนที่            นั้น')
    pdf.ln(8)
    pdf.cell(0, 10, u'                    ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  ขอให้ท่านยืนยันการจัดการเรียนการสอนใน')
    pdf.ln(8)
    pdf.cell(0, 10, u'         รายวิชาดังกล่าว ตามแบบฟอร์มด้านล่าง พร้อมตารางสอนและใบเบิกค่าสอนของอาจารย์ผู้สอนและ')
    pdf.ln(8)
    pdf.cell(0, 10, u'         ส่งคืนกลับภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์  เพื่อจะได้ดำเนินการในส่วนที่เกี่ยวข้องต่อไป')
    pdf.ln(8)
    pdf.cell(0, 10, u'                        จึงเรียนมาเพื่อโปรดทราบ')
    pdf.ln(20)
    pdf.cell(0, 10, u'                                                  (ดร.นภดล   วิวัชรโกเศศ)')
    pdf.ln(8)
    pdf.cell(0, 10, u'                                              หัวหน้าภาควิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    pdf.ln(14)
    pdf.cell(0, 10, u'            ..................................................................................................................................................')
    pdf.ln(8)
    pdf.cell(0, 10, u'         ชื่อผู้สอน.................................................................... รหัสผู้สอน.................................ภาควิชา ')
    pdf.ln(8)
    pdf.cell(0, 10, u'         คณะ.......................................................................รหัสวิชา...........................................ชื่อวิชา ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                        ตอนเรียน           วัน              เวลา  ')
    pdf.ln(8)
    pdf.cell(0, 10, u'         ได้จัดการเรียนการสอนเป็น ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                    ภาษาอังกฤษ  ')
    pdf.rect(37, 210, 3, 3)
    pdf.ln(8)
    pdf.cell(0, 10, u'                    ภาษาไทย')
    pdf.rect(37, 218, 3, 3)
    pdf.ln(8)
    pdf.cell(0, 10, u'                                            ลงชื่อ......................................อาจารย์ผู้สอน ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                                            (..............................................) ')
    pdf.ln(8)
    pdf.cell(0, 10, u'                                            ลงชื่อ......................................')
    pdf.ln(8)
    pdf.cell(0, 10, u'                                            (..............................................) ')
    pdf.ln(8)   
    pdf.cell(0, 10, u'                                            หัวหน้าภาควิชา............................................')
    pdf.ln(8)

    pdf.cell(0, 10, u'' + proID)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + firstname + '   '+ lastname)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + shortname)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + department)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + faculty)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + sahakornAccount)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + tell)
    pdf.ln(8)
    pdf.cell(0, 10, u'' + email)          
    pdf.ln(20)
    pdf.cell(0, 10, u'' + teachObj.subject.subjectID)          
    pdf.ln(20)
    pdf.cell(0, 10, u'' + teachObj.subject.subjectName)          
    pdf.ln(20)
    pdf.cell(0, 10, u'' + teachObj.section.section)          
    pdf.ln(20)
    pdf.cell(0, 10, u'' + str(teachObj.section.startTime))          
    pdf.ln(20)
    pdf.cell(0, 10, u'' + teachObj.section.date)          
    pdf.ln(20)
    pdf.output("group3/uni.pdf", 'F')
    
    # next path will open pdf file in new tab on browser.
    with open('group3/uni.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=uni.pdf'
        return response
    pdf.closed
    
def drawAttr(pdf ,start, end, attr=False):
    Y = [start, end]
    if attr:
        pdf.line(10,Y[0], 288, Y[0])
    pdf.line(10,Y[1], 288, Y[1])
    
    pdf.line(10, Y[0], 10, Y[1])
    pdf.line(18, Y[0], 18, Y[1])
    pdf.line(63, Y[0], 63, Y[1])
    pdf.line(71, Y[0], 71, Y[1])
    
    pdf.line(88, Y[0], 88, Y[1])
    pdf.line(131,Y[0], 131, Y[1])
    pdf.line(144, Y[0], 144, Y[1])
    
    pdf.line(150,Y[0], 150, Y[1])
    pdf.line(168,Y[0], 168, Y[1])
    pdf.line(180,Y[0], 180, Y[1])
    pdf.line(200,Y[0], 200, Y[1])

    pdf.line(243,Y[0], 243, Y[1])
    pdf.line(263,Y[0], 263, Y[1])
    pdf.line(288,Y[0], 288, Y[1])

def drawAttr2(pdf, start, end, attr=False):
    Y = [start, end]
    if attr:
        pdf.line(10, Y[0], 198, Y[0])
    pdf.line(10, Y[0], 10, Y[1])
    pdf.line(15, Y[0], 15, Y[1])
    pdf.line(25, Y[0], 25, Y[1])
    pdf.line(35, Y[0], 35, Y[1])
    
    pdf.line(45, Y[0], 45, Y[1])
    pdf.line(55,Y[0], 55, Y[1])
    pdf.line(65, Y[0], 65, Y[1])

def genallpdf(request):
    allTeach = Teach.objects.all()
    allsection = Section.objects.all()
    
    ListSec = []
    for sec in allsection:
        eachSec = []
        for teach in allTeach:
            if teach.section == sec:
                eachSec.append(teach)
        ListSec.append(eachSec)
        
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()
    
    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 8)
        
    ganY = [10, 18]
    drawAttr(pdf, ganY[0], ganY[1], True)
    pdf.cell(0, ganY[0], u'ลำดับ              ชื่อ-สกุล                    ตัวย่อ    รหัสวิชา                ชื่อวิชา                      ตอนเรียน  วัน       เวลา       ห้องเรียน  เบอร์โทรศัพท์                   Email                  บ-ช สหกรณ์      หมายเหตุ    ')
    pdf.ln(4) # width:298 height:210
    #drawAttr(pdf, ganY[0]+ 32, ganY[1] + 32, False)
    
    cnt_no = 0
    cnt_line = 0
    for sec in ListSec:
        cnt_no += 1
        no = str(cnt_no)
        # write no.
        for Prof in sec:
            cnt_line += 1
            try:
                first_name = Prof.prof.firstName
                last_name = Prof.prof.lastName
                full_name = first_name + '  ' + last_name
            except:
                full_name = 'None'
                
            try:
                shortname = Prof.prof.shortName
            except:
                shortname = 'None'
                
            try:
                subjectID = Prof.subject.subjectID
            except:
                subjectID = 'None'
                
            try:
                subject = Prof.subject.subjectName
            except:
                subject = 'None'
                
            try:
                section = Prof.section.section
            except:
                section = " "
                
            try:
                day = Prof.section.date
            except:
                day = ' '
            
            try:
                starttime = Prof.section.startTime
            except:
                starttime = 'None'
                
            try:
                room = Prof.section.classroom
            except:
                room = 'None'
                
            try:
                phone_num = Prof.prof.tell
            except:
                phone_num = 'None'
            
            try:
                email = Prof.prof.email
            except:
                email = 'None'
            
            try:
                sahakorn = Prof.prof.sahakornAccount
            except:
                sahakorn = 'None'
                
            pdf.cell(8, 18, no)
            pdf.cell(45, 18, full_name)
            pdf.cell(8, 18, shortname)
            pdf.cell(17, 18, subjectID)
            pdf.cell(45, 18, subject)
            pdf.cell(12, 18, section)
            pdf.cell(7, 18, day)
            pdf.cell(17, 18, str(starttime))
            pdf.cell(12, 18, room)
            pdf.cell(19, 18, phone_num)
            pdf.cell(43, 18, email)
            pdf.cell(29, 18, sahakorn)

            pdf.ln(8)
            if cnt_line % 16 == 0:
                drawAttr(pdf, ganY[0]+ (cnt_line*8), ganY[1] + (cnt_line*8), True)
            else:
                drawAttr(pdf, ganY[0]+ (cnt_line*8), ganY[1] + (cnt_line*8))
            no = ''
    
    pdf.ln(8)
    pdf.cell(230, 18, '')
    pdf.cell(230, 18, u'ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์ ')
    pdf.ln(8)
    pdf.cell(240, 18, '')
    pdf.cell(240, 18, u'คณะวิศวกรรมศาสตร์ ')
    pdf.ln(8)
    pdf.output("group3/allTeach.pdf", 'F')
    
    with open('group3/allTeach.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=allTeach.pdf'
        return response
    pdf.closed
    
def gen_single_text(pdf, position, text=""): # use to create a single text for only a line.
    pdf.cell(position, 18, u'')
    pdf.cell(position, 18, u'' + text)
    pdf.ln(8)

def hourpdf(request):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    ganY = [10, 18]  # line bettwen collumn.
    
    pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
    pdf.set_font('Kinnari', '', 12)
    
    gen_single_text(pdf, 60, u'ใบลงเวลาทำงานลูกจ้างชั่วคราวรายชั่วโมง')
    gen_single_text(pdf, 60, u'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเนือ')
    gen_single_text(pdf, 60, u'ชื่อ')
    
    pdf.ln(8)
    pdf.cell(0, 18, u'วัน      วันที่ เดือน ปี          เวลาทำงาน          รวมชั่วโมง         ลายมือชื่อ          หมายเหตุ')
    drawAttr2(pdf, ganY[0], ganY[1], True)
    
    gen_single_text(pdf, 70, u'รวมจำนวนชั่วโมง ' + u'ชั่วโมง')
    gen_single_text(pdf, 70, u'อัตรา 45.45 บาท ชั่วโมง')
    gen_single_text(pdf, 70, u'รวมเป็นเงินทั้งสิ้น' + u'บาท')
    gen_single_text(pdf, 70, u'(                   )')
    gen_single_text(pdf, 70, u'ได้ตรวจสอบถูกต้องแล้ว')
    gen_single_text(pdf, 70, u'ลงชื่อ.......................................................')
    gen_single_text(pdf, 70, u'(...................................................)')
    
    pdf.output("group3/hour.pdf", 'F')
    
    with open('group3/hour.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=hour.pdf'
        return response
    pdf.closed