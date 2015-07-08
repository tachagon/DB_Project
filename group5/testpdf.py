#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fpdf import FPDF


pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
pdf.set_font('Kinnari', '', 12) # 12 is font size

#pdf.image('C:/Python27/Scripts/DB_Project por/static/images/picture.jpg', 10, 8, 33)
        # position logo on the right
pdf.cell(0, 10, u'สวัสดี')
pdf.ln(10) # new line
pdf.cell(0, 10, u'ชาวโลก')
pdf.ln(10) # new line
pdf.cell(0, 10, u'ชาวโลก')

pdf.output("group5/exam.pdf", 'F') # generate pdf file
#C:/Users/jittinan/Desktop/