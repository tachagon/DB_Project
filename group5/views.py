from django.shortcuts import render
from django.http import HttpResponse
from group5.models import *
from django.views import generic

# Create your views here.
def status(request):
    return render(request, 'group5/status.html')
def company(request):
    return render(request, 'group5/company.html')
def department_new(request):
    return render(request, 'group5/department_new.html')

class table(generic.ListView):
    template_name = 'group5/status.html'
    context_object_name = 'object'
    def get_queryset(self):
        return subporzaa.objects.order_by('subjectID')