from django.shortcuts import render
from group3.models import *

# Create your views here.
def prof2lang_index(request):
    template = 'group3/prof2lang_index.html'    # get template
    prof2langList = Prof2Lang.objects.all()     # get all Prof2Lang objects

    return render(
        request,
        template,
        {'prof2langList': prof2langList}
    )