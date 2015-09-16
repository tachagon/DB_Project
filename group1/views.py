from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    template = 'group1/index.html'
    context = RequestContext(request)
    
    return render_to_response(
        template,
        {},
        context
    )

#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from group1.models import Document, Category, Personal, Document_modify
from login.models import UserProfile
from group1.forms import DocumentForm



def upload_file(request):

    # Handle file upload

    # Load categories for the list page

    category = Category.objects.all()
    persons = UserProfile.objects.all()
    modify = Personal.objects.all()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        name_file = request.POST.get('name_file')
        category_file = request.POST.get('category_name')
        dept_file = request.POST.get('name_dept')	
        month_file = request.POST.get('month_file')
        date_file = request.POST.get('date_file')
        year_file = request.POST.get('year_file')
        number_file = request.POST.get('number_file')
        number_file2 = request.POST.get('number_file2')
        detail1_file = request.POST.get('detail1_file')
        detail2_file = request.POST.get('detail2_file')
        detail3_file = request.POST.get('detail3_file')
        detail4_file = request.POST.get('detail4_file')
        docfrom_file = request.POST.get('docfrom_file')
        user_doc = request.POST.get('user_doc')
        pres_email = request.POST.getlist('pers_email[]')
	
	    # Redirect to upload page if category is none
        if category_file == '':
            return render_to_response('group1/upload.html', 
				{'persons':persons, 'category': category, 'name_file':name_file, 'year_file':year_file, 'modify': modify,
                                 'number_file2':number_file2, 'number_file':number_file, 'form':form, 'msg':204 },
                              	context_instance=RequestContext(request))


        if form.is_valid():
            try:
		cate = None
		print category_file
		if category_file == '-':
			cate = Category.objects.get(name="-")					
		else:
			try:
				cate = Category.objects.get(name=category_file)
			except:
				return render_to_response('group1/upload.html', 
				{'persons':persons, 'category': category, 'name_file':name_file, 'year_file':year_file, 'modify': modify,
                                 'number_file2':number_file2, 'number_file':number_file, 'form':form, 'msg':204 },
                              	context_instance=RequestContext(request))
				
                if(Document.objects.filter(year=year_file, number= number_file)):
                    msg = 202

                    return render_to_response('group1/upload.html',{ 'persons': persons, 'category':category, 'modify': modify,
                                            'name_file':name_file, 'year_file':year_file, 'number_file2':number_file2,
                                            'number_file':number_file, 'msg':msg},context_instance=RequestContext(request))	   
		
                newdoc = Document(docfile=request.FILES['docfile'],
                                name=name_file, addby = user_doc,
                                category=cate, dept = dept_file, added = date_file+"/"+month_file+"/"+year_file,
                                year=year_file, number=number_file, number2=number_file2,
                                detail1=detail1_file, detail2=detail2_file, detail3=detail3_file, detail4=detail4_file
                )
                newdoc.save()
                for preson_in in pres_email:
			if preson_in != "":		
				newdoc.userProfile.add(UserProfile.objects.get(id=preson_in))

		# Load documents for the list page
		documents = Category.objects.get(name=category_file)
                documents = documents.document_set.all()
                documents = documents.filter(year=year_file)
                documents = documents.filter(name=name_file)
                documents = documents.filter(number=number_file)
                documents = documents.filter(number2=number_file2)

                return render_to_response('group1/search.html', {'form': form,'persons':persons, 'modify': modify,
					'category': category, 'name_file':name_file, 'year_file':year_file,
					'number_file':number_file, 'number_file2':number_file2, 'msg':200, 'documents':documents},
					context_instance=RequestContext(request))
            except:

                # Redirect to upload page
                return render_to_response('group1/upload.html', {'form': form,'persons':persons, 'modify': modify,
                                          'category': category, 'name_file':name_file, 'year_file':year_file,
                                          'number_file':number_file, 'number_file2':number_file2, 'msg': 201},
                                          context_instance=RequestContext(request))
        else:
            form = DocumentForm()  # A empty, unbound form
            return render_to_response('group1/upload.html', {'form': form,'persons':persons,'category': category,'name_file':name_file,
                                      'year_file':year_file, 'number_file':number_file, 'number_file2':number_file2, 'msg': 203, 'modify': modify,
                                      'error_msg_upload':"***Please select file***"},context_instance=RequestContext(request))	    

    form = DocumentForm()  # A empty, unbound form
    # Render list page with the documents and the form

    return render_to_response('group1/upload.html', {'form': form,'persons':persons, 'modify': modify,
                              'category': category},
                              context_instance=RequestContext(request))

########################################################################################


def search_file(request):

    # Handle file search

    # Load categories for the list page....
    category = Category.objects.all()
    modify = Personal.objects.all()

    if request.method == 'POST':        
        name_file = request.POST.get('name_file')
        dept_file = request.POST.get('name_dept')
        category_file = request.POST.get('category_name')
        month_file = request.POST.get('month_file')
        year_file = request.POST.get('year_file')
        number_file = request.POST.get('number_file')
        number_file2 = request.POST.get('number_file2')
        mail_sended = request.POST.get('mail_sended')
        
        if name_file != '':
            documents = Document.objects.filter(name__contains=name_file)
        else:
            documents = Document.objects.all()

        if category_file != '' and category_file != None:
            documents = documents.filter(category=Category.objects.get(name__contains=category_file))

        if dept_file != '' and dept_file != None:
            documents = documents.filter(dept__contains=dept_file)

        if month_file != '':	
            documents = documents.filter(added__contains="/"+month_file+"/")

        if year_file != '' and year_file != None:
            documents = documents.filter(year=year_file)

        if number_file != '' and number_file != None:
            documents = documents.filter(number=number_file)

        if number_file2 != '' and number_file != None:
            documents = documents.filter(number2=number_file2)

        if mail_sended != '':
            documents = documents.filter(send_status=mail_sended)
        print documents
        return render_to_response('group1/search.html',
                                  {'documents': documents, 'modify': modify, 'category': category},
                                   context_instance=RequestContext(request))
    
    return render_to_response('group1/search.html', {'modify': modify, 'category': category},
                              context_instance=RequestContext(request))

########################################################################################

def edit_file(request, doc_id):
    document = Document.objects.get(id=doc_id)
    categories = Category.objects.all();
    cate = Category.objects.get(id=document.category.id)
    persons = UserProfile.objects.all()
    modify = Personal.objects.all()
    return render_to_response('group1/edit.html', {'document': document, 'modify': modify, 'modify_history': document.document_modify_set.all(), 'categories':categories, 'category_name':cate, 'persons':persons},context_instance=RequestContext(request))

def edit_this_file(request):
    categories = Category.objects.all();
    persons = UserProfile.objects.all()
    modify = Personal.objects.all()
	
    if request.method == 'POST':
        try:
            doc_id = request.POST.get('document_id')
	    user_doc = request.POST.get('user_doc')
            name_file = request.POST.get('name_file')
            category_file = request.POST.get('category_name')
            month_file = request.POST.get('month_file')
            date_file = request.POST.get('date_file')
            year_file = request.POST.get('year_file')
            number_file = request.POST.get('number_file')
            number_file2 = request.POST.get('number_file2')
            detail1_file = request.POST.get('detail1_file')
            detail2_file = request.POST.get('detail2_file')
            detail3_file = request.POST.get('detail3_file')
            detail4_file = request.POST.get('detail4_file')
            docfrom_file = request.POST.get('docfrom_file')
            pres_email = request.POST.getlist('pers_email[]')
            document = Document.objects.get(id=doc_id)
            dept_file = request.POST.get('name_dept')
	    if category_file==None:
		cate = Category.objects.get(name="-")
	    else:
            	cate = Category.objects.get(name=category_file)
		
            if(len(Document.objects.filter(year=document.year, number= number_file))>1):
                msg = 202
                return render_to_response('group1/edit.html',{ 'document': document, 'modify': modify, 'categories':categories, 'cate':cate, 'persons':persons, 'msg':msg, 'modify_history': document.document_modify_set.all()},context_instance=RequestContext(request))
	  
            document.name = name_file
            document.category = cate	   
            document.dept = dept_file
            document.number = number_file
            document.number2 = number_file2	   
            document.detail1 = detail1_file
            document.detail2 = detail2_file	    
            document.detail3 = detail3_file
            document.detail4 = detail4_file
            document.userProfile.clear()
	    
	    modify = Document_modify(modifyby=user_doc, modified=date_file+"/"+month_file+"/"+year_file, document=document);	
	    modify.save()
 	    
	   
	    for preson_in in pres_email:
		if preson_in!="":
		    if preson_in == "person_all":
			for u_profile in UserProfile.objects.all():
			    document.userProfile.add(u_profile)
			break		
		    document.userProfile.add(UserProfile.objects.get(id=preson_in))
	    
            document.save()
            msg = 200

        except:
            msg = 201
    return render_to_response('group1/edit.html',{ 'document': document, 'modify': modify, 'categories':categories, 'cate':cate, 'dept_file': dept_file,'persons':persons, 'msg':msg, 'modify_history': document.document_modify_set.all()},context_instance=RequestContext(request))

########################################################################################

def send_email(request, doc_id):
	document = Document.objects.get(id=doc_id)
	modify = Personal.objects.all()
	return render_to_response('group1/send.html', {'modify': modify, 'document': document},context_instance=RequestContext(request))

def sender(request):
	
	modify = Personal.objects.all()
	
	if request.method == 'POST':
		doc_id = request.POST.get('doc_id')
		comment = request.POST.get('comment')
		name_email = request.POST.get('name_email')
	
		print (comment)
	
		document = Document.objects.get(id=doc_id)
		personals = document.userProfile.all()
		send_to = []
	
		for per in personals:
			send_to.append(per.user.email)
	
		# Build message
		email = EmailMessage(subject=name_email, body=comment, from_email='documentece01@gmail.com',to=send_to, headers = {'Reply-To': 'documentece01@gmail.com'})
	
		# Open file
		attachment = open(u'media/'+document.docfile.name, 'rb')
	
		# Attach file
		email.attach("attach_file.pdf", attachment.read(),'application/pdf')
	
		# Send message with built-in send() method
		email.send()

	document.send_status = 1
	document.save()
		
        return render_to_response('group1/send.html', {'document': document, 'modify': modify, 'msg': 200} ,
                              context_instance=RequestContext(request))    

	return render_to_response('group1/send.html', {'document': document, 'modify': modify} ,
                              context_instance=RequestContext(request))

########################################################################################

def add_category(request):
	categories = Category.objects.all()
	modify = Personal.objects.all()
	if request.method == 'POST':
		category_name = request.POST.get('category_name')

		category = Category(name = category_name)
		category.save()

		return render_to_response('group1/category.html', {'msg':200, 'modify': modify, 'category':category, 'categories':categories},
							  context_instance=RequestContext(request))        
	return render_to_response('group1/category.html', {'categories':categories, 'modify': modify}, context_instance=RequestContext(request))

########################################################################################

def add_people(request):
	persons = Personal.objects.all()
	
	if request.method == 'POST':
		people_name = request.POST.get('p_name')
		people_username = request.POST.get('p_username')

		personal = Personal(name = people_name, username = people_username)
		personal.save()

		return render_to_response('group1/people.html', {'msg':200, 'persons':persons,
                                         'people_name': people_name, 'people_username': people_username
                                         }, context_instance=RequestContext(request))
	return render_to_response('group1/people.html', {'persons':persons                                 
                                  }, context_instance=RequestContext(request))
