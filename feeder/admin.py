from django.contrib import admin

# Register your models here.
from .models import Restaurant
from .models import Category
from .models import Like


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category, CategoryAdmin)
