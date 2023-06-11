import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from .models import Recipe

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


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_profile = User.objects.create_user(
            username=username, password=password)

        user_profile.save()

        return redirect('home')
    else:
        return render(request, 'register.html')


def community(req):
    res = Recipes.objects.all()

    return render(req, "community.html", {'res': res})


def newrecipe(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        body = req.POST.get('body')
        rating = req.POST.get('rating')

        recipe = Recipe(user=req.user, title=title, body=body, rating=rating)
        recipe.save()

        return redirect('home')
    else:
        return render(req, 'newrecipe.html')


def home(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    cocktails = response.json()['drinks']

    arrayOfIngr = {"drink0": [], "drink1": [], "drink2": [],
                   "drink3": [], "drink4": [], "drink5": []}
    ingr = arrayOfIngr

    for j in range(0, len(cocktails)):
        for i in range(1, 15):
            ingredient = "strIngredient" + str(i)
            element = "drink" + str(j)
            if cocktails[j][ingredient] is not None:
                lst = cocktails[j][ingredient]
                arrayOfIngr[element].append(lst)

    ingr = []
    for key, value in arrayOfIngr.items():
        ingr.append({'name': key, 'ingredients': value})

    return render(request, "home.html", {"cocktails": cocktails, "rate": rate, "ingr": ingr})
    # "ingr": json_object
    pass


def logout_view(request):
    auth_logout(request)
    return redirect('home')


'''
arrayOfIngredients.push(
          drink.strIngredient1,
          drink.strIngredient2,
          drink.strIngredient3,
          drink.strIngredient4,
          drink.strIngredient5,
          drink.strIngredient6,
          drink.strIngredient7,
          drink.strIngredient8,
          drink.strIngredient9,
          drink.strIngredient10,
          drink.strIngredient11,
          drink.strIngredient12,
          drink.strIngredient13,
          drink.strIngredient14,
          drink.strIngredient15
        );
'''
