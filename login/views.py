#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from login.forms import *
from login.models import *
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    template = 'login/index.html'
    context = RequestContext(request)
    registered = False
    errors=[]

    if request.method == 'POST':
        users = User.objects.all()  # get all User objects
        # get data from register_form
        username = request.POST['username']     # get username
        first_name = request.POST['first_name'] # get first name
        last_name = request.POST['last_name']   # get last name
        email = request.POST['email']           # get email
        password = request.POST['password']     # get password
        check_password = request.POST['check_password'] # get check_password
        if password != check_password:
            print 'password incorrected'
            errors.append(1)            # show some error message in template
        else:
            print 'password corrected'
            for user in users:                  # check user is duplicate
                if(username == user.username):
                    errors.append(2)    # show some error message in template
                    break
            if len(errors)==0:
                print'can save user'
                # create new User object and save in database
                new_user = User(username=username,
                                first_name=first_name,
                                last_name=last_name,
                                email=email)
                new_user.set_password(password)
                new_user.save()

                # create new UserProfile object and save in database
                new_profile = UserProfile()
                new_profile.user = new_user
                new_profile.save()
                # change state registered in template was success
                registered = True

    return render_to_response(
        template,
        {'registered': registered, 'errors': errors},
        context)

def menu(request):
    template = 'login/menu.html'
    context = RequestContext(request)

    return  render_to_response(
        template,
        {},
        context
    )

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'login/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('login:menu'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('login/login.html', {'error':'error'}, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('login:index'))

def user_register(request):
    template = 'login/register.html'
    context = {}
    errors = []

    if request.method == 'POST':
        # get all User objects
        users = User.objects.all()

        # get data from template login/register.html
        username        = request.POST['username']          # get 1. username
        std_id          = request.POST['std_id']            # get 2. std_id
        firstname_th    = request.POST['firstname_th']      # get 3. firstname_th
        lastname_th     = request.POST['lastname_th']       # get 4. lastname_th
        firstname_en    = request.POST['firstname_en']      # get 5. firstname_en
        lastname_en     = request.POST['lastname_en']       # get 6. lastname_en
        address         = request.POST['address']           # get 7. address
        office          = request.POST['office']            # get 8. office
        email           = request.POST['email']             # get 9. email
        tel             = request.POST['tel']               # get 10. tel
        scheme          = request.POST['scheme']            # get 11. scheme
        main            = request.POST['main']              # get 12. main
        department      = request.POST['department']        # get 13. department
        faculty         = request.POST['faculty']           # get 14. faculty
        password        = request.POST['password']          # get 15. password
        check_password  = request.POST['check_password']    # get 16. check_password

        # errors 1: User fill invalid password
        if password != check_password:
            print 'password is invalid'
            errors.append(1)

        # errors 2: username is duplicate
        try:
            user = User.objects.get(username = username)
            errors.append(2)
        except:
            pass

        # errors 3: std_id is duplicate
        try:
            std = Student.objects.get(std_id = std_id)
            errors.append(3)
        except:
            pass

        # if don't have an error
        if len(errors) == 0:
            # create new User object
            newUser = User(
                username        = username,
                first_name      = firstname_en,
                last_name       = lastname_en,
                email           = email
            )
            newUser.set_password(password)
            newUser.save()  # save new User object into database

            # create new UserProfile object
            newUserProfile = UserProfile(
                user = newUser,
                firstname_th    = firstname_th,
                lastname_th     = lastname_th,
                firstname_en    = firstname_en,
                lastname_en     = lastname_en,
                address         = address,
                office          = office,
                tel             = tel,
                department      = department,
                faculty         = faculty,
                type            = '0' # type '0' is Student
            )
            newUserProfile.save() # save new UserProfile object into database

            # create new Student object
            newStudent = Student(
                userprofile     = newUserProfile,
                std_id          = std_id,
                scheme          = scheme,
                main            = main
            )
            newStudent.save() # save new Srudent object into database

            # redirect to template with register is success
            context['registered'] = True
        # if have an error
        else:
            # redirect to template with errors list
            context['errors'] = errors

            # redirect to template with some data
            context['username']     = username
            context['std_id']       = std_id
            context['firstname_th'] = firstname_th
            context['lastname_th']  = lastname_th
            context['firstname_en'] = firstname_en
            context['lastname_en']  = lastname_en
            context['address']      = address
            context['office']       = office
            context['email']        = email
            context['tel']          = tel

            # delete some context dict that user fill invalid
            for error in errors:
                if error == 2:
                    del context['username']
                elif error == 3:
                    del context['std_id']

    return render(
        request,
        template,
        context
    )