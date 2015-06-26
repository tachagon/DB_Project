# DB_Project
โปรเจ็คสำหรับวิชา Database Systems

## วิธีติดตั้ง FPDF สำหรับ python2.7 windows8.1
* โหลดตัวติดตั้งจาก [Download](http://pyfpdf.googlecode.com/files/fpdf-1.7.hg.zip) แล้วทำการแตกไฟล์
* เปิดหน้าต่าง command line แล้วเข้าไปยังไดเรกทอรีที่เพิ่งแตกไฟล์ออกมาแล้วพิมพ์คำสั่ง
   python setup.py install
* [Download unicode font](http://pyfpdf.googlecode.com/files/fpdf_unicode_font_pack.zip) ได้เป็นไฟล์ zip ออกมา ทำการแตกไฟล์จะได้โฟล์เดอร์ font ออกมา
* ย้ายไฟล์เดอร์ font ไปเก็บยัง C:\Python27\Lib\site-packages\fpdf
* ทดสอบโค้ด
###Example
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from fpdf import FPDF

	pdf = FPDF('P', 'mm', 'A4')
	pdf.add_page()

	pdf.add_font('Kinnari', '', 'Kinnari.ttf', uni=True)
	pdf.set_font('Kinnari', '', 12) # 12 is font size

	pdf.cell(0, 10, u'สวัสดี')
	pdf.ln(10) # new line
	pdf.cell(0, 10, u'ชาวโลก')
	pdf.line(8, 20, 30, 20) # draw line(x1, y1, x2, y2)

	pdf.output('exam.pdf') # generate pdf file

* ส่วน #-*- coding: utf-8 -*- ทำให้เราเขียนภาษาไทยใน code python ได้และให้เราเปลี่ยนค่า file encoding เป็น UTF-8 ด้วย

* หลังจาก run สำเร็จแล้วจะได้ไฟล์ชื่อ exam.pdf ออกมา   สามารถหาข้อมูลเกี่ยวกับ fpdf เพิ่มเติมได้ที่
[https://code.google.com/p/pyfpdf/](https://code.google.com/p/pyfpdf/)
