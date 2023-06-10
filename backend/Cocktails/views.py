import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages

rate = 3.5


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')



def register(req):
    return HttpResponse("This is register page.")


def home(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    cocktails = response.json()['drinks']
    return render(request, "cocktails.html", {"cocktails": cocktails, "rate": rate})
    pass
