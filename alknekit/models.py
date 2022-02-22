from django.db import models
from django.contrib.postgres.fields import ArrayField


class accounts(models.Model):
    login = models.CharField(default=None, unique=True, max_length=16)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=16)
    def __str__(self):
        return self.login

class Category(models.Model):
    Category = models.CharField(max_length=50)
    Subcategory = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Subcategory

class Products(models.Model):
    subcategory = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=50)
    articul = models.CharField(unique=True, max_length=75)
    price = models.FloatField(default=0)
    mainimage = models.ImageField(default=None, null=False,upload_to='static/images/products')
    def __str__(self):
        return self.tittle

class Images(models.Model):
    articul = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField()

