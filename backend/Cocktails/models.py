from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    ingredients = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
    rating = models.FloatField(null=True)
