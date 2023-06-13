
# RateMyCocktail

A social platform to share and rate cocktail recipes made with Django 4.2.

### Models

+ Recipe
    + user (_ForeignKey_ from `django.contrib.auth.models` User model),
    + title (_CharField_),
    + ingredients (_CharField_),
    + body (_CharField_)

Contains a method:
__average_rating(self)__ which returns the average rating of the recipe object.

+ Rating
    + user (_ForeignKey_ from `django.contrib.auth.models` User model),
    + recipe (_ForeignKey_) from Recipe model.
    + rating (_IntegerField_)

__An interesting fact__:
We didn't create a model for "user". We just simply use the built-in Django User model which we import from the `auth` module.

## Views

#### With a template
+ Home 

Contains a random cocktail page which works with a third party API (CocktailDB) to fetch random cocktail data every single refresh. 

+ Community

User-created cocktail data are being represented here. Users can rate listed recipes with the Rating function. Average rating score is shown right after the recipe.

+ New recipe

The view for creating a new recipe with Title, Ingredients and Description fields.


+ Register

The view where the user can create an account with a username and a password. Username must be unique and it is checked by;
```
if User.objects.filter(username = username).first():
    messages.error(request, "This username is already taken. Choose another one.")
    return render(request, 'register.html')
```

 `User` model is imported from `django.contrib.auth.models` package and `messages` from `django.contrib`.

 + Login

User can login to an existing accout with a correct username-password pair.

#### Without a template

+ Logout

A simple logout view, works with the logout method from `django.contrib.auth`.

+ Delete

+ Rate

### Templates

We use Django template language for forms and Bootstrap for styling.

+ Home
+ Community
+ New Recipe
+ Login
+ Register
## Run Locally

Clone the project

```bash
  git clone https://github.com/egecam/RateMyCocktail.git
```

Go to the project directory

```bash
  cd RateMyCocktail
```

Create and activate the virtual environment

  See: [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html).


Install dependencies

```bash
  pip3 install django
```

Start the server

(First, locate to main directory which is the one with a file named `manage.py`)

```bash
  python manage.py runserver
```

For Mac users;

use `python3` instead of `python`.

## Deployment

To deploy this project run;

```bash
  python manage.py migrate
  python manage.py makemigrations Cocktails
  python manage.py migrate
  python manage.py runserver
```

for Mac users;

use `python3` instead of `python`.


## Authors

- [Ege Çam](https://www.github.com/egecam)
- [Yiğit Özman](https://www.github.com/yigitozman)


## License

[GPL-3](https://choosealicense.com/licenses/gpl-3.0//)

