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
    other = Restaurant.objects.filter(city="Durham")
    count = len(other)
    restaurant = other[random.randint(0, count)]
    c = restaurant.categories[1:].split('*')
    context = {'restaurant': restaurant, 'count': count, 'cats': c}
    return render(request, 'result.html', context)
    
def profile(request):
    #user = User.objects.all()[2]
    #context = {'user': user}
    context = {}
    return render(request, 'profile.html', context)