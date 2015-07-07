#-*- coding: utf-8 -*-
from django.shortcuts import render
from group4.models import *
from django.http import HttpResponse,HttpResponseRedirect
from checkWeb import *
from django.core.urlresolvers import reverse
from fpdf import FPDF
from django.utils import timezone
# Create your views here.

def adminIndexPage(request):
    template = 'group4/adminIndexPage.html'    # get template

    #Tab 1
    olddate = Olddate.objects.all().order_by('id')
    dataWithdrawCure = WithdrawCure.objects.all().order_by('id')[:5]
    dataWithdrawStudy = WithdrawStudy.objects.all().order_by('id')[:5]

    #Tab 2
    check_update()
    getlen = DataFromWeb.objects.all()
    # get all DataFromWeb objects
    result = []
    notfound = []
    dataFromWebList = []
    if request.method == "POST":
        seach = request.POST['seach']
        seach = str(seach)
        for each in getlen:
            if each.account_id == seach:
                result.append(each)
            else:
                notfound.append(each)
    if len(result) == 0 and len(notfound) == 0 :
        dataFromWebList = DataFromWeb.objects.all().order_by('-id')[:len(getlen)]
        result = []
    elif len(result) >0:
        dataFromWebList = []
        notfound = []
    elif len(result) > 0 and len(notfound) > 0 :
        dataFromWebList = []
        notfound   = []

    #Tab 3
    edit = EditPresident.objects.all()
    data = edit[0]
    return render(
        request,
        template,
        {   'olddate'           : olddate,
            'dataWithdrawCure'  : dataWithdrawCure,
            'dataWithdrawStudy' : dataWithdrawStudy,
            'dataFromWebList'   : dataFromWebList,
            'result'            : result,
            'notfound'          : notfound,
            'dataFromWebList_edit': data}
    )

def userPage(request):
    template = 'group4/userPage.html'    # get template
    objUser = request.user
    objUsers = UserProfile.objects.get(user = objUser)
    withdrawCure = WithdrawCure.objects.all().order_by('-id')
    print "44444444444"
    if (len(withdrawCure)>0):
        print "555555555555555555"
        withdrawCureList = []
        for i in withdrawCure:
            if i.user==objUsers:
                withdrawCureList.append(i)
    try:
        eachUserDataList = DataFromWeb.objects.all()
        datalist = []
        for i in eachUserDataList:
            if i.user==objUsers:
                datalist.append(i)

        return render(
            request,
            template,
            {'eachUserDataList' :   datalist,
             'objUsers'         :   objUsers,
             'withdrawCureList' :   withdrawCureList
             }
        )
    except:
        return render(
            request,
            template,
            {'objUsers': objUsers,
             'withdrawCureList' :   withdrawCureList
             }
        )


def commit_data(request,presidentid):
    objUsers = EditPresident.objects.get(id=int(presidentid))
    if request.method == 'POST':
        presidentName   = request.POST['presidentName']         # 2. firstName
        position        = request.POST['position']          # 3. lastName
        objUsers.presidentName = presidentName
        objUsers.position     = position
        objUsers.save()
    return HttpResponseRedirect(reverse("group4:adminIndexPage"))


def commitWithdrawCure(request):
    if request.method == "POST":
        objUser         = request.user
        objUsers        = UserProfile.objects.get(user=objUser)
        account_id      = request.POST["account_id"]
        checkList       = request.POST.getlist("check")
        print checkList
        selfW = '0'
        spouseW = '0'
        fatherW = '0'
        motherW = '0'
        childW1 = '0'
        childW2 = '0'
        orderchildW1 = '0'
        orderchildW2 = '0'
        for i in checkList:
            if i == '1':
                selfW = '1'
            elif i == '2':
                spouseW = '1'
            elif i == '3':
                fatherW = '1'
            elif i == '4':
                motherW = '1'
            elif i == '5':
                childW1 = '1'
                orderchildW1 = request.POST["orderchildW1"]
            elif i == '6':
                childW2 = '1'
                orderchildW2 = request.POST["orderchildW2"]
        disease         = request.POST["disease"]
        hospital        = request.POST["hospital"]
        hospitalOf      = request.POST["hospitalOf"]
        startDate       = request.POST["startDate"]
        stopDate        = request.POST["stopDate"]
        value           = request.POST["value"]
        valueChar       = request.POST["valueChar"]
        numBill         = request.POST["numBill"]
        dataWithdraw    = WithdrawCure(
            user        = objUsers,
            account_id  = account_id,
            selfW = selfW,
            spouseW = spouseW,
            fatherW = fatherW,
            motherW = motherW,
            childW1 = childW1,
            childW2 = childW2,
            orderchildW1 = orderchildW1,
            orderchildW2 = orderchildW2,
            disease     = disease,
            hospital    = hospital,
            hospitalOf  = hospitalOf,
            startDate   = startDate,
            stopDate    = stopDate,
            value       = value,
            valueChar   = valueChar,
            numBill     = numBill,
        )
        dataWithdraw.save()
        #pdf = WithdrawCure.objects.all().order_by('id')
        #previewPDF = pdf[len(pdf)-1]

        #addpdf(previewPDF.id)

    return HttpResponseRedirect(reverse("group4:userPage"))

def addpdf(request, profID): # use to generate pdf file for lend another teacher.

    obj = WithdrawCure.objects.get(pk= int(profID))
    if obj.spouseW == '1':
        sp = Spouse.objects.get(user=obj.user)
    if obj.fatherW == '1':
        dad = Father.objects.get(user=obj.user)
    if obj.motherW == '1':
        mom = Mother.objects.get(user=obj.user)
    if obj.childW1 == '1':
        ch = Child.objects.all()
        ch1list = []
        for i in ch:
            if i.user == obj.user:
                ch1list.append(i)
        for j in ch1list:
            if obj.orderChildW1 == j.OrderF:
                ch1 = j

    if obj.childW2 == '1':
        ch = Child.objects.all()
        ch2list = []
        for i in ch:
            if i.user == obj.user:
                ch2list.append(i)
        for j in ch2list:
            if obj.orderChildW1 == j.OrderF:
                ch2 = j

    pres = EditPresident.objects.all()
    presi = pres[0]
    pdf = FPDF('P', 'mm', 'A4')    # start pdf file
    pdf.add_page()                 # begin first page.


    try:
        firstname = obj.user.firstname_th
    except:
        firstname = 'None'

    try:
        lastname = obj.user.lastname_th
    except:
        lastname = 'None'

    try:
        department = obj.user.department
    except:
        department = 'None'

    try:
        faculty = obj.user.faculty
    except:
        faculty = 'None'

    try:
        if obj.user.type=='1':
            typeu = Teacher.objects.get(userprofile=obj.user)
            typeuser = typeu.position
        elif obj.user.type=='2':
            typeu = Officer.objects.get(userprofile=obj.user)
            typeuser = typeu.position
    except:
        typeuser = 'None'

    try:
        user = obj.user
    except:
        user = 'None'

    try:
        account_id = obj.account_id
    except:
        account_id = 'None'

    try:
        disease = obj.disease
    except:
        disease = 'None'

    try:
        hospital = obj.hospital
    except:
        hospital = 'None'

    try:
        hospitalOf = obj.hospitalOf
    except:
        hospitalOf = 'None'

    try:
        startDate = obj.startDate
    except:
        startDate = 'None'

    try:
        stopDate = obj.stopDate
    except:
        stopDate = 'None'

    try:
        value = obj.value
    except:
        value = 'None'

    try:
        valueChar = obj.valueChar
    except:
        valueChar = 'None'

    try:
        numBill = obj.numBill
    except:
        numBill = 'None'

    try:
        typeWithdraw = obj.typeWithdraw
    except:
        typeWithdraw = 'None'

    pdf.line(12, 31, 198, 31)
    pdf.line(12, 31, 12, 285)
    pdf.line(12, 285, 198, 285)
    pdf.line(198, 31, 198, 285)
    pdf.line(12, 179, 198, 179)

    pdf.image('group4\A.png',145,113,6) #ก
    pdf.image('group4\B.png',140,190,6) #ข
    pdf.image('group4\C.png',27,254,6) #ค

    pdf.add_font('THSarabunNew Bold', '', 'THSarabunNew Bold.ttf', uni=True)
    pdf.set_font('THSarabunNew Bold', '', 18)
    pdf.cell(169, 10, u'                                    ใบเบิกเงินสวัสดิการเกี่ยวกับการรักษาพยาบาล     ')
    pdf.set_font('THSarabunNew Bold', '', 14)
    pdf.cell(0, 10, u'แบบ 7131')
    pdf.ln(8)
    pdf.cell(0, 10, u'                                     โปรดทำเครื่องหมาย      ลงในช่องว่าง  พร้อมทั้งกรอกข้อความให้ครบถ้วน    ')
    pdf.image('group4\son2.png',80,20,6)
    pdf.ln(16)
    pdf.add_font('THSarabunNew', '', 'THSarabunNew.ttf', uni=True)
    pdf.set_font('THSarabunNew', '', 14)
    pdf.cell(30, 10, u'     1. ข้าพเจ้า................................................................................................เลขที่บัญชีสหกรณ์ออมทรัพย์ SA-.....................................................')
    pdf.cell(115, 8, u'' + firstname + u'  ' + lastname)
    pdf.cell(20, 8, u'' + account_id)
    pdf.ln(7)
    pdf.cell(0, 10, u'        สถานะ  ข้าราชการ   ลูกจ้างประจำ   ข้าราชการบำนาญ(เปลี่ยนสถานะ และ เกษียณอายุ)   พนักงานมหาวิทยาลัย ')
    if typeuser == '0':
        pdf.image('group4\son2.png',29,43,6)
    elif typeuser == '1':
        pdf.image('group4\son2.png',49,43,6)
    elif typeuser == '2':
        pdf.image('group4\son2.png',73,43,6)
    elif typeuser == '3':
        pdf.image('group4\son2.png',145,43,6)
    pdf.ln(7)

    pdf.cell(40, 10, u'        สังกัด ภาควิชา.................................................................................................คณะ......................................................................................')
    if department == '1':
        pdf.cell(85, 8, u'วิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    if faculty == '1':
        pdf.cell(0, 8, u'วิศวกรรมศาสตร์')
    pdf.ln(7)
    pdf.cell(0, 10, u'     2. ขอเบิกเงินค่ารักษาพยาบาลของ')
    pdf.ln(7)
    pdf.cell(0, 10, u'           ตนเอง')
    if obj.selfW == '1':
        pdf.image('group4/son2.png',20,64,6)
    pdf.ln(7)
    pdf.cell(40, 10, u'           คู่สมรส  ชื่อ...............................................................................เลขประจำตัวประชาชน......................................................')
    if obj.spouseW == '1':
        pdf.image('group4\son2.png',20,71,6)
        pdf.cell(90, 8, u'' + sp.title + sp.firstname +u'  '+sp.lastname)
        pdf.cell(0, 8, u''+ sp.pid)
    pdf.ln(7)
    pdf.cell(45, 10, u'                         ที่ทำงาน......................................................................ตำแหน่ง..............................................................................')
    if obj.spouseW == '1':
        pdf.cell(70, 8, u''+ sp.office)
        pdf.cell(0, 8, u''+sp.position)
    pdf.ln(7)

    pdf.cell(40, 10, u'           บิดา      ชื่อ..............................................................................เลขประจำตัวประชาชน......................................................')
    if obj.fatherW == '1':
        pdf.image('group4\son2.png',20,85,6)
        pdf.cell(90, 8, u'' + dad.title + dad.firstname+u'  '+ dad.lastname)
        pdf.cell(0, 8, u''+ dad.pid)
    pdf.ln(7)

    pdf.cell(40, 10, u'           มารดา   ชื่อ..............................................................................เลขประจำตัวประชาชน......................................................')
    if obj.motherW == '1':
        pdf.image('group4\son2.png',20,92,6)
        pdf.cell(90, 8, u''+ mom.title + mom.firstname + u'  '+ mom.lastname)
        pdf.cell(0, 8, u''+ mom.pid)
    pdf.ln(7)

    pdf.cell(40, 10, u'           บุตร      ชื่อ..............................................................................เลขประจำตัวประชาชน......................................................')
    if obj.childW1 == '1':
        pdf.image('group4\son2.png',20,99,6)
        pdf.cell(90, 8, u''+ ch1.title + ch1.firstname +u'  '+ch1.lastname)
        pdf.cell(0, 8, u''+ch1.pid)
    pdf.ln(7)
    pdf.cell(42, 10, u'                          เกิดเมื่อ.................................................เป็นบุตรลำดับที่(ของบิดา)..................เป็นบุตรลำดับที่(ของมารดา)................... ')
    if obj.childW1 == '1':
        pdf.cell(75, 8, u'' + str(ch1.birthDate))
        pdf.cell(50, 8, u'' + str(ch1.orderF))
        pdf.cell(0, 8, u'' + str(ch1.orderM))
    pdf.ln(7)
    pdf.cell(0, 10, u'                           ยังไม่บรรลุนิติภาวะ    เป็นบุตรไร้ความสามารถ หรือเสมือนไร้ความสามารถ ')
    if obj.childW1 == '1':
        if ch1.disable=='1':
            pdf.image('group4\son2.png',71,113,6)
        year = timezone.now().year
        month = timezone.now().month
        today = timezone.now().day
        print today
        birthdate = str(ch1.birthDate).split('-')
        year = year-int(birthdate[0])
        month = month-int(birthdate[1])
        today = today-int(birthdate[2])
        if year > 20   :
             pdf.image('group4\son2.png',38,113,6)
        elif year == 20 and month > 0 :
             pdf.image('group4\son2.png',38,113,6)
        elif year == 20 and today >= 0 and month == 0:
             pdf.image('group4\son2.png',38,113,6)

    pdf.ln(7)
    pdf.cell(40, 10, u'           บุตร      ชื่อ..............................................................................เลขประจำตัวประชาชน.....................................................')
    pdf.ln(7)
    pdf.cell(42, 10, u'                          เกิดเมื่อ.................................................เป็นบุตรลำดับที่(ของบิดา)..................เป็นบุตรลำดับที่(ของมารดา)................... ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                           ยังไม่บรรลุนิติภาวะ    เป็นบุตรไร้ความสามารถ หรือเสมือนไร้ความสามารถ ')
    pdf.ln(7)

    pdf.cell(35, 10, u'         ป่วยเป็นโรค............................................................................................................................................................................................')
    pdf.cell(20, 8, u'' + disease)
    pdf.ln(7)
    pdf.cell(95, 10, u'         และได้รับการตรวจรักษาพยาบาลจาก(ชื่อสถานพยาบาล).....................................................................................................................')
    pdf.cell(20, 8, u'' + hospital)
    pdf.ln(7)
    pdf.cell(115, 10, u'         ซึ่งเป็นสถานพยาบาลของ    ของทางราชการ     เอกชน   ตั้งแต่วันที่.........................................................................................')
    pdf.cell(20, 8, u'' + str(startDate) )
    if hospitalOf == '0':
        pdf.image('group4\son2.png',55,155,6)
    elif hospitalOf == '1':
        pdf.image('group4\son2.png',85,155,6)
    pdf.ln(7)
    pdf.cell(30, 10, u'         ถึงวันที่...........................................................................................เป็นเงินรวมทั้งสิ้น.....................................................................บาท')
    pdf.cell(100, 8, u'' + str(stopDate))
    pdf.cell(20, 8, u'' + str(value))
    pdf.ln(7)
    pdf.cell(30, 10, u'         (.......................................................................................................................) ตามใบเสร็จรับเงินที่แนบ จำนวน.........................ฉบับ')
    pdf.cell(128, 8, u'' + valueChar)
    pdf.cell(20, 8, u'' + str(numBill))
    pdf.ln(14)

    pdf.cell(0, 10, u'    3. ข้าพเจ้ามีสิทธิได้รับเงินสวัสดิการเกี่ยวกับการรักษาพยาบาล ตามพระราชกฤษฎีกาเงินสวัสดิการเกี่ยวกับการรักษาพยาบาล ')
    pdf.ln(7)
    pdf.cell(0, 10, u'         ตามสิทธิ                     เฉพาะส่วนที่ขาดอยู่จากสิทธิที่ได้รับจากหน่วยงานอื่น ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                            เฉพาะส่วนที่ขาดอยู่จากสัญญาประกันภัย ')
    pdf.ln(7)

    pdf.cell(30, 10, u'       เป็นเงิน.....................................................บาท (............................................................................................................................) และ ')
    pdf.cell(55, 8, u'' + str(value))
    pdf.cell(0, 8, u'' + valueChar)
    pdf.ln(12)
    pdf.cell(0, 10, u'       (1)  ข้าพเจ้า                ไม่มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่น  ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นแต่เลือกใช้สิทธิจากทางราชการ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย  ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      เป็นผู้ใช้สิทธิเบิกค่ารักษาพยาบาลสำหรับบุตรแค่เพียงฝ่ายเดียว ')
    pdf.ln(10)


    pdf.cell(0, 10, u'       (2) ................ข้าพเจ้า     ไม่มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่น                      ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นแต่ค่ารักษาพยาบาลที่ได้รับต่ำกว่าสิทธิตามพระราชกฤษฎีกาฯ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นในฐานะเป็นผู้อาศัยสิทธิของผู้อื่น ')
    pdf.ln(7)



    pdf.add_page()

    #frame
    pdf.line(12, 15, 198, 15)
    pdf.line(12, 15, 12, 282)
    pdf.line(12, 282, 198, 282)
    pdf.line(198, 15, 198, 282)
    pdf.line(12, 80, 198, 80)
    pdf.line(12, 137, 198, 137)

    #table
    pdf.line(20, 170, 80, 170)
    pdf.line(20, 170, 20, 215)
    pdf.line(20, 215, 80, 215)
    pdf.line(80, 170, 80, 215)
    pdf.line(20, 178, 80, 178)
    pdf.line(20, 185, 80, 185)
    pdf.line(20, 193, 80, 193)
    pdf.line(20, 200, 80, 200)
    pdf.line(42, 170, 42, 200)

    pdf.image('group4\D.png',55,19,6) #ง

    pdf.image('group4\A.png',19,239,6) #A
    pdf.image('group4\B.png',19,246,6) #B
    pdf.image('group4\C.png',19,260,6) #C
    pdf.image('group4\D.png',19,267,6) #D


    pdf.add_font('THSarabunNew', '', 'THSarabunNew.ttf', uni=True)
    pdf.set_font('THSarabunNew', '', 14)
    pdf.cell(0, 10, u'')
    pdf.ln(7)
    pdf.cell(0, 10, u'     4. เสนอ อธิการบดี')
    pdf.ln(14)
    pdf.cell(0, 10, u'                      ข้าพเจ้าขอรับรองว่าข้าพเจ้ามีสิทธิเบิกค่ารักษาพยาบาลสำหรับตนเองและบุคคลในครอบครัวตามจำนวนที่ขอเบิก ซึ่งกำหนด')
    pdf.ln(7)
    pdf.cell(0, 10, u'      ไว้ในกฏหมายและข้อความข้างต้นเป็นจริงทุกประการ')
    pdf.ln(16)
    pdf.cell(0, 10, u'                                                                                       (ลงชื่อ)........................................................ผู้รับเงินสวัสดิการ')
    pdf.ln(7)
    pdf.cell(103, 10, u'                                                                                             (..........................................................)')
    pdf.cell(0, 8, u'' + firstname + u'  ' + lastname)
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                                          วันที่............เดือน..........................พ.ศ...............')
    pdf.ln(14)

    pdf.cell(0, 10, u'    5. คำอนุมัติ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                  อนุมัติให้เบิกได้')
    pdf.ln(14)
    pdf.cell(0, 10, u'                                                                       (ลงชื่อ)........................................................ ')
    pdf.ln(7)
    pdf.cell(86, 10, u'                                                                             (..........................................................)')
    pdf.cell(0, 8, u'' + presi.presidentName)
    pdf.ln(7)
    pdf.cell(90, 10, u'                                                                      ตำแหน่ง..........................................................')
    pdf.cell(0, 8, u'' + presi.position)
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                     วันที่............เดือน..........................พ.ศ............... ')
    pdf.ln(14)

    pdf.cell(0, 10, u'    6. ใบรับเงิน')
    pdf.ln(7)
    pdf.cell(100, 10, u'                 ได้รับเงินสวัสดิการเกี่ยวกับการรักษาพยาบาล จำนวน...........................................................................บาท ')
    pdf.cell(0, 8, u'' + str(value))
    pdf.ln(7)
    pdf.cell(30, 10, u'          (................................................................................................................................................)ไปถูกต้องแล้ว ')
    pdf.cell(0, 8, u'' + valueChar)
    pdf.ln(18)
    pdf.cell(40, 10, u'           วงเงินที่ได้รับ                                                                          (ลงชื่อ)......................................................ผู้รับเงิน')
    pdf.cell(0, 8, u'20,000')
    pdf.ln(7)
    pdf.cell(40, 10, u'           เบิกครั้งก่อน                                                                                 (..........................................................)    ')
    pdf.cell(78, 8, u'9,999')
    pdf.cell(0, 8, u'' + firstname + u'  ' + lastname)
    pdf.ln(7)
    pdf.cell(40, 10, u'           เบิกครั้งนี้ ')
    pdf.cell(0, 8, u'9,999')
    pdf.ln(7)
    pdf.cell(40, 10, u'           คงเหลือ                                                                               (ลงชื่อ)......................................................ผู้จ่ายเงิน ')
    pdf.cell(0, 8, u'9,999')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                                                          (..........................................................)')
    pdf.ln(7)
    pdf.cell(0, 10, u'                ....................................ผู้คุมยอดการเบิก                                     วันที่...........เดือน.........................พ.ศ...............')
    pdf.ln(22)
    pdf.cell(0, 10, u'                                                                            คำชี้แจง')
    pdf.ln(10)
    pdf.cell(0, 10, u'              ให้แนบสำเนาคำสั่งศาลที่สั่ง/พิพากษาให้เป็นบุคคลไร้ความสามารถ  หรือเสมือนไร้ความสามารถ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'              ให้มีคำชี้แจงด้วยว่ามีสิทธิเพียงใด และขาดอยู่เท่าใด กรณีที่ได้รับจากหน่วยงานอื่นเมื่อเทียบสิทธิตามพระราชกฤษฎีกาเงินสวัสดิการ')
    pdf.ln(7)
    pdf.cell(0, 10, u'               เกี่ยวกับการรักษาพยาบาลหรือขาดอยู่เท่าใดเมื่อได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย ')
    pdf.ln(7)
    pdf.cell(0, 10, u'              ให้เติมคำว่า คู่สมรส บิดา มารดา หรือบุตรแล้วแต่กรณี')
    pdf.ln(7)
    pdf.cell(0, 10, u'              ให้เสนอต่อผู้มีอำนาจอนุมัติ')
    pdf.ln(7)

    pdf.output("group4/safe.pdf", 'F')

    # next path will open pdf file in new tab on browser.
    with open('group4/safe.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=safe.pdf'
        return response
    pdf.closed



def addpdf2(request, profID): # use to generate pdf file for lend another teacher.
    #template = 'grop4/pdf.html'
    #teachObj = Teach.objects.get(pk= int(profID))   # get all objects teacher.

    Obj = WithdrawCure.objects.get(pk= int(profID))
    print Obj.user
    print WithdrawStudy.user
    #familyObj = Family.objects.get(user=Obj.user)
    lists = Obj.user.family_set.all()
    dad = Obj.user.Father_set.all()
    mom = Obj.user.Monther_set.all()
    ch = Obj.user.Child_set.all()
    presi = EditPresident.objects.all()
    sp = Obj.user.Spouse_set.all()

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()


    try:
        firstname = Obj.user.firstname_th
    except:
        firstname = 'None'

    try:
        lastname = Obj.user.lastname_th
    except:
        lastname = 'None'

    try:
        department = Obj.user.department
    except:
        department = 'None'

    try:
        faculty = Obj.user.faculty
    except:
        faculty = 'None'

    try:
        typeuser = Obj.user.type
    except:
        typeuser = 'None'

    try:
        user = Obj.user
    except:
        user = 'None'

    try:
        account_id = Obj.account_id
    except:
        account_id = 'None'

    try:
        disease = Obj.disease
    except:
        disease = 'None'

    try:
        hospital = Obj.hospital
    except:
        hospital = 'None'

    try:
        hospitalOf = Obj.hospitalOf
    except:
        hospitalOf = 'None'

    try:
        startDate = Obj.startDate
    except:
        startDate = 'None'

    try:
        stopDate = Obj.stopDate
    except:
        stopDate = 'None'

    try:
        value = Obj.value
    except:
        value = 'None'

    try:
        valueChar = Obj.valueChar
    except:
        valueChar = 'None'

    try:
        numBill = Obj.numBill
    except:
        numBill = 'None'

    try:
        typeWithdraw = Obj.typeWithdraw
    except:
        typeWithdraw = 'None'


    pdf.line(12, 38, 198, 38)
    pdf.line(12, 38, 12, 280)
    pdf.line(12, 280, 198, 280)
    pdf.line(198, 38, 198, 280)

    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',80,27,6)

    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',29,50,6) #ข้าราชการ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',49,50,6) #ลูกจ้างประจำ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',73,50,6) #ข้าราชการบำนาช
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',145,50,6) #พนักงานมหาวิทยาลัย

    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,71,6) #ไม่เป็นข้าราชการหรือลูกจ้างประจำ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,78,6) #เป็นข้าราชการ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',45,78,6) #ลูกจ้างประจำ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',70,78,6) #พนักงานมหาวิทยาลัย
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,85,6) #เป็นพนักงานหรือลูกจ้าง

    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,106,6) #เป็นบิดาชอบด้วยกฏหมาย
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,113,6) #เป็นมารดา
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,120,6) #บุตรอยู่ในความปกครองของข้าพเจ้า
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,127,6) #บุตรอยู่ในความอุปการะการเลี้ยงดูของข้าพเจ้า




    pdf.add_font('THSarabunNew Bold', '', 'THSarabunNew Bold.ttf', uni=True)
    pdf.set_font('THSarabunNew Bold', '', 14)
    pdf.cell(169, 10, u'')
    pdf.cell(0, 10, u'แบบ 7223')
    pdf.ln(8)
    pdf.set_font('THSarabunNew Bold', '', 18)
    pdf.cell(0, 10, u'                                    ใบเบิกเงินสวัสดิการการเกี่ยวกับการศึกษาของบุตร     ')
    pdf.ln(7)
    pdf.set_font('THSarabunNew Bold', '', 14)
    pdf.cell(0, 10, u'                                     โปรดทำเครื่องหมาย      ลงในช่องว่าง  พร้อมทั้งกรอกข้อความให้ครบถ้วน    ')
    pdf.ln(16)
    pdf.add_font('THSarabunNew', '', 'THSarabunNew.ttf', uni=True)
    pdf.set_font('THSarabunNew', '', 14)
    pdf.cell(30, 10, u'     1. ข้าพเจ้า................................................................................................เลขที่บัญชีสหกรณ์ออมทรัพย์ SA-.....................................................')
    pdf.cell(115, 8, u'' + firstname + u'  ' + lastname)
    pdf.cell(20, 8, u'' + account_id)
    pdf.ln(7)
    pdf.cell(0, 10, u'        สถานะ  ข้าราชการ   ลูกจ้างประจำ   ข้าราชการบำนาญ(เปลี่ยนสถานะ และ เกษียณอายุ)   พนักงานมหาวิทยาลัย ')
    if typeuser == '0':
        pdf.image('group4\son2.png',29,50,6)
    elif typeuser == '1':
        pdf.image('group4\son2.png',49,50,6)
    elif typeuser == '2':
        pdf.image('group4\son2.png',73,50,6)
    elif typeuser == '3':
        pdf.image('group4\son2.png',145,50,6)
    pdf.ln(7)
    pdf.cell(40, 10, u'        สังกัด ภาควิชา.................................................................................................คณะ......................................................................................')
    if department == '1':
        pdf.cell(85, 8, u'วิศวกรรมไฟฟ้าและคอมพิวเตอร์')
    if faculty == '1':
        pdf.cell(0, 8, u'วิศวกรรมศาสตร์')
    pdf.ln(7)
    pdf.cell(50, 10, u'     2. คู่สมรสของข้าพเจ้าชื่อ .................................................................................................................................................................................')
    pdf.cell(0, 8, u'' + sp.title + sp.firstname + u'  ' + sp.lastname)
    pdf.ln(7)
    pdf.cell(0, 10, u'        □  ไม่เป็นข้าราชการหรือลูกจ้างประจำ')
    if sp.typeOfWork == '0':
        pdf.image('group4\son2.png',19,71,6)
    pdf.ln(7)
    pdf.cell(109, 10, u'        □  เป็นข้าราชการ  □  ลูกจ้างประจำ  □  พนักงานมหาวิทยาลัย ตำแหน่ง...........................................สังกัด.........................................')
    if sp.typeOfWork == '1':
        pdf.image('group4\son2.png',19,78,6)
        pdf.cell(41, 8, u'' + sp.office)
        pdf.cell(0, 8, u'' + sp.position)
    elif sp.typeOfWork == '2':
        pdf.image('group4\son2.png',45,71,6)
        pdf.cell(41, 8, u'' + sp.office)
        pdf.cell(0, 8, u'' + sp.position)
    elif sp.typeOfWork == '3':
        pdf.image('group4\son2.png',70,71,6)
        pdf.cell(41, 8, u'' + sp.office)
        pdf.cell(0, 8, u'' + sp.position)
    pdf.ln(7)
    pdf.cell(0, 10, u'        □  เป็นพนักงานหรือลูกจ้างในรัฐวิสาหกิจ/หน่วยงานของทางราชการ ราชการส่วนท้องถิ่น กรุงเทพมหานคร องค์กรอิสระ')
    if sp.typeOfWork == '4':
        pdf.image('group4\son2.png',19,85,6)
    pdf.ln(7)
    pdf.cell(80, 10, u'             องค์กรมหาชน หรือ หน่วยงานอื่นใด ตำแหน่ง.........................................................................สังกัด.....................................................')
    if sp.typeOfWork == '4':
        pdf.cell(62, 8, u'' + sp.office)
        pdf.cell(0, 8, u'' + sp.position)
    pdf.ln(7)
    pdf.cell(0, 10, u'     3. ข้าพเจ้าเป็นผู้มีสิทธิและขอใช้สิทธิเนื่องจาก ')
    pdf.ln(7)
    pdf.cell(0, 10, u'        □ เป็นบิดาชอบด้วยกฏหมาย')
    if ch.parentRelate == '0':
        pdf.image('group4\son2.png',19,106,6)
    pdf.ln(7)
    pdf.cell(0, 10, u'        □ เป็นมารดา')
    if ch.parentRelate == '1':
        pdf.image('group4\son2.png',19,113,6)
    pdf.ln(7)
    pdf.cell(0, 10, u'        □ บุตรอยู่ในความปกครองของข้าพเจ้า โดยการสิ้นสุดของการสมรส ')
    if ch.parentRelate == '2':
        pdf.image('group4\son2.png',19,120,6)
    pdf.ln(7)
    pdf.cell(0, 10, u'        □ บุตรอยู่ในความอุปการะการเลี้ยงดูของข้าพเจ้าเนื่องจากแยกกันอยู่ โดยมิได้หย่าขาดตามกฏหมาย')
    if ch.parentRelate == '3':
        pdf.image('group4\son2.png',19,127,6)
    pdf.ln(7)
    pdf.cell(0, 10, u'     4. ข้าพเจ้าได้จ่ายเงินสำหรับการศึกษาของบุตร ดังนี้')
    pdf.ln(7)
    pdf.cell(0, 10, u'        (1) เงินบำรุงการศึกษา                                    (2) เงินค่าเล่าเรียน ')
    pdf.ln(7)
    pdf.cell(33, 10, u'            1)  บุตรชื่อ........................................................................................เกิดเมื่อ...........................................................................................')
    pdf.cell(90, 8, u'' + ch.title + ch.firstname + u'  ' + ch.lastname)
    pdf.cell(0, 8, u'' + ch.birthDate)
    pdf.ln(7)
    pdf.cell(70, 10, u'                เป็นบุตรลำดับที่(ของบิดา)...........................................................เป็นบุตรลำดับที่(ของมารดา)..........................................................')
    pdf.cell(80, 8, u'' + ch.orderF)
    pdf.cell(0, 8, u'' + ch.orderM)
    pdf.ln(7)
    pdf.cell(120, 10, u'                (กรณีเป็นบุตรแทนที่บุตรซึ่งถึงแก่กรรมแล้ว) แทนที่บุตรลำดับที่........................................................................................................')
    pdf.cell(0, 8, u'')
    pdf.ln(7)
    pdf.cell(27, 10, u'                ชื่อ...........................................................................เกิดเมื่อ................................................ถึงแก่กรรมเมื่อ........................................')
    pdf.cell(70, 8, u'นายกิตติพงศ์ จันทร์นัณทยงว์ป่า')
    pdf.cell(58, 8, u'11/11/1111')
    pdf.cell(0, 8, u'11/11/1111')
    pdf.ln(7)
    pdf.cell(35, 10, u'                สถานศึกษา.................................................................................อำเภอ........................................จังหวัด..........................................')
    pdf.cell(75, 8, u'มหาวิทยาลัยหหหหหหหหหหหหหหหหหหห')
    pdf.cell(40, 8, u'เมือง')
    pdf.cell(0, 8, u'ราชบุรี')
    pdf.ln(7)
    pdf.cell(35, 10, u'                ชั้นที่ศึกษา..........................................................................................................จำนวน..............................................................บาท')
    pdf.cell(100, 8, u'ประถมศึกษาปีที่4')
    pdf.cell(0, 8, u'2,000')
    pdf.ln(7)
    pdf.cell(0, 10, u'            2)  บุตรชื่อ........................................................................................เกิดเมื่อ...........................................................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                เป็นบุตรลำดับที่(ของบิดา)...........................................................เป็นบุตรลำดับที่(ของมารดา)..........................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                (กรณีเป็นบุตรแทนที่บุตรซึ่งถึงแก่กรรมแล้ว) แทนที่บุตรลำดับที่........................................................................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                ชื่อ...........................................................................เกิดเมื่อ................................................ถึงแก่กรรมเมื่อ........................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                สถานศึกษา.................................................................................อำเภอ........................................จังหวัด..........................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                ชั้นที่ศึกษา..........................................................................................................จำนวน..............................................................บาท')
    pdf.ln(7)
    pdf.cell(0, 10, u'            3)  บุตรชื่อ........................................................................................เกิดเมื่อ...........................................................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                เป็นบุตรลำดับที่(ของบิดา)...........................................................เป็นบุตรลำดับที่(ของมารดา)..........................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                (กรณีเป็นบุตรแทนที่บุตรซึ่งถึงแก่กรรมแล้ว) แทนที่บุตรลำดับที่........................................................................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                ชื่อ...........................................................................เกิดเมื่อ................................................ถึงแก่กรรมเมื่อ........................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                สถานศึกษา.................................................................................อำเภอ........................................จังหวัด..........................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                ชั้นที่ศึกษา..........................................................................................................จำนวน..............................................................บาท')



    pdf.add_page()

    #frame
    pdf.line(12, 15, 198, 15)
    pdf.line(12, 15, 12, 253)
    pdf.line(12, 253, 198, 253)
    pdf.line(198, 15, 198, 253)
    pdf.line(12, 124, 198, 124)
    pdf.line(12, 175, 198, 175)

    #table
    pdf.line(20, 205, 83, 205)
    pdf.line(20, 205, 20, 250)
    pdf.line(20, 250, 83, 250)
    pdf.line(83, 205, 83, 250)

    pdf.line(20, 213, 83, 213)
    pdf.line(20, 220, 83, 220)
    pdf.line(20, 228, 83, 228)
    pdf.line(20, 235, 83, 235)
    pdf.line(48, 205, 48, 235)

    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,26,6) #ตามสิทธิ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',59,26,6) #เฉพาะส่วน
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,47,6) #ข้าพเจ้ามีสิทธิได้รับเงินช่วยเหลือ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,61,6) #บุตรของข้าพเจ้าอยู่ในข่าย
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,68,6) #เป็นผู้ใช้สิทธิเบิกเงินช่วยเหลือ
    pdf.image('C:\Users\Artty\PycharmProjects\untitled\son2.png',19,75,6) #คู่สมรสของข้าพเจ้าได้รับการช่วยเหลือ

    pdf.add_font('THSarabunNew', '', 'THSarabunNew.ttf', uni=True)
    pdf.set_font('THSarabunNew', '', 14)
    pdf.ln(7)
    pdf.cell(0, 10, u'     5. ข้าพเจ้าขอรับเงินสวัสดิการเกี่ยวกับการศึกษาของบุตร')
    pdf.ln(7)
    pdf.cell(120, 10, u'        □  ตามสิทธิ                      □  เฉพาะส่วนที่ยังขาดจากสิทธิ เป็นจำนวนเงิน ............................................................. บาท')
    pdf.cell(0, 8, u'20000')
    pdf.ln(7)
    pdf.cell(20, 10, u'        (...............................................................................................................................................)')
    pdf.cell(0, 8, u'เก้าพันเก้าร้อยเก้าสิบเก้าบาทถ้วน')
    pdf.ln(7)
    pdf.cell(0, 10, u'     6. เสนอ........................................... ')
    pdf.ln(7)
    pdf.cell(0, 10, u'        □  ข้าพเจ้ามีสิทธิได้รับเงินช่วยเหลือตามพระราชกฤษฎีกาเงินสวัสดิการเกี่ยวกับการศึกษาของบุตร')
    pdf.ln(7)
    pdf.cell(0, 10, u'             และข้อความระบุข้างต้นเป็นความจริง ')
    pdf.ln(7)
    pdf.cell(0, 10, u'        □  บุตรของข้าพเจ้าอยู่ในข่ายได้บการช่วยเหลือตามพระราชกฤษฎีกาเงินสวัสดิการเกี่ยวกับการศึกษาของบุตร')
    pdf.ln(7)
    pdf.cell(0, 10, u'        □  เป็นผู้ใช้สิทธิเบิกเงินช่วยเหลือตามพระราชกฤษฎีกาเงินสวัสดิการเกี่ยวกับการศึกษาของบุตรแต่เพียงฝ่ายเดียว')
    pdf.ln(7)
    pdf.cell(0, 10, u'        □  คู่สมรสของข้าพเจ้าได้รับการช่วยเหลือจากรัฐวิสาหกิจ หน่วยงานของทางราชการ ราชการส่วนท้องถิ่นกรุงเทพมหานคร')
    pdf.ln(7)
    pdf.cell(0, 10, u'             องค์กรอิสระ องค์การมหาชน หรือหน่วยงานอื่นใด ต่ำกว่าจำนวนเงินที่ได้รับจากทางราชการเป็นจำนวนเงิน.....................บาท')
    pdf.ln(7)
    pdf.cell(0, 10, u'        ข้าพเจ้าขอรับรองว่ามีสิทธิเบิกได้ตามกฏหมายตามจำนวนเงินที่ขอเบิก')
    pdf.ln(12)
    pdf.cell(0, 10, u'                                                                                            (ลงชื่อ)........................................................ผู้ขอรับเงินสวัสดิการ')
    pdf.ln(7)
    pdf.cell(110, 10, u'                                                                                                   (..........................................................)')
    pdf.cell(0, 8, u'' + firstname + u'   ' + lastname)
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                                               วันที่............เดือน..........................พ.ศ...............')
    pdf.ln(12)
    pdf.cell(0, 10, u'    7. คำอนุมัติ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                  อนุมัติให้เบิกได้')
    pdf.ln(10)
    pdf.cell(0, 10, u'                                                                                             (ลงชื่อ)......................................................... ')
    pdf.ln(7)
    pdf.cell(110, 10, u'                                                                                                    (..........................................................)')
    pdf.cell(0, 8, u'' + presi.presidentName)
    pdf.ln(7)
    pdf.cell(115, 10, u'                                                                                             ตำแหน่ง..........................................................')
    pdf.cell(0, 8, u'' + presi.position)
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                                             วันที่............เดือน..........................พ.ศ............... ')
    pdf.ln(12)
    pdf.cell(0, 10, u'    8. ใบรับเงิน')
    pdf.ln(7)
    pdf.cell(95, 10, u'                 ได้รับเงินสวัสดิการเกี่ยวกับการรักษาพยาบาล จำนวน...........................................................................บาท ')
    pdf.cell(0, 8, u'66,000')
    pdf.ln(7)
    pdf.cell(35, 10, u'          (..............................................................................................................................................................................)ไปถูกต้องแล้ว ')
    pdf.cell(0, 8, u'หกพันบาทถ้วน')
    pdf.ln(15)
    pdf.cell(45, 10, u'           อัตราที่เบิกได้ต่อปี                                                                   (ลงชื่อ)......................................................ผู้รับเงิน')
    pdf.cell(0, 10, u'66,000')
    pdf.ln(7)
    pdf.cell(45, 10, u'           เบิกครั้งก่อน                                                                                 (..........................................................)    ')
    pdf.cell(73, 10, u'6,000')
    pdf.cell(0, 8, u'นายกิตติพงศ์ จันทร์นัณทยงว์ป่า')
    pdf.ln(7)
    pdf.cell(45, 10, u'           เบิกครั้งนี้ ')
    pdf.cell(0, 10, u'6,000')
    pdf.ln(7)
    pdf.cell(45, 10, u'           คงเหลือ                                                                               (ลงชื่อ)......................................................ผู้จ่ายเงิน ')
    pdf.cell(0, 10, u'6,000')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                                                          (..........................................................)')
    pdf.ln(7)
    pdf.cell(0, 10, u'                ....................................ผู้คุมยอดการเบิก                                     วันที่...........เดือน.........................พ.ศ...............')
    pdf.ln(13)
    pdf.cell(0, 10, u'     คำชี้แจง')
    pdf.ln(7)
    pdf.cell(0, 10, u'                   ให้ระบุการมีสิทธิเพียงใด เมื่อเทียบกับสิทธิที่ได้รับตามพระราชกฤษฎีกาเงินสวัสดิการเกี่ยวกับการศึกษาของบุตร')
    pdf.ln(7)
    pdf.cell(0, 10, u'                   ให้เสนอต่อผู่มีอำนาจอนุมัติ')
    pdf.ln(7)


    pdf.output("group4/bursary.pdf", 'F')

    # next path will open pdf file in new tab on browser.
    with open('group4/bursary.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=bursary.pdf'
        return response
    pdf.closed

def check_update():
    name_list = []
    ser_list = []
    cost_list = []
    accnum_list = []
    num = 0
    ondate = []
    countname = 0
    url = "http://www.finance.oop.kmutnb.ac.th"
    full_urls = []
    lists = Olddate.objects.all()
    for i,j in enumerate(lists):
        temp1 = j.date.encode("utf8")
        if temp1 != list_name[i]:
            j.date = list_name[i]
            j.save()
            ondate = str(list_name[i]).split(" ")
            ondate = ondate[1]+" "+ondate[2]+" "+ondate[3]
            full_urls.append(url_list[i])
            num += 1
    update_list = [0 for x in range(num)]
    for k in range(0,num):
        urls = str(full_urls[k])
        #urls = str(new_url[0])
        html = requests.get(urls).text
        ##if has update
        b = bs4.BeautifulSoup(html)
        m = b.find(id='art-main')
        s = m.find("div",{ "class" : "art-article" })
        if s.find("strong") :
            qq = s.findAll("strong")
        else:
            qq = s.findAll("td")
        count= 0
        count2 = 0
        end = 0
        start =0
        pos = 0
        varcost = []
        for row in range(0,len(qq)):
            temp = str(qq[row])
            for index in range(0,len(temp)):
                if temp[index] == '>' :
                    start = index
                elif temp[index] == '<' :
                    end = index
                    count += 1
                if count == 3 :
                    cut = temp[start+1:end]
                    if len(cut) != 0:
                        break
                    else: pass
                elif count == 4:
                    cut = temp[start+1:end]
                    if len(cut) != 0 :
                        break
                    else:
                        pass
                elif count == 6:
                    cut = temp[start+1:end]
                    if len(cut) != 0:
                        break
                    else: pass

            if len(cut) >= 18:
                if cut.find("นาย") == 0:
                    cut = cut[9:len(cut)]
                elif cut.find("นาง") == 0 and cut.find("สาว") != 9:
                    cut = cut[9:len(cut)]
                elif cut.find("นางสาว") == 0:
                    cut = cut[18:len(cut)]
                    #print cut
            #print cut
            if len(cut) != 1 and len(cut) != 2: #except numeric and blank
                pos += 1
                if pos == 1:
                    countname += 1
                    name_list.append(cut)
                elif pos == 2:
                    ser_list.append(cut)
                elif pos == 3:
                    varcost.append(cut)
                    cutpos = cut.find('.')
                    integer = cut[0:cutpos]
                    floats = cut[cutpos+1:len(cut)]
                    if len(integer) >= 5:
                        comma = integer.find(',')
                        frontcomma = integer[0:comma]
                        endcomma = integer[comma+1:len(integer)]
                        integer = int(frontcomma+endcomma)
                    else:
                        integer = int(integer)
                    floats = float(floats)/100
                    cut = integer+floats
                    cost_list.append(cut)
                else:
                    accnum_list.append(cut)
                    pos = 0
            count = 0  # reset count
        update_list[k] = countname
        countname = 0

    for j in range(0,len(name_list)) :
        allUser = UserProfile.objects.all()
        for eachUser in allUser:
            if (eachUser.firstname_th.encode("utf8")==str(name_list[j]) and eachUser.lastname_th.encode("utf8")==str(ser_list[j]) ):
                new_date = DataFromWeb(
                    user = eachUser,
                    date = str(ondate),
                    account_id = str(accnum_list[j]),
                    price = int(cost_list[j]),
                    priceChar = str(varcost[j])
                )
                new_date.save()
