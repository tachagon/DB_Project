#-*- coding: utf-8 -*-
from django.shortcuts import render
from group4.models import *
from django.http import HttpResponse,HttpResponseRedirect
from checkWeb import *
from django.core.urlresolvers import reverse
from fpdf import FPDF
from django.utils import timezone
# Create your views here.

def adminIndex(request):
    template = 'group4/adminIndex.html'    # get template
    dataFromWebList_Index = Withdraw.objects.all().order_by('-id')[:5]     # get all Prof2Lang objects
    olddate = Olddate.objects.all().order_by('-id')
    return render(
        request,
        template,
        {'dataFromWebList_Index': dataFromWebList_Index,
         'olddate':olddate
         }
    )

def adminShow(request):
    template = 'group4/adminShow.html'    # get template
    check_update()
    try:
        getlen = DataFromWeb.objects.all()
        dataFromWebList = DataFromWeb.objects.all().order_by('-id')[:len(getlen)]    # get all DataFromWeb objects

        return render(
            request,
            template,
            {'dataFromWebList': dataFromWebList}
        )
    except:
        return render(
            request,
            template,
            {}
        )

def userShow(request):
    template = 'group4/userShow.html'    # get template
    user = request.user
    try:
        userprofile = UserProfile.objects.get(user = user)
        eachUserDataList = DataFromWeb.objects.all().order_by('-id')[:len(userprofile)]
        datalist = []
        for i in eachUserDataList:
            if i.user==userprofile:
                datalist.append(i)

        return render(
            request,
            template,
            {'eachUserDataList': datalist}
        )
    except:
        return render(
            request,
            template,
            {}
        )

def addNewPage(request):
    template = 'group4/addNewPage.html'    # get template
    objUser = request.user
    objUsers = UserProfile.objects.get(user=objUser)
    print type(objUsers.type.encode("utf8"))
    if (objUsers.type.encode("utf8") == "1"):
        typeUser = Teacher.objects.get(userprofile=objUsers)
    elif (objUsers.type.encode("utf8") == "2"):
        typeUser = Officer.objects.get(userprofile=objUsers)


    return render(
        request,
        template,
        {"objUsers": objUsers,
         "typeUser": typeUser
         }
    )

def commit(request):
    if request.method == "POST":

        objUser         = request.user
        objUsers        = UserProfile.objects.get(user=objUser)
        account_id      = request.POST["account_id"]
        disease         = request.POST["disease"]
        hospital        = request.POST["hospital"]
        hospitalOf      = request.POST["hospitalOf"]
        startDate       = request.POST["startDate"]
        stopDate        = request.POST["stopDate"]
        value           = request.POST["value"]
        valueChar       = request.POST["valueChar"]
        numBill         = request.POST["numBill"]
        credit          = request.POST["credit"]
        creditChar      = request.POST["creditChar"]
        claim           = request.POST["claim"]
        selfClaim       = request.POST["selfClaim"]
        typeWithdraw    = request.POST["typeWithdraw"]
        if typeWithdraw == '1':
            familyClaim     = request.POST["familyClaim1"]
        elif typeWithdraw =='2':
            familyClaim     = request.POST["familyClaim2"]
        elif typeWithdraw=='3':
            familyClaim     = request.POST["familyClaim3"]
        elif typeWithdraw=='4':
            familyClaim     = request.POST["familyClaim4"]
        dataWithdraw    = Withdraw(
            user        = objUsers,
            account_id  = account_id,
            disease     = disease,
            hospital    = hospital,
            hospitalOf  = hospitalOf,
            startDate   = startDate,
            stopDate    = stopDate,
            value       = value,
            valueChar   = valueChar,
            numBill     = numBill,
            credit      = credit,
            creditChar  = creditChar,
            claim       = claim,
            selfClaim   = selfClaim,
            familyClaim = familyClaim,
            typeWithdraw= typeWithdraw
        )
        dataWithdraw.save()

        if(typeWithdraw!='0'):
            objUser         =   request.user
            objUsers        =   UserProfile.objects.get(user=objUser)
            if typeWithdraw == '1':
                firstnameFam    =   request.POST["firstnameFam1"]
                lastnameFam     =   request.POST["lastnameFam1"]
                pidFam          =   request.POST["pidFam1"]
            elif typeWithdraw =='2':
                firstnameFam    =   request.POST["firstnameFam2"]
                lastnameFam     =   request.POST["lastnameFam2"]
                pidFam          =   request.POST["pidFam2"]
            elif typeWithdraw =='3':
                firstnameFam    =   request.POST["firstnameFam3"]
                lastnameFam     =   request.POST["lastnameFam3"]
                pidFam          =   request.POST["pidFam3"]
            elif typeWithdraw =='4':
                firstnameFam    =   request.POST["firstnameFam4"]
                lastnameFam     =   request.POST["lastnameFam4"]
                pidFam          =   request.POST["pidFam4"]
            dataFamily      =   Family(
                user        =   objUsers,
                firstname   =   firstnameFam,
                lastname    =   lastnameFam,
                pid         =   pidFam,
                typeFamily  =   typeWithdraw
            )
            dataFamily.save()

        if(typeWithdraw=='3'):
            family          =   dataFamily
            office          =   request.POST["officeFam3"]
            position        =   request.POST["positionFam3"]
            dataSpouse      =   Spouse(
                family      =   family,
                office      =   office,
                position    =   position
            )
            dataSpouse.save()

        if(typeWithdraw=='4'):
            family          =   dataFamily
            birthDate       =   request.POST["birthDateFam4"]
            orderF          =   request.POST["orderF4"]
            orderM          =   request.POST["orderM4"]
            disable         =   request.POST["disable4"]
            dataChild       =   Child(
                family      =   family,
                birthDate   =   birthDate,
                orderF      =   orderF,
                orderM      =   orderM,
                disable     =   disable
            )
            dataChild.save()

    return HttpResponseRedirect(reverse("group4:userShow"))

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
            ondate = ondate[1]+ondate[2]+ondate[3]
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
        print ondate
    for j in range(0,len(name_list)) :
        allUser = UserProfile.objects.all()
        for eachUser in allUser:
            if (eachUser.firstname_th.encode("utf8")==str(name_list[j]) and eachUser.lastname_th.encode("utf8")==str(ser_list[j]) ):
                new_date = DataFromWeb(
                    user = eachUser,
                    date = str(ondate),
                    account_id = str(accnum_list[j]),
                    price = int(cost_list[j])
                )
                new_date.save()
def addpdf(request, profID): # use to generate pdf file for lend another teacher.
    #template = 'grop4/pdf.html'
    #teachObj = Teach.objects.get(pk= int(profID))   # get all objects teacher.

    Obj = Withdraw.objects.get(pk= int(profID))
    print Obj.user
    print Family.user
    #familyObj = Family.objects.get(user=Obj.user)
    lists = Obj.user.family_set.all()



    print "5555555   ", len(lists)
    #UserPro = UserProfile.objects.all()



    pdf = FPDF('P', 'mm', 'A4')    # start pdf file
    pdf.add_page()                 # begin first page.


    user        = ''
    account_id  = ''
    disease  = ''
    hospital = ''
    hospitalOf = ''
    startDate   = ''
    stopData    = ''
    value       = ''
    valueChar   = ''
    numBill     = ''
    credit      = ''
    creditChar  = ''
    claim  = ''
    typeFamily  = ''
    typeClaim   = ''
    selfClaim   = ''
    familyClaim = ''
    typeWithdraw= ''

    #try:
        #typeFamily = familyObj.typeFamily
    #except:
    #    typeFamily = 'None'

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
        stopData = Obj.stopData
    except:
        stopData = 'None'

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
        credit = Obj.credit
    except:
        credit = 'None'

    try:
        creditChar = Obj.creditChar
    except:
        creditChar = 'None'

    try:
        claim = Obj.claim
    except:
        claim = 'None'

    try:
        selfClaim = Obj.selfClaim
    except:
        selfClaim = 'None'

    try:
        familyClaim = Obj.familyClaim
    except:
        familyClaim = 'None'

    try:
        typeWithdraw = Obj.typeWithdraw
    except:
        typeWithdraw = 'None'

    for fam in lists:
        if fam.typeFamily== typeWithdraw:
            fami = fam

    famiFirstname = fami.firstname
    famiLastname = fami.lastname
    famiPid = fami.pid

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
    pdf.cell(30, 10, u'     1. ข้าพเจ้า................................................................................................เลขที่บัญชีสหกรณ์ออมทรัพย์............................................................')
    pdf.cell(115, 8, u'' + firstname + u'   ' + lastname)
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
    if typeWithdraw == '0':
        pdf.image('son2.png',20,64,6)
    pdf.ln(7)
    pdf.cell(40, 10, u'           คู่สมรส  ชื่อ...............................................................................เลขประจำตัวประชาชน......................................................')
    if typeWithdraw == '3':
        pdf.image('group4\son2.png',20,71,6)
        pdf.cell(90, 8, u''+famiFirstname+u'  '+famiLastname)
        pdf.cell(0, 8, u''+famiPid)
    pdf.ln(7)
    pdf.cell(45, 10, u'                         ที่ทำงาน......................................................................ตำแหน่ง..............................................................................')
    if typeWithdraw == '3':
        sp = Spouse.objects.get(family=fami)
        pdf.cell(70, 8, u''+sp.office)
        pdf.cell(0, 8, u''+sp.position)
    pdf.ln(7)

    pdf.cell(40, 10, u'           บิดา      ชื่อ..............................................................................เลขประจำตัวประชาชน......................................................')
    if typeWithdraw == typeFamily:
        pdf.image('group4\son2.png',20,85,6)
        pdf.cell(90, 8, u''+famiFirstname+u'  '+famiLastname)
        pdf.cell(0, 8, u''+famiPid)
    pdf.ln(7)

    pdf.cell(40, 10, u'           มารดา   ชื่อ..............................................................................เลขประจำตัวประชาชน......................................................')
    if typeWithdraw == '2':
        pdf.image('group4\son2.png',20,92,6)
        pdf.cell(90, 8, u''+famiFirstname+u'  '+famiLastname)
        pdf.cell(0, 8, u''+famiPid)
    pdf.ln(7)

    pdf.cell(40, 10, u'           บุตร      ชื่อ..............................................................................เลขประจำตัวประชาชน......................................................')
    if typeWithdraw == '4':
        pdf.image('group4\son2.png',20,99,6)
        pdf.cell(90, 8, u''+famiFirstname+u'  '+famiLastname)
        pdf.cell(0, 8, u''+famiPid)
    pdf.ln(7)
    pdf.cell(42, 10, u'                          เกิดเมื่อ.................................................เป็นบุตรลำดับที่(ของบิดา)..................เป็นบุตรลำดับที่(ของมารดา)................... ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                           ยังไม่บรรลุนิติภาวะ    เป็นบุตรไร้ความสามารถ หรือเสมือนไร้ความสามารถ ')
    if typeWithdraw == '4':
        ch = Child.objects.get(family=fami)
        pdf.cell(75, 8, u'' + str(ch.birthDate))
        pdf.cell(50, 8, u'' + str(ch.orderF))
        pdf.cell(0, 8, u'' + str(ch.orderM))
         ################################
        if ch.disable=='1':
            pdf.image('group4\son2.png',71,113,6)
        year = timezone.now().year
        month = timezone.now().month
        today = timezone.now().day
        print today
        birthdate = []
        birthdate = str(ch.birthDate).split('-')
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
    pdf.cell(100, 8, u'' + str(stopData))
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
    if claim == '1':
        pdf.image('group4\son2.png',19,190,6)
    elif claim == '2':
        pdf.image('group4\son2.png',56,190,6)
    elif claim == '3':
        pdf.image('group4\son2.png',56,197,6)

    pdf.cell(30, 10, u'       เป็นเงิน.....................................................บาท (............................................................................................................................) และ ')
    pdf.cell(55, 8, u'' + str(credit))
    pdf.cell(0, 8, u'' + creditChar)
    pdf.ln(12)
    pdf.cell(0, 10, u'       (1)  ข้าพเจ้า                ไม่มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่น  ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นแต่เลือกใช้สิทธิจากทางราชการ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย  ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      เป็นผู้ใช้สิทธิเบิกค่ารักษาพยาบาลสำหรับบุตรแค่เพียงฝ่ายเดียว ')
    pdf.ln(10)
    if selfClaim == '1':
        pdf.image('group4\son2.png',49,216,6)
    elif selfClaim == '2':
        pdf.image('group4\son2.png',49,223,6)
    elif selfClaim == '3':
        pdf.image('group4\son2.png',49,230,6)
    elif selfClaim == '4':
        pdf.image('group4\son2.png',49,237,6)

    pdf.cell(0, 10, u'       (2) ................ข้าพเจ้า     ไม่มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่น                      ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นแต่ค่ารักษาพยาบาลที่ได้รับต่ำกว่าสิทธิตามพระราชกฤษฎีกาฯ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลตามสัญญาประกันภัย ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                      มีสิทธิได้รับค่ารักษาพยาบาลจากหน่วยงานอื่นในฐานะเป็นผู้อาศัยสิทธิของผู้อื่น ')
    pdf.ln(7)
    if familyClaim == '1':
        pdf.image('group4\son2.png',49,247,6)
    elif familyClaim == '2':
        pdf.image('group4\son2.png',49,254,6)
    elif familyClaim == '3':
        pdf.image('group4\son2.png',49,261,6)
    elif familyClaim == '4':
        pdf.image('group4\son2.png',49,268,6)



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
    pdf.cell(0, 10, u'                                                                                             (..........................................................)')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                                          วันที่............เดือน..........................พ.ศ...............')
    pdf.ln(14)

    pdf.cell(0, 10, u'    5. คำอนุมัติ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                  อนุมัติให้เบิกได้')
    pdf.ln(14)
    pdf.cell(0, 10, u'                                                                       (ลงชื่อ)........................................................ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                             (..........................................................)')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                      ตำแหน่ง..........................................................')
    pdf.ln(7)
    pdf.cell(0, 10, u'                                                                     วันที่............เดือน..........................พ.ศ............... ')
    pdf.ln(14)

    pdf.cell(0, 10, u'    6. ใบรับเงิน')
    pdf.ln(7)
    pdf.cell(0, 10, u'                 ได้รับเงินสวัสดิการเกี่ยวกับการรักษาพยาบาล จำนวน...........................................................................บาท ')
    pdf.ln(7)
    pdf.cell(0, 10, u'          (................................................................................................................................................)ไปถูกต้องแล้ว ')
    pdf.ln(18)
    pdf.cell(0, 10, u'           วงเงินที่ได้รับ                                                                          (ลงชื่อ)......................................................ผู้รับเงิน')
    pdf.ln(7)
    pdf.cell(0, 10, u'           เบิกครั้งก่อน                                                                                 (..........................................................)    ')
    pdf.ln(7)
    pdf.cell(0, 10, u'           เบิกครั้งนี้ ')
    pdf.ln(7)
    pdf.cell(0, 10, u'           คงเหลือ                                                                               (ลงชื่อ)......................................................ผู้จ่ายเงิน ')
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