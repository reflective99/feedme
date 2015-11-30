from django.shortcuts import render
from django.http import HttpResponse

from .models import Restaurant

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
    context = {'cities': cities, 'categories': categories }
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