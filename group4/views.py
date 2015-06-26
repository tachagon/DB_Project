#-*- coding: utf-8 -*-
from django.shortcuts import render
from group4.models import *
# Create your views here.
def adminShow(request):
    template = 'group4/adminShow.html'    # get template
    dataFromWebList = DataFromWeb.objects.all()     # get all Prof2Lang objects

    return render(
        request,
        template,
        {'dataFromWebList': dataFromWebList}
    )