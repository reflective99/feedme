from django.contrib import admin

# Register your models here.
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating')

admin.site.register(Restaurant, RestaurantAdmin)
