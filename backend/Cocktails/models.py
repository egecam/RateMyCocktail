from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='recipes/')
    rating = models.FloatField()
