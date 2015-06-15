#!/usr/bin/env python
#-*- coding: utf-8 -*-
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
    

