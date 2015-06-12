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
    
    text = u"hello thai language................."
    pdf.write(10, text)
    pdf.image('group3/logo.png',10,20,33)
    pdf.ln(8)
    
    pdf.add_font('Waree', '', 'Waree.ttf', uni=True)
    pdf.set_font('Waree', '', 14)
    pdf.cell(0, 10, u'' + teachObj.prof.profID)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.firstName + '   '+ teachObj.prof.lastName)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.shortName)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.department)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.faculty)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.sahakornAccount)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.tell)
    pdf.ln(8)
    pdf.cell(0, 10, u'' +teachObj.prof.email)
                                
    pdf.ln(20)
    pdf.output("group3/uni.pdf", 'F')
    
    with open('group3/uni.pdf', 'rb') as pdf: # path to pdf in directory views.
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=uni.pdf'
        return response
    pdf.closed
    

