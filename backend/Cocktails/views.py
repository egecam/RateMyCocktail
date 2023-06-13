from django.http import HttpRequest, HttpResponse
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import Recipe, Rating
from django.contrib import messages

rate = 3.5


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('cocktailDB')
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken. Choose another one.")
            return render(request, 'register.html')

        user_profile = User.objects.create_user(
            username=username, password=password)

        user_profile.save()

        return redirect('community')
    else:
        return render(request, 'register.html')


def community(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        recipes = Recipe.objects.all()
        for recipe in recipes:
            rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
            recipe.user_rating = rating.rating if rating else 0
        return render(request, "community.html", {"recipes": recipes})
    else:
        recipes = Recipe.objects.all()
        for recipe in recipes:
            rating = Rating.objects.filter(recipe=recipe, user = request.user.id).first()
            recipe.user_rating = rating.rating if rating else 0
        return render(request, "community.html", {"recipes": recipes, "user": request.user.id})

def rate(request: HttpRequest, recipe_id: int, rating: int) -> HttpResponse:
    recipe = Recipe.objects.get(id=recipe_id)
    Rating.objects.filter(recipe=recipe, user=request.user).delete()
    recipe.rating_set.create(user=request.user, rating=rating)
    return community(request)


def newrecipe(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        ingredients = req.POST.get('ingredients')
        body = req.POST.get('body')
        rating = req.POST.get('rating')

        recipe = Recipe(user=req.user, title=title,ingredients = ingredients, body=body, rating=rating)
        recipe.save()

        return redirect('community')
    else:
        return render(req, 'newrecipe.html')

def delete(request, recipe_id: int):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect('community')
    

def home(request):
    response = requests.get(
        "http://www.thecocktaildb.com/api/json/v1/1/random.php")
    cocktails = response.json()['drinks']

    arrayOfIngr = {"drink0": []}
    ingr = arrayOfIngr

    for j in range(0, len(cocktails)):
        for i in range(1, 15):
            ingredient = "strIngredient" + str(i)
            element = "drink" + str(j)
            if cocktails[j][ingredient] is not None:
                lst = cocktails[j][ingredient]
                arrayOfIngr[element].append(lst)

    arrayOfIngr.values()

    return render(request, "home.html", {"cocktails": cocktails, "ingr": ingr})
    # "ingr": json_object
    pass


def logout_view(request):
    auth_logout(request)
    return redirect('cocktailDB')


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
