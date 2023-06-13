from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cocktailDB'),  # this is homepage
    # this is the second homepage aka community page
    path('community', views.community, name='community'),
    # this is for creating a new recipe
    path('newrecipe', views.newrecipe, name='newrecipe'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('rate/<int:recipe_id>/<int:rating>/', views.rate),
    path('delete/<int:recipe_id>', views.delete),
]
