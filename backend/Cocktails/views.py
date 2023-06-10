import requests
from django.shortcuts import render
from django.http import HttpResponse

rate = 3.5


def index(req):
    return HttpResponse("Hello, world. You're at the cocktails index.")


def login(req):
    return HttpResponse("This is login page.")


def register(req):
    return HttpResponse("This is register page.")


def home(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    cocktails = response.json()['drinks']
    for i in range(15):
        ingr = [response.json()['drinks']['strIngredient'+str(i)]]
        ingrs.append(ingr)
    return render(request, "cocktails.html", {"cocktails": cocktails, "rate": rate}, ingrs)
    pass
