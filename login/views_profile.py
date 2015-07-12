#-*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from login.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

########################################### Information of User Profile ################################################
# this function for profile index that show information of current user
# Usage: login:profile_index
def index(request, context={}):
    template = 'login/profile/index.html'

    try:
        user = request.user
        userprofile = UserProfile.objects.get(user = user)

        context['userprofile'] = userprofile
        context['profile_index'] = 'active'
    except:
        pass
    return render(request, template, context)

# this function for edit firstname_th and lastname_th
# Usage: login:profile_editThaiName
def editThaiName(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            firstname_th    = request.POST['firstname_th']
            lastname_th     = request.POST['lastname_th']

            # update date
            userprofile.firstname_th    = firstname_th
            userprofile.lastname_th     = lastname_th
            # save change
            userprofile.save()

            context['success'] = 'เปลี่ยนชื่อเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนชื่อได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit firstname_en and lastname_en
# Usage: login:profile_editEngName
def editEngName(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            firstname_en    = request.POST['firstname_en']
            lastname_en     = request.POST['lastname_en']

            # update date
            user.first_name             = firstname_en
            user.last_name              = lastname_en
            userprofile.firstname_en    = firstname_en
            userprofile.lastname_en     = lastname_en
            # save change
            user.save()
            userprofile.save()

            context['success'] = 'เปลี่ยนชื่อเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนชื่อได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit username
# Usage: login:profile_editUsername
def editUsername(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user

            # get data from template
            username = request.POST['username']

            try:
                test = User.objects.get(username = username)
                errors.append('username นี้มีผู้อื่นใช้แล้ว')
                context['errors'] = errors
                return index(request, context)
            except:
                pass

            # update date
            user.username = username
            # save change
            user.save()

            context['success'] = 'เปลี่ยน username เรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถใช้ username นี้ได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit email
# Usage: login:profile_editEmail
def editEmail(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user

            # get data from template
            email = request.POST['email']

            # update date
            user.email = email
            # save change
            user.save()

            context['success'] = 'เปลี่ยน E-mail เรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยน E-mail นี้ได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit tel
# Usage: login:profile_editTel
def editTel(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            tel     = request.POST['tel']
            ext     = request.POST['ext']

            # update date
            userprofile.tel     = tel
            userprofile.ext     = ext
            # save change
            userprofile.save()

            context['success'] = 'เปลี่ยนเบอร์โทรศัพท์เรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนเบอร์โทรศัพท์ได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit address of user profile
# Usage: login:profile_editAddress
def editAddress(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            address = request.POST['address']

            # update date
            userprofile.address = address
            # save change
            userprofile.save()

            context['success'] = 'เปลี่ยนที่อยู่เรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนที่อยู่ได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit office of user profile
# Usage: login:profile_editOffice
def editOffice(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            office = request.POST['office']

            # update date
            userprofile.office = office
            # save change
            userprofile.save()

            context['success'] = 'เปลี่ยนที่ทำงานเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนที่ทำงานได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit account number of user profile
# Usage: login:profile_editAccount
def editAccount(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            account = request.POST['account']

            # update date
            userprofile.account = account
            # save change
            userprofile.save()

            context['success'] = 'เปลี่ยนเลขที่บัญชีเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนเลขที่บัญชีได้')
            context['errors'] = errors

    return index(request, context)

# this function for edit password
# Usage: login:profile_editPassword
def editPassword(request):
    template = 'login/profile/change_password.html'
    context = {}
    errors = []
    error = False

    try:
        user = request.user
        userprofile = UserProfile.objects.get(user = user)

        context['userprofile'] = userprofile
    except:
        pass

    context['profile_change_password'] = 'active'

    if request.method == 'POST':
        # get data from template
        currentPassword     = request.POST['cPass']
        newPassword         = request.POST['nPass']
        newPasswordAgain    = request.POST['nPassAgain']

        # check current password is correct
        if not request.user.check_password(currentPassword):
            errors.append('รหัสผ่านปัจจุบันไม่ถูกต้อง')
            error = True
        # check new password is correct
        if newPassword != newPasswordAgain:
            errors.append('รหัสผ่านใหม่กรอกไม่ตรงกัน')
            error = True

        if error:
            context['errors'] = errors
        else:
            try:
                user = request.user
                user.set_password(newPassword)
                user.save()
                context['success'] = 'เปลี่ยนรหัสผ่านเรียบร้อยแล้ว'

                user = authenticate(username=user.username, password=newPassword)
                login(request, user)
            except:
                errors.append('เปลี่ยนรหัสผ่านไม่สำเร็จ')
                context['errors'] = errors

    return render(request, template, context)

# this function for edit prefix_name of user profile
# Usage: login:profile_editPrefixName
def editPrefixName(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)

            # get data from template
            prefix_name = request.POST['prefix_name']

            # update date
            userprofile.prefix_name = prefix_name
            # save change
            userprofile.save()

            context['success'] = 'เปลี่ยนคำนำหน้าชื่อเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนคำนำหน้าชื่อได้')
            context['errors'] = errors

    return index(request, context)

########################################## END of Information User Profile #############################################

########################################## Information of Student Profile ##############################################
# this fuction for show information of current student profile
# Usage: login:profile_student
def student(request, context={}):
    template = 'login/profile/profile_student.html'

    try:
        user = request.user
        userprofile = UserProfile.objects.get(user = user)

        # user is Student
        if userprofile.type == '0':
            student = Student.objects.get(userprofile = userprofile)
            context['student'] = student
        # user is not Student
        else:
            return HttpResponseRedirect(reverse('login:profile_index'))
        context['userprofile'] = userprofile
        context['profile_student'] = 'active'
    except:
        pass

    return render(request, template, context)
######################################### END of Information Student Profile ###########################################

########################################### Information of Teacher Profile #############################################
# this function for show information of current teacher profile
# Usage: login:profile_teacher
def teacher(request, context={}):
    template = 'login/profile/profile_teacher.html'

    try:
        user = request.user
        userprofile = UserProfile.objects.get(user = user)

        # user is Teacher
        if userprofile.type == '1':
            teacher = Teacher.objects.get(userprofile = userprofile)
            context['teacher'] = teacher
        # user is not Student
        else:
            return HttpResponseRedirect(reverse('login:profile_index'))
        context['userprofile'] = userprofile
        context['profile_teacher'] = 'active'
    except:
        pass

    return render(request, template, context)

# this function for edit prefix_name and academic_position of Teacher profile
# Usage: login:profile_editPrefix
def editPrefix(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)
            # get current teacher profile
            teacherObj = Teacher.objects.get(userprofile = userprofile)

            # get data from template
            prefix = request.POST['prefix']

            # update date
            if prefix == '0': # select อาจารย์
                userprofile.prefix_name = '4'
                teacherObj.academic_position = '0'
            elif prefix == '1': # select ดร.
                userprofile.prefix_name = '3'
                teacherObj.academic_position = '0'
            elif prefix == '2':# select ผศ.
                userprofile.prefix_name = '4'
                teacherObj.academic_position = '1'
            elif prefix == '3':# select รศ.
                userprofile.prefix_name = '4'
                teacherObj.academic_position = '2'
            elif prefix == '4':# select ศ.
                userprofile.prefix_name = '4'
                teacherObj.academic_position = '3'
            elif prefix == '5':# select ผศ.ดร.
                userprofile.prefix_name = '3'
                teacherObj.academic_position = '1'
            elif prefix == '6':# select รศ.ดร.
                userprofile.prefix_name = '3'
                teacherObj.academic_position = '2'
            elif prefix == '7':# select ศ.ดร.
                userprofile.prefix_name = '3'
                teacherObj.academic_position = '3'

            # save change
            userprofile.save()
            teacherObj.save()

            context['success'] = 'เปลี่ยนคำนำหน้าชื่อเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนคำนำหน้าชื่อได้')
            context['errors'] = errors

    return teacher(request, context)

# this function for edit shortname of teacher profile
# Usage: login:profile_editShortname
def editShortname(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)
            # get current teacher profile
            teacherObj = Teacher.objects.get(userprofile = userprofile)

            # get data from template
            shortname = request.POST['shortname']

            # convert shortname to UPPER case
            shortname = str(shortname).upper()

            # check shortname is duplicate
            if teacherObj.shortname != shortname:
                try:
                    test = Teacher.objects.get(shortname = shortname)
                    errors.append('ตัวย่อชื่อนี้มีผู้อื่นใช้แล้ว')
                    context['errors'] = errors
                    return teacher(request, context)
                except:
                    pass

            # update date
            teacherObj.shortname = shortname

            # save change
            teacherObj.save()

            context['success'] = 'เปลี่ยนตัวย่อชื่อเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนตัวย่อชื่อได้')
            context['errors'] = errors

    return teacher(request, context)

# this function for edit position of teacher profile
# Usage: login:profile_editTeacherPosition
def editTeacherPosition(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)
            # get current teacher profile
            teacherObj = Teacher.objects.get(userprofile = userprofile)

            # get data from template
            position = request.POST['position']

            # update date
            teacherObj.position = position

            # save change
            teacherObj.save()

            context['success'] = 'เปลี่ยนตำแหน่งเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนตำแหน่งได้')
            context['errors'] = errors

    return teacher(request, context)
######################################### END of Information Teacher Profile ###########################################

########################################## Information of Officer profile ##############################################
# this function for show information of current officer profile
# Usage: login:profile_officer
def officer(request, context={}):
    template = 'login/profile/profile_officer.html'

    try:
        user = request.user
        userprofile = UserProfile.objects.get(user = user)

        # user is Officer
        if userprofile.type == '2':
            officer = Officer.objects.get(userprofile = userprofile)
            context['officer'] = officer
        # user is not Student
        else:
            return HttpResponseRedirect(reverse('login:profile_index'))
        context['userprofile'] = userprofile
        context['profile_officer'] = 'active'
    except:
        pass

    return render(request, template, context)

# this function for edit position of teacher profile
# Usage: login:profile_editOfficerPosition
def editOfficerPosition(request):
    context = {}
    errors = []

    if request.method == 'POST':
        try:
            # get current user
            user = request.user
            # get current user profile
            userprofile = UserProfile.objects.get(user = user)
            # get current teacher profile
            officerObj = Officer.objects.get(userprofile = userprofile)

            # get data from template
            position = request.POST['position']

            # update date
            officerObj.position = position

            # save change
            officerObj.save()

            context['success'] = 'เปลี่ยนตำแหน่งเรียบร้อยแล้ว'
        except:
            errors.append('ไม่สามารถเปลี่ยนตำแหน่งได้')
            context['errors'] = errors

    return officer(request, context)
######################################### END of Information Officer Profile ###########################################