from django.shortcuts import render
from group3.models import *

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

def prof2lang_add(request):
    template = 'group3/prof2lang_add.html'
    
    return render(
        request,
        template,
        {}
    )
