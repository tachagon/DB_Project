#-*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from login.models import *
from group3.models import *

def prof_index(request):
    template = 'group3/prof/prof_index.html'
    context = {}

    profList = Prof2Lang.objects.all().order_by('profID')
    context['profList'] = profList
    return render(
        request,
        template,
        context
    )

def prof_add(request):
    template = 'group3/prof/prof_form.html'
    context = {}

    context['menuName'] = 'เพิ่มข้อมูลอาจารย์ผู้สอน'
    context['formAction'] = '0'

    error = False
    errorMessage = []

    if request.method == 'POST':
        profID          = request.POST['profID']            # 1. profID
        firstName       = request.POST['firstName']         # 2. firstName
        lastName        = request.POST['lastName']          # 3. lastName
        shortName       = request.POST['shortName']         # 4. shortName
        tell            = request.POST['tell']              # 5. tell
        email           = request.POST['email']             # 6. email
        sahakornAccount = request.POST['sahakornAccount']   # 7. sahakornAccount
        department      = request.POST['department']        # 8. department
        faculty         = request.POST['faculty']           # 9. faculty

        # ปรับ shortName ให้เป็นตัวพิมพ์ใหญ่
        shortName = str(shortName).upper()

        # ตรวจสอบดูว่า profID ซ้ำหรือไม่
        try:
            test = Prof2Lang.objects.get(profID = profID)
            error = True
            errorMessage.append('รหัสอาจารย์นี้มีในฐานข้อมูลแล้ว')
        except:
            pass

        if error:
            context['profID']           = profID            # 1. profID
            context['firstName']        = firstName         # 2. firstName
            context['lastName']         = lastName          # 3. lastName
            context['shortName']        = shortName         # 4. shortName
            context['tell']             = tell              # 5. tell
            context['email']            = email             # 6. email
            context['sahakornAccount']  = sahakornAccount   # 7. sahakornAccount
            context['department']       = department        # 8. department
            context['faculty']          = faculty           # 9. faculty

            context['errorMessage']     = errorMessage
        else:
            # create new Prof2Lang object
            newProf = Prof2Lang(
                profID          = profID,           # 1. profID
                firstName       = firstName,        # 2. firstName
                lastName        = lastName,         # 3. lastName
                shortName       = shortName,        # 4. shortName
                tell            = tell,             # 5. tell
                email           = email,            # 6. email
                sahakornAccount = sahakornAccount,  # 7. sahakornAccount
                department      = department,       # 8. department
                faculty         = faculty           # 9. faculty
            )

            # save new Prof2Lang object into database
            newProf.save()
            context['successMessage'] = "เพิ่มข้อมูลอาจารย์ผู้สอนเรียบร้อยแล้ว"

    return render(
        request,
        template,
        context
    )

def prof_view(request, profID):
    template = 'group3/prof/prof_view.html'
    context = {}
    try:
        prof = Prof2Lang.objects.get(profID = profID)
        context['prof'] = prof
    except:
        pass
    return render(
        request,
        template,
        context
    )

def prof_update(request, profID):
    template = 'group3/prof/prof_form.html'
    context = {}

    # get Prof2Lang object
    prof = Prof2Lang.objects.get(profID = profID)

    context['prof'] = prof
    context['menuName'] = 'แก้ไขข้อมูล'

    context['profID']           = prof.profID           # 1. profID
    context['firstName']        = prof.firstName        # 2. firstName
    context['lastName']         = prof.lastName         # 3. lastName
    context['sahakornAccount']  = prof.sahakornAccount  # 7. sahakornAccount

    return render(
        request,
        template,
        context
    )
