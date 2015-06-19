from django.shortcuts import render

def index(request):
    return render(request, 'group6/index.html')

def create_3forms(request):
    return render(request, 'group6/index.html')

def approveProject(request, apID):
    return render(request, 'group6/index.html')

def offerProject(request, opID):
    return render(request, 'group6/index.html')

def researchProject(request, rpID):
    return render(request, 'group6/index.html')
