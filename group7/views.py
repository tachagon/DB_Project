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


def home(request):
	stu = ProjectG6.objects.all()
        teacher=[]
        for name in stu:
            teacher.append(Teacher.objects.get(id=name.teacher_id))
            
        return render(request, 'group7/home.html', {'object': stu,'teacher':teacher})
                
def order(request,pk):
	project = ProjectG6.objects.get(id=pk)
        teacher=Teacher.objects.get(id=project.teacher_id)
        return render(request, 'group7/order.html', {'object': project,'teacher':teacher})
class addorder(generic.DetailView):
	model=ProjectG6
        template_name='group7/addorder.html'


        
def addorderview(request, pk):
	date=request.POST['date']
	valid_date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
        p=Order(Projectg7_id=pk,Date=valid_date)   	
	p.save()
        url="/group7/"+pk
        return HttpResponseRedirect(url)
#----------------------------- Orderinfo -------------------------------------------#
def orderinfo(request,pk):
        s = Order.objects.get(id=pk)
        info=s.orderinfo_set.all()
        sum=0
        for price in info:
            sum+=price.Cost_total
        return render(request, 'group7/orderinfo.html', {'object': info,'sum':sum,'s':s})

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
        sum=int(price)*int(amount)
        p=Orderinfo(Order_id=pk,Item_name=itemname, Amount=amount,Company=company,OrderID=id, Cost=price, Cost_total=sum)   	
	p.save()
        url="/group7/"+pk+"/orderinfo/"
        return HttpResponseRedirect(url)
#----------------------------- StatusOf -------------------------------------------#
class statusof(generic.DetailView):
	model=Order
   	template_name= 'group7/statusof.html'
# Create your views here.
def addstatusview(request,pk):
        order=Order.objects.get(id=pk)
	stat=order.status_of_set.all()
	laststat=""
	id=pk
	for s in stat:
		laststat=s.State
	return render(request, 'group7/addstatusof.html', {'object': laststat,'id':id})
	
	
	
def addstatus(request,pk):
    date=request.GET.get('date')
    valid_date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
    state = request.GET.get('state_status')
    more=request.GET.get('more')
    status=""
    if (request.GET.get('requisition_id')!=""):
        reqid=request.GET.get('requisition_id')
	req=Requisition(Status_of_id=pk,Requisition_Id=reqid)
	req.save()
    if (request.GET.get('state_status')=="complete"):
        status="สมบูรณ์"
        state="ใบเบิกวัสดุ"
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
            
        return render(request, 'group7/editorderinfo.html', {'object': stu})
    
    
def editOrderinfo(request,info_id): #Page Orderinfo for delete Orderinfo
        itemname=request.GET.get('itemname_orderinfo')
	amount=request.GET.get('amount_orderinfo')
	price=request.GET.get('price_orderinfo')
        company=request.GET.get('company')
        id=request.GET.get('id')
        sum=int(price)*int(amount)
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
	reqid=[]
	r=order.requisition_set.all() 
	for i in r: 
		reqid.append(i) 
	stat4=order.status_of_set.all()
	moreabout=""
	for r in stat4:
		status4=r.State.encode('utf-8')
		date4=r.Date
		moreabout=r.Moreabout
	if status4 == "ใบเบิกวัสดุ":
		now=date4
	project=ProjectG6.objects.get(id=order.Projectg7_id)
        return render(request, 'group7/requisitionview.html', {'order': order,'project':project,'date':now,'req':reqid,'more':moreabout})

def vieworderprint(request,pk):
        now = datetime.datetime.now()
        
	order = Order.objects.get(id=pk)
        project=ProjectG6.objects.get(id=order.Projectg7_id)
        stu = ProjectG6.objects.all()
        teacher=[]
	student=[]
        for name in stu:
                teacher.append(Teacher.objects.get(id=name.teacher_id))
	namestd=project.student.all()
	for std in namestd:
		student.append(std)
        return render(request, 'group7/orderinfoview.html', {'order': order,'teacher':teacher,'project':project,'date':now,'student':student})
        
def statusofedit(request,pk):
        stu=Status_Of.objects.get(id=pk)
        return render(request, 'group7/editstatusof.html', {'object': stu})
        
def editstatusof(request,info_id): #Page Orderinfo for delete Orderinfo
	date=request.GET.get('date')
	valid_date = datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
    	state = request.GET.get('state_status')
    	more=request.GET.get('more')
    	status=""
    	if (request.GET.get('state_status')=="complete"):
        	status="สมบูรณ์"
        	state="ใบเบิกวัสดุ"
    	else:
        	status="ไม่สมบูรณ์"
	q=Status_Of.objects.get(id=info_id)
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
			date=r.Date
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
			date2=r.Date
			
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
			
			date3=r.Date
		if status3 == "ใบเบิกวัสดุ":
			count.append(c)
			data=(ProjectG6.objects.get(id=s.Projectg7_id))
			dataset3.append(data.name_thai)
			dataset3.append(date3)
		status3=""
	return render(request, 'group7/showlistrequi.html', {'data': dataset3,'c':count})
	
def summarypro(request):
	va_name = ProjectG6.objects.all()
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
	for s in va_name:
		project.append(s)
		student_list2.append(s.student.all())
	
	for t in student_list2:
		for r in t:
			count+=1
		member.append(count)
		count=0
	for u in member:
		cost.append(u*5000)
		
	for s in project:
		order=Order.objects.all()
		for ord in order:
			if ord.Projectg7_id==s.id:
				status=ord.status_of_set.all()
				for i in status:
					if (i.Status).encode('utf-8') == "สมบูรณ์":
						costt=Orderinfo.objects.all()
						for cst in costt:
							if cst.Order_id==i.Order_id:
								round+=cst.Cost_total
		costtotal.append(round)
		round=0
		
	for s in project:
		summary.append(s.name_thai)
		summary.append(cost[count2])
		summary.append(costtotal[count2])
		summary.append(cost[count2]-costtotal[count2])
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
