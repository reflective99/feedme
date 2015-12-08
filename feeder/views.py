from django.shortcuts import render
from feeder.forms import UserForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Restaurant
from .models import Like
from .models import Category
from django.contrib.auth.models import User

import random

def index(request):
    city_hash = Restaurant.objects.values('city')
    cities = []
    for c in city_hash:
        cities.append(c['city'])
    cities = set(cities)
    cats = Category.objects.values('cat').distinct()
    categories = []
    for c in cats:
        categories.append(c['cat'])
    categories = sorted(set(categories))
    print categories
    #categories = sorted(set(categories))
    # categories = Category.objects.order_by('cat').values('cat').distinct()
    allusers = User.objects.all()
    context = {'cities': cities, 'categories': categories, 'users': allusers }
    return render(request, 'index.html', context)

def result(request):
    c = request.POST.get('city')
    category_param = request.POST.get('categories')
    print c
    print category_param
    
    #get restaurants in specified location
    if c != "I don't care":
      restaurants_with_location = Restaurant.objects.filter(city=c)
    else:
      restaurants_with_location = Restaurant.objects.all()
      
    #get all restaurants with the requested category
    if category_param != "Doesn't matter":
      #gives list of rids that are restaurants with appropriate category
      restaurants_with_category = Category.objects.filter(cat=category_param).values('rid')

    
    #need to find all restaurants that are in restaurants_with_location and in restaurants_with_category
      res = []
      for res1 in restaurants_with_location:
        for res2 in restaurants_with_category:
          if res1.id == res2['rid']:
            res.append(res1)
      print res
    else:
      #if no category specified, just use the ones with correct location
      res = restaurants_with_location
    
    count = len(res)
    if(count > 0):
        #randomly select a restaurant
        restaurant = res[random.randint(0, count-1)]
        add = restaurant.address + " " + restaurant.city 
        add.replace(" ", "+")
        restaurant_categories = Category.objects.filter(rid=restaurant.id)
        
        #check if the restaurant has been liked by this user
        user = request.user
        res_liked = Like.objects.filter(uid=user.id, rid=restaurant.id).exists()
        
        context = {'restaurant': restaurant, 'count': count, 'cats': restaurant_categories, 'addr': add, 'res_liked': res_liked}
        return render(request, 'result.html', context)
    else:
        return render(request, 'failed.html')
    
def profile(request):
    #user = User.objects.all()[2]
    #context = {'user': user}
    user = request.user
    likes = Like.objects.filter(uid=user.id).distinct()
    rnames = []
    for l in likes:
      r = Restaurant.objects.get(id = l.rid)
      rnames.append(r)
    context = {'u': user, 'res_names': rnames}
    return render(request, 'profile.html', context)

def add_like(request, uid, rid):
    l = Like(uid=uid, rid=rid)
    l.save()
    return HttpResponseRedirect('/profile')
    
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