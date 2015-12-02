from django.conf.urls import url
from django.conf.urls import include 

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'results', views.result, name='result'),
    url(r'about', views.about, name='about'),
    url(r'profile', views.profile, name='profile'),
    url(r'contact', views.contact, name='contact'),
    url(r'register', views.register, name='register'),
    url(r'login', views.user_login, name='login'),
    url(r'logout', views.user_logout, name='logout'),
]