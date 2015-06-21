from django.shortcuts import render
from group6.models import *

def index(request):
    return render(request, 'group6/index.html')

def create_3forms(request):
    #teachers = TeacherG6.objects.all()
    return render(request)#, 'group6/create_3forms.html', {'teachers': teachers,},)

def approveProject(request, apID):
    return render(request, 'group6/index.html')

def offerProject(request, opID):
    return render(request, 'group6/index.html')

def researchProject(request, rpID):
    return render(request, 'group6/index.html')


#django study view function Url /home (JA)
#def home(request):	# show all chapter in django study
#    personals = get_object_or_404(Personal,pk = get_id(request))	# get object id from  Personal id
#    chapter = Chapter.objects.order_by('unit')				# sort objects from title of each chapter
#    return render(request, 'home.html', {'chapter': chapter,'personals':personals, },)#return object with the result of the rendered template
