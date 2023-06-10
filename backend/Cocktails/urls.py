from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # this is homepage
    path('login', views.login),
    path('register', views.register),
]
