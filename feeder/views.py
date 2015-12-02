from django.shortcuts import render
from feeder.forms import UserForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Restaurant
from django.contrib.auth.models import User

import random

def index(request):
    city_hash = Restaurant.objects.values('city')
    cities = []
    for c in city_hash:
        cities.append(c['city'])
    cities = set(cities)
    cats = Restaurant.objects.values('categories')
    categories = []
    for c in cats:
        cat_list = c['categories'][1:].split('*')
        for cat in cat_list:
            categories.append(cat)
    categories = sorted(set(categories))
    allusers = User.objects.all()
    context = {'cities': cities, 'categories': categories, 'users': allusers }
    return render(request, 'index.html', context)

def result(request):
    c = request.POST.get('city')
    cat = request.POST.get('categories')
    other = Restaurant.objects.filter(city=c)
    res = []
    for r in other:
         if cat in r.categories:                                                                                        
           res.append(r)
    count = len(res)
    if(count > 0):
        
        restaurant = res[random.randint(0, count-1)]
        add = restaurant.address + " " + restaurant.city 
        add.replace(" ", "+")
        c1= restaurant.categories[1:].split('*')
        context = {'restaurant': restaurant, 'count': count, 'cats': c1, 'addr': add}
        return render(request, 'result.html', context)
    else:
        return render(request, 'failed.html')
    
def profile(request):
    #user = User.objects.all()[2]
    #context = {'user': user}
    context = {}
    return render(request, 'profile.html', context)
    
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')
    
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

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

         

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
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
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Feed Me account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)
        
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')