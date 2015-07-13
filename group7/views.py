#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from group6.models import *
from group7.models import *
from login.models import *
from datetime import datetime
from django.views import generic
import datetime

month = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
def home(request):#ส่วนสำหรับแสดงหน้าhome
	stu = ProjectG6.objects.all()#เลือกโปรเจ็คทั้งหมดที่มีออกมา
        teacher=[]
        for name in stu:#วนลูปเพื่อเข้าถึงทุกobjectsในprojectแต่ละproject
            p=Teacher.objects.get(id=name.teacher_id)#เก็ทค่าของteacherที่เป็นที่ปรึกษาโปรเจคนั้นๆ
	    q=UserProfile.objects.get(id=p.userprofile_id)#เก็ทค่ารายละเอียดของอาจารย์ออกมา
	    n=q.firstname_th+"  "+q.lastname_th#เก็บค่าชื่อไทยของอาจารย์
	    teacher.append(name.name_thai)#เก็บค่าชื่อโปรเจ็คภาษาไทยไว้ในตัวแปรteacher
	    teacher.append(name.name_eng)#เก็บค่าชื่อโปรเจ็คภาษาอังกฤษไว้ในตัวแปรteacher
            teacher.append(n)#เก็บค่าชื่ออาจารย์ภาษาไทยไว้ในตัวแปรteacher
	    teacher.append(name.id)
        return render(request, 'group7/home.html', {'teacher':teacher})
                
def order(request,pk):
	project = ProjectG6.objects.get(id=pk)#เลือกโปรเจ็คทั้งหมดที่มีออกมา
	order=Order.objects.all()#เลือกorderทั้งหมดที่มีออกมา
	date=[]
	for r in order:
		if r.Projectg7_id==project.id:
			date.append(str((r.Date).day)+"/"+month[(r.Date).month-1] +"/"+str((r.Date).year))#เปลี่ยนแปลงรูปแบบวันที่ที่ต้องการแสดง
        teacher=Teacher.objects.get(id=project.teacher_id)#เก็ทค่าของteacherที่เป็นที่ปรึกษาโปรเจคนั้นๆ
	usr=UserProfile.objects.get(id=teacher.userprofile_id)#เก็ทค่ารายละเอียดของอาจารย์ออกมา
	pid=CategoriesProject.objects.get(project_id=pk)
        return render(request, 'group7/order.html', {'object': project,'teacher':usr,'dates':date,'pid':pid})
def addorder(request,pk):
	projectg6 = ProjectG6.objects.get(id=pk)#เลือกโปรเจ็คที่id=pk
	now = datetime.datetime.now()
	now=now.date()
	date = datetime.datetime.strptime(str(now), '%Y-%m-%d').strftime('%d-%m-%Y')#เก็บค่าวันที่ปัจจุบันในรูปแบบ ปี เดือน วัน
	return render(request, 'group7/addorder.html', {'object': date,'projectg6':projectg6})



        
def addorderview(request, pk):
	date=request.GET.get('date')#รับค่าวันที่จากtemplate
	valid_date = datetime.datetime.strptime(str(date), '%d-%m-%Y').strftime('%Y-%m-%d')#เก็บค่าวันที่ปัจจุบันในรูปแบบ ปี เดือน วัน
        p=Order(Projectg7_id=pk,Date=valid_date)  #สร้าง orderใหม่ 	
	p.save()
        url="/group7/"+pk
        return HttpResponseRedirect(url)
#----------------------------- Orderinfo -------------------------------------------#
def orderinfo(request,pk):
        s = Order.objects.get(id=pk)
        info=s.orderinfo_set.all()
        sum=0
	sum2=""
        for price in info:
            sum+=price.Cost_total
	sum2='{:,.2f}'.format(sum)
        return render(request, 'group7/orderinfo.html', {'object': info,'sum':sum2,'s':s})

#----------------------------- Add OrderInfo -------------------------------------------#
class addorderinfo(generic.DetailView):
	model=Order
        template_name='group7/addorderinfo.html'

def addorderinfoview(request, pk):
	itemname=request.POST['itemname_orderinfo']
	amount=request.POST['amount_orderinfo']
	price=request.POST['price_orderinfo']
        company=request.POST['company']
        id=request.POST['id']
        sum=float(price)*float(amount)
        p=Orderinfo(Order_id=pk,Item_name=itemname, Amount=amount,Company=company,OrderID=id, Cost=price, Cost_total=sum)   	
	p.save()
        url="/group7/"+pk+"/orderinfo/"
        return HttpResponseRedirect(url)
#----------------------------- StatusOf -------------------------------------------#
def statusof(request,pk):
	s = Order.objects.get(id=pk)
        order=Status_Of.objects.all()
	data=[]
	rid=[]
	for r in order:
		if r.Order_id==s.id:
			data.append(str((r.Date).day)+"/"+month[(r.Date).month-1] +"/"+str((r.Date).year))
			data.append(r.State)
			data.append(r.Status)
			data.append(r.Moreabout)
			data.append(r.id)

	return render(request, 'group7/statusof.html', {'data': data,'s':s})
# Create your views here.
def addstatusview(request,pk):
	now = datetime.datetime.now()
	now=now.date()
	date = datetime.datetime.strptime(str(now), '%Y-%m-%d').strftime('%d-%m-%Y')
        order=Order.objects.get(id=pk)
	stat=order.status_of_set.all()
	laststat=""
	id=pk
	for s in stat:
		laststat=s.State
	return render(request, 'group7/addstatusof.html', {'object': laststat,'id':id,'now':date})
	
def addstatus(request,pk):
    date=request.GET.get('date')
    valid_date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
    state = request.GET.get('state_status')
    more=request.GET.get('more')
    status=""
    
    if (request.GET.get('state_status')=="complete"):
        status="สมบูรณ์"
        state="ใบเบิกวัสดุ"
	if (request.GET.get('requisition_id')!="None"):
		reqid=request.GET.get('requisition_id')
		req=Requisition(Status_of_id=pk,Requisition_Id=reqid)
		req.save()
    else:
        status="ไม่สมบูรณ์"
    p=Status_Of(Order_id=pk,Date=valid_date,State=state, Status=status ,Moreabout=more,Prove="Ok") 
    p.save()
    url="/group7/"+pk+"/statusof/"
    return HttpResponseRedirect(url)
    
def removeOrder(request,info_id): #Page Order for delete Order
	p=Order.objects.get(id=info_id)
        q=p.Projectg7_id
	p.delete()
	p.save
	url="/group7/"+str(q)
	return HttpResponseRedirect(url)
def removeOrderinfo(request,info_id): #Page Orderinfo for delete Orderinfo
	p=Orderinfo.objects.get(id=info_id)
        q=p.Order_id
	p.delete()
	p.save
	url="/group7/"+str(q)+"/orderinfo/"
	return HttpResponseRedirect(url)
        
def orderedit(request,pk):
        stu=Orderinfo.objects.get(id=pk)
        now = datetime.datetime.now()
        return render(request, 'group7/editorderinfo.html', {'object': stu})
    
    
def editOrderinfo(request,info_id): #Page Orderinfo for delete Orderinfo
        itemname=request.GET.get('itemname_orderinfo')
	amount=request.GET.get('amount_orderinfo')
	price=request.GET.get('price_orderinfo')
        company=request.GET.get('company')
        id=request.GET.get('id')
        sum=float(price)*float(amount)
        q=Orderinfo.objects.get(id=info_id)
	p=Orderinfo(id=info_id,Order_id=q.Order_id,Item_name=itemname, Amount=amount,Company=company,OrderID=id, Cost=price, Cost_total=sum)   	
	p.save()
	url="/group7/"+str(q.Order_id)+"/orderinfo/"
	return HttpResponseRedirect(url)
def removeStatusof(request,info_id): #Page Orderinfo for delete Orderinfo
	p=Status_Of.objects.get(id=info_id)
	objects=Order.objects.get(id=p.Order_id)
	for r in objects.requisition_set.all():
		s=r
		s.delete()
        q=p.Order_id
	p.delete()
	p.save
	url="/group7/"+str(q)+"/statusof/"
	return HttpResponseRedirect(url)
#----------------------------- View orderinfo -------------------------------------------#
class vieworderinfo(generic.DetailView):
	model=Order
   	template_name= 'group7/orderinfoview.html'
#----------------------------- View requisition -------------------------------------------#
def viewrequi(request,pk):
        now=""
	order = Order.objects.get(id=pk) 
	reqid=""
	moreabout=""
	id=""
	stat4=order.status_of_set.all()
	for r in stat4:
		id=r.id
		status4=r.State
		date4=r.Date
		moreabout=r.Moreabout
	if status4.encode('utf-8') == "ใบเบิกวัสดุ":
		req=Requisition.objects.get(Status_of_id=pk)
		reqid=req.Requisition_Id
		now=str((date4).day)+"/"+month[(date4).month-1] +"/"+str((date4).year)
	project=ProjectG6.objects.get(id=order.Projectg7_id)
        return render(request, 'group7/requisitionview.html', {'order': order,'project':project,'date':now,'req':reqid,'more':moreabout})

def vieworderprint(request,pk):
        now = datetime.datetime.now()
	order = Order.objects.get(id=pk)
	date3=str((order.Date).day)+"/"+month[(order.Date).month-1] +"/"+str((order.Date).year)
        project=ProjectG6.objects.get(id=order.Projectg7_id)
        stu = ProjectG6.objects.all()
        teacher=[]
	student=[]
        for name in stu:
                p=Teacher.objects.get(id=name.teacher_id)
		q=UserProfile.objects.get(id=p.userprofile_id)#เก็ทค่ารายละเอียดของอาจารย์ออกมา
		n=q.firstname_th+"  "+q.lastname_th#เก็บค่าชื่อไทยของอาจารย์
		teacher.append(n)
	namestd=project.student.all()
	for std in namestd:
		q=UserProfile.objects.get(id=std.userprofile_id)#เก็ทค่ารายละเอียดของอาจารย์ออกมา
		n=q.firstname_th+"  "+q.lastname_th
		student.append(n)
        return render(request, 'group7/orderinfoview.html', {'order': order,'teacher':teacher,'project':project,'date':date3,'student':student})
        
def statusofedit(request,pk):
        stu=Status_Of.objects.get(id=pk)
	req=""
	if stu.State.encode('utf-8') == "ใบเบิกวัสดุ":
		req=Requisition.objects.get(Status_of_id=stu.Order_id)
	now = datetime.datetime.now()
        return render(request, 'group7/editstatusof.html', {'object': stu,'req':req})
        
def editstatusof(request,info_id): #Page Orderinfo for delete Orderinfo
	date=request.GET.get('date')
	valid_date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
    	state = request.GET.get('state_status')
    	more=request.GET.get('more')
    	status=""
	q=Status_Of.objects.get(id=info_id)
    	if (request.GET.get('state_status')=="complete"):
        	status="สมบูรณ์"
        	state="ใบเบิกวัสดุ"
		if (request.GET.get('requisition_id')!="None"):
			reqid=request.GET.get('requisition_id')
			re=Requisition.objects.get(Status_of_id=q.Order_id)
			req=Requisition(id=re.id,Status_of_id=q.Order_id,Requisition_Id=reqid)
			req.save()
		
    	else:
        	status="ไม่สมบูรณ์"
	
    	p=Status_Of(id=info_id,Order_id=q.Order_id,Date=valid_date,State=state, Status=status ,Moreabout=more,Prove="Ok") 
    	p.save()
    	url="/group7/"+str(q.Order_id)+"/statusof/"
    	return HttpResponseRedirect(url)
	
def sumdate(request):
	status=""
	date=""
	dataset=[]
	ordd=Order.objects.all()
	for s in ordd:
		stat=s.status_of_set.all()
		for r in stat:
			status=r.State.encode('utf-8')
			date=str((r.Date).day)+"/"+month[(r.Date).month-1] +"/"+str((r.Date).year)
		if status == "วันที่ในการซื้อวัสดุ":
			data=(ProjectG6.objects.get(id=s.Projectg7_id))
			dataset.append(data.name_thai)
			dataset.append(date)
		status=""
	return render(request, 'group7/showlistdate.html', {'data': dataset})

def sumcheck(request):
	status2=""
	date2=""
	dataset2=[]
	ordd2=Order.objects.all()
	for s in ordd2:

		stat2=s.status_of_set.all()
		for r in stat2:
			status2=r.State.encode('utf-8')
			date2=str((r.Date).day)+"/"+month[(r.Date).month-1] +"/"+str((r.Date).year)
			
		if status2 == "ตรวจสอบวัสดุและใบเสร็จ":
			data2=(ProjectG6.objects.get(id=s.Projectg7_id))
			dataset2.append(data2.name_thai)
			dataset2.append(date2)
		status2=""
	return render(request, 'group7/showlistcheck.html', {'data': dataset2})

def sumreq(request):
	status3=""
	date3=""
	dataset3=[]
	ordd3=Order.objects.all()
	count=[];
	c=0
	for s in ordd3:
		stat3=s.status_of_set.all()
		for r in stat3:
			c+=1
			status3=r.State.encode('utf-8')
			date3=str((r.Date).day)+"/"+month[(r.Date).month-1] +"/"+str((r.Date).year)
		if status3 == "ใบเบิกวัสดุ":
			count.append(c)
			data=(ProjectG6.objects.get(id=s.Projectg7_id))
			dataset3.append(data.name_thai)
			dataset3.append(date3)
		status3=""
	return render(request, 'group7/showlistrequi.html', {'data': dataset3,'c':count})
	
def summarypro(request):#หน้าแสดงรายงานรวม
	va_name = ProjectG6.objects.all()#เรียกรายชื่อโปรเจ็คทั้งหมด
	student_list2=[]
	project=[]
	member=[]
	count=0
	cost=[]
	summary=[]
	count2=0
	count3=0
	round=0
	buy=0
	check=0
	complete=0
	costtotal=[]
	pname=[]
	for s in va_name:#ลูปสำหรับเรียกค่า นศ และ ชื่อ โปรเจ็ค
		project.append(s)
		student_list2.append(s.student.all())
	
	for t in student_list2:#ลูปสำหรับนับจำนวนสมาชิก
		for r in t:
			count+=1
		member.append(count)
		count=0
	for u in member:#ลูปสำหรับคำนวณเงินที่ใช้ได้ในแต่ละโปรเจค
		cost.append(u*5000)
		
	for s in project:#ลูปสำหรับคำนวณเงินที่ใช้ได้ในแต่ละโปรเจคทีใช้ไปในปัจจุบัน
		order=Order.objects.all()#ลเก็ทรายการสั่งซื้อทั้งหมดออกมา
		for ord in order:
			if ord.Projectg7_id==s.id:
				status=ord.status_of_set.all()
				for i in status:
					if (i.Status).encode('utf-8') == "สมบูรณ์":#หากรายการสั่งซื้อนั้นสถานะสมบูรณ์จะนำเงินในใบสั่งซื้อมาคำนวณ
						costt=Orderinfo.objects.all()
						for cst in costt:
							if cst.Order_id==i.Order_id:
								round+=cst.Cost_total
		costtotal.append(round)
		round=0
		
	for s in project:#ลูปสำหรับเก็บค่าไปแสดงในหน้าแสดงผล
		pid=CategoriesProject.objects.get(project_id=s.id)
		summary.append(s.name_thai)
		summary.append(str(pid.project_catagories)+str(pid.year)+"-"+str(pid.semester)+"-"+str(pid.number))
		sum1='{:,.2f}'.format(cost[count2])
		sum2='{:,.2f}'.format(costtotal[count2])
		sum3=(cost[count2]-costtotal[count2])
		summary.append(sum1)
		summary.append(sum2)
		summary.append(sum3)
		count2+=1
	ordd=Order.objects.all()
	for s in ordd:
		stat=s.status_of_set.all()
		for r in stat:
			if (r.State).encode('utf-8') == "วันที่ในการซื้อวัสดุ":
				buy+=1
			elif (r.State).encode('utf-8') == "ตรวจสอบวัสดุและใบเสร็จ":
				check+=1
				buy-=1
				if buy<0: buy=0
			else:
				complete+=1
				check-=1
				if check<0:check=0
		
        return render(request, 'group7/sumallproject.html', {'cost':summary,'buy':buy,'check':check,'complete':complete})

def Orderedit(request,pk):
        stu = Order.objects.get(id=pk)
        now = stu.Date
	valid_date = datetime.datetime.strptime(str(now), '%Y-%m-%d').strftime('%d-%m-%Y')
        return render(request, 'group7/editorder.html', {'object':stu,'dates':valid_date})
   
def editOrder(request,info_id):
        date=request.GET.get('date')
	valid_date = datetime.datetime.strptime(str(date), '%d-%m-%Y').strftime('%Y-%m-%d')
	q=Order.objects.get(id=info_id) 
        p=Order(id=info_id,Projectg7_id=q.Projectg7_id,Date=valid_date)   	
	p.save()
        url="/group7/"+str(q.Projectg7_id)
        return HttpResponseRedirect(url)
