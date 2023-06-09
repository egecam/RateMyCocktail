from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25),
    password = models.CharField(max_length=25),
    avatar = models.ImageField(
        upload_to='avatars/', default='avatars/default.png'),
    recipes = models.OneToManyField(recipe, on_delete=models.CASCADE),


class Recipe(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE),
    title = models.CharField(max_length=25),
    body = models.CharField(max_length=1000),
    photo = models.ImageField(upload_to='recipes/'),
    rating = models.IntegerField(max=5, min=0),
    comment = models.OneToManyField(comment, on_delete=models.CASCADE),


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE),
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE),
    body = models.CharField(max_length=400),
