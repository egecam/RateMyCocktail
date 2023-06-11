import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

rate = 3.5


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('loggedin')
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


def home(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    cocktails = response.json()['drinks']

    arrayOfIngr = {"drink0": [], "drink1": [], "drink2": [],
                   "drink3": [], "drink4": [], "drink5": []}

    for j in range(0, len(cocktails)):
        for i in range(1, 15):
            ingredient = "strIngredient" + str(i)
            element = "drink" + str(j)
            if cocktails[j][ingredient] is not None:
                lst = cocktails[j][ingredient]
                arrayOfIngr[element].append(lst)

    return render(request, "home.html", {"cocktails": cocktails, "rate": rate, "ingr": arrayOfIngr})
    pass


def loggedinHome(request):
    response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    cocktails = response.json()['drinks']
    return render(request, "loggedinhome.html", {"cocktails": cocktails, "rate": rate})


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
