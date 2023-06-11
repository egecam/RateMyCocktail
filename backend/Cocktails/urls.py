from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # this is homepage
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('loggedinhome', views.loggedinHome, name = 'loggedin')
]
