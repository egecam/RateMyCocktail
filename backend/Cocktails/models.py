from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25),
    password = models.CharField(max_length=25),
    avatar = models.ImageField(
        upload_to='avatars/', default='avatars/default.png'),


class Recipe(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE),
    title = models.CharField(max_length=25),
    body = models.CharField(max_length=1000),
    photo = models.ImageField(upload_to='recipes/'),
    rating = models.FloatField(),
