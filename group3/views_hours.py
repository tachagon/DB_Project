#-*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from login.models import *
from group3.models import *
from datetime import date, time

def add_work(request, employeeID):
    template = 'group3/worker/add_work.html'
    context = {}
    employee = HourlyEmployee.objects.get(id=employeeID)
    context["employee"] = employee

    if request.method == "POST":
        startTime_hour   = request.POST["startTime_hour"]
        startTime_minute = request.POST["startTime_minute"]
        endTime_hour     = request.POST["endTime_hour"]
        endTime_minute   = request.POST["endTime_minute"]

        if (int(startTime_hour) >= int(endTime_hour)) or (int(startTime_hour) < 9) or (int(startTime_hour) > 16) or ( int(endTime_hour) > 16 ) or ( int(endTime_hour) < 9 ):
            context['show_error1'] = "error"
            return render(request, template, context)
        elif (int(startTime_hour) == int(endTime_hour)) and ( int(startTime_minute) > int(endTime_minute) ):
            context['show_error1'] = "error"
            return render(request, template, context)
        
        startTime = str(startTime_hour + ":" + startTime_minute + ":00")
        endTime   = str(endTime_hour   + ":" + endTime_minute   + ":00")
#=======
        #startTime = time(int(startTime_hour), int(startTime_minute), 0)
        #endTime   = time(int(endTime_hour), int(endTime_minute), 0)
        #
        #today = date.today()
        #workList = Work.objects.filter(releaseDate = today, employee = employee).order_by('-id')
        #if len(workList) != 0:
        #    lastWork = workList[0]
        #    if lastWork.endTime > startTime:
        #        context['error'] = "เวลาเริ่มงานไม่ถูกต้อง"
        #        return render(
        #            request,
        #            template,
        #            context
        #        )

#>>>>>>> master

        workObj = Work(
            startTime = startTime,
            endTime   = endTime,
            employee  = employee
        )
        workObj.save()
        return HttpResponseRedirect(reverse('group3:returnsearch', args=[employeeID]))


    return render(
        request,
        template,
        context
    )
