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

from group1.models import Document, Category, Personal
from login.models import UserProfile
from group1.forms import DocumentForm

#######################################################################################################################

def upload_file(request):

    # Handle file upload

    # Load categories for the list page

    category = Category.objects.all()
    persons = Personal.objects.all()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        name_file = request.POST.get('name_file')
        category_file = request.POST.get('category_file')
        year_file = request.POST.get('year_file')
        number_file = request.POST.get('number_file')
        number_file2 = request.POST.get('number_file2')
        detail1_file = request.POST.get('detail1_file')
        detail2_file = request.POST.get('detail2_file')
        detail3_file = request.POST.get('detail3_file')
        detail4_file = request.POST.get('detail4_file')
        pres_email = request.POST.getlist('pers_email[]')
	

	# Redirect to search page
        if category_file == 'none' or category_file == '':
            return render_to_response('group1/upload.html', 
				{'persons':persons, 'category': category, 'name_file':name_file, 'year_file':year_file,
                                 'number_file2':number_file2, 'number_file':number_file,
                                 'error_msg_upload':"***Please insert all data***" },
                              	context_instance=RequestContext(request))


        if form.is_valid():
                try:
                    cate = Category.objects.get(code_name=category_file)	   
	
                    newdoc = Document(docfile=request.FILES['docfile'],
		                      name=name_file,
		                      category=cate,
		                      year=year_file, number=number_file, number2=number_file2,
				      detail1=detail1_file, detail2=detail2_file, detail3=detail3_file, detail4=detail4_file
                                     )
                    category_code = category_file
                    category_name = cate.name
                    newdoc.save()

                    for preson_in in pres_email:
                        if preson_in != "":			
                            newdoc.personal.add(Personal.objects.get(name=preson_in.split(':')[0]))

		     # Load documents for the list page
                    documents = Category.objects.get(code_name=category_file)
                    documents = documents.document_set.all()
                    documents = documents.filter(year=year_file)
                    documents = documents.filter(name=name_file)
                    documents = documents.filter(number=number_file)
                    documents = documents.filter(number2=number_file2)

                    return render_to_response('group1/search.html', {'form': form,'persons':persons,
		                      'category': category,  'documents':documents},
		                      context_instance=RequestContext(request))
                except:


            		# Redirect to upload page

                    return render_to_response('group1/upload.html', {'form': form,'persons':persons,
		                      'category': category, 'name_file':name_file, 'year_file':year_file,
                                      'number_file':number_file, 'number_file2':number_file2,
#                                      'detail5_file':detail5_file,
                                      'error_msg_upload':"***Insert data error***",
                                      'category_code':category_code, 'category_name':category_name},
		                      context_instance=RequestContext(request))
        else:
            form = DocumentForm()  # A empty, unbound form
            return render_to_response('group1/upload.html', {'form': form,'persons':persons,'category': category, 'name_file':name_file,
                                      'year_file':year_file, 'number_file':number_file, 'number_file2':number_file2,
                                      'error_msg_upload':"***Please insert all data***"},context_instance=RequestContext(request))	    

    form = DocumentForm()  # A empty, unbound form
    # Render list page with the documents and the form

    return render_to_response('group1/upload.html', {'form': form,'persons':persons,
                              'category': category},
                              context_instance=RequestContext(request))


#######################################################################################################################

def search_file(request):

    # Handle file search

    # Load categories for the list page....
    category = Category.objects.all()
    persons = Personal.objects.all()

    if request.method == 'POST':
        name_file = request.POST.get('name_file')
        category_file = request.POST.get('category_file')
        year_file = request.POST.get('year_file')
        number_file = request.POST.get('number_file')
        number_file2 = request.POST.get('number_file2')
        detail5_file = request.POST.get('detail5_file')

        
        if name_file != '':
            documents = Document.objects.filter(name__contains=name_file)
        else:
            documents = Document.objects.all()

        if category_file != '':
            documents = documents.filter(category=Category.objects.get(code_name=category_file))

        if year_file != '':
            documents = documents.filter(year=year_file)

        if number_file != '':
            documents = documents.filter(number=number_file)

        if number_file2 != '':
            documents = documents.filter(number2=number_file2)

        if detail5_file != '':
            documents = documents.filter(category=Category.objects.filter(depart=detail5_file))

        
        return render_to_response('group1/search.html',
                                  {'documents': documents, 'category': category},
                                  context_instance=RequestContext(request))
    
    return render_to_response('group1/search.html', {'category': category, 'persons':persons},
                              context_instance=RequestContext(request))

#######################################################################################################################

def send_email(request, doc_id):
	document = Document.objects.get(id=doc_id)
	return render_to_response('group1/send.html', {'document': document},context_instance=RequestContext(request))

#######################################################################################################################

def sender(request):
	
    if request.method == 'POST':
	doc_id = request.POST.get('doc_id')
        comment = request.POST.get('comment')
        name_email = request.POST.get('name_email')

	document = Document.objects.get(id=doc_id)
	personals = document.personal.all()
	send_to = []
	for per in personals:
		send_to.append(per.email)

   	# Build message
    	email = EmailMessage(subject=name_email, body=comment, from_email='documentece01@gmail.com',to=send_to, headers = {'Reply-To': 'documentece01@gmail.com'})

    	# Open file
    	attachment = open(u''+document.docfile.name, 'rb')

    	# Attach file
    	email.attach("attach_file.pdf", attachment.read(),'application/pdf')

    	# Send message with built-in send() method
    	email.send()
	msg_ok = "Send message success"
    	print('Send message success')    
    
    return render_to_response('group1/send.html', {'document': document, 'msg_ok': msg_ok} ,
                              context_instance=RequestContext(request))
							  
###################################################################################################

def add_category(request):
    
    category = Category.objects.all()
    
    if request.method == 'POST':
        name_file = request.POST.get('category_name')
        detail5_file = request.POST.get('detail5_file')

        for i in range (1, 101):
            if not(Category.objects.filter(code_name=i)):
                break

        newdoc = Category(code_name=i, name=name_file, depart=detail5_file)
        newdoc.save()

        return render_to_response('group1/category.html', {
                                      'category': category},
		                      context_instance=RequestContext(request))
    
    return render_to_response('group1/category.html',
                              {'category': category},
                              context_instance=RequestContext(request))
                              
####################################################################################################
def add_people(request):
    
    persons = Personal.objects.all()

    if request.method == 'POST':
        t_name_file = request.POST.get('t_name_file')
        t_code_name = request.POST.get('t_code_name')
        email_file = request.POST.get('email_file')
        	
        newdoc = Personal(code_name=t_code_name, name=t_name_file, email=email_file)
        newdoc.save()

        return render_to_response('group1/people.html', {
                                      'persons': persons},
		                      context_instance=RequestContext(request))
    
    return render_to_response('group1/people.html',
                              {'persons': persons},
                              context_instance=RequestContext(request))

#############################################################################################
                              
def edit(request):
    
    return render_to_response('group1/edit.html',
                              context_instance=RequestContext(request))
                              
#############################################################################################
                              
def delete(request):

    documents = Document.objects.all()

##    if request.method == 'POST':
##        name_file = request.POST.get('name_file')
##
##        Document.objects.filter(name=name_file).delete()
##
##        return render_to_response('group1/search.html',
##                              context_instance=RequestContext(request))
    
    return render_to_response('group1/delete.html',{'documents': documents},
                              context_instance=RequestContext(request))
