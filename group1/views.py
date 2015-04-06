from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'group1/index.html'
    context = RequestContext(request)
    
    return render_to_response(
        template,
        {},
        context
    )