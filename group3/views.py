from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
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

def prof2lang_add(request, option = '0'):
    template = 'group3/prof2lang_add.html'
    # get all Prof2Lang objects
    prof2langObj = Prof2Lang.objects.all().order_by('shortName')
    # get all Subject objects
    subjectObj = Subject.objects.all().order_by('subjectID')

    # option 0 is get prof2lang_add web page
    if request.method == 'GET' and option == '0':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
        }
    # option 1 is add Prof2Lang object success
    elif option == '1':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
            'addProfSuccess': True,
        }
    # option 2 is add Prof2Lang object not success
    elif option == '2':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj' : subjectObj,
            'addProfError': True,
        }
    # option 3 is add Subject object success
    elif option == '3':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSubjectSuccess': True
        }
    # option 4 is add Subject object not success
    elif option == '4':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSubjectError': True
        }
    # option 5 is add Section object success
    elif option == '5':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSectionSuccess': True
        }
    # option 6 is add Section object not success
    elif option == '6':
        context = {
            'prof2langObj': prof2langObj,
            'subjectObj': subjectObj,
            'addSectionError': True
        }
    else:
        return prof2lang_index(request)



    return render(
        request,
        template,
        context
    )

# This function for get data and create new Prof2Lang object.
def addProf(request):
    if request.method == 'POST':
        # get data from html template
        profID      = request.POST['profID']
        firstName   = request.POST['firstName']
        lastName    = request.POST['lastName']
        shortName   = request.POST['shortName']
        tell        = request.POST['tell']
        email       = request.POST['email']
        sahakornAccount = request.POST['sahakornAccount']
        department  = request.POST['department']
        faculty     = request.POST['faculty']

        try:
            # create new Prof2Lang object
            newProf = Prof2Lang(
                profID = profID,
                firstName = firstName,
                lastName = lastName,
                shortName = shortName,
                tell = tell,
                email = email,
                sahakornAccount = sahakornAccount,
                department = department,
                faculty = faculty
            )
            # save new Prof2Lang object into database
            newProf.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['1']))
        except Exception, e:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['2']))

# This function for get data and create new Subject object.
def addSubject(request):
    if request.method == 'POST':
        try:
            # get data from HTML template
            subjectID = request.POST['subjectID']
            subjectName = request.POST['subjectName']

            # create new Subject object
            newSubject = Subject(
                subjectID = subjectID,
                subjectName = subjectName
            )
            # save new Subject object into database
            newSubject.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['3']))
        except:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['4']))

# This function for get data and create new Section object
def addSection(request):
    if request.method == 'POST':
        try:
            # get data from HTML template
            section = request.POST['section']
            subject = request.POST['subject']
            classroom = request.POST['classroom']
            startTime_hour = request.POST['startTime_hour']
            startTime_minute = request.POST['startTime_minute']
            endTime_hour = request.POST['endTime_hour']
            endTime_minute = request.POST['endTime_minute']
            date = request.POST['date']

            # create startTime
            startTime = startTime_hour + ":" + startTime_minute + ":" + "00"
            # create endTime
            endTime = endTime_hour + ":" + endTime_minute + ":" + "00"
            # get Subject object that selected
            subjectObj = Subject.objects.get(subjectID = subject)

            # create new Section object
            newSection = Section(
                section = section,
                subject = subjectObj,
                classroom = classroom,
                startTime = startTime,
                endTime = endTime,
                date = date
            )
            # save new Section object into database
            newSection.save()
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['5']))
        except:
            return HttpResponseRedirect(reverse('group3:prof2lang_add', args=['6']))
