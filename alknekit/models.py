from django.db import models


class accounts(models.Model):
    login = models.CharField(default=None, unique=True, max_length=16)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=16)

class Products(models.Model):
    subcategory = models.CharField(max_length=20,default=1)
    tittle = models.CharField(max_length=50)
    articul = models.CharField(unique=True, max_length=75)
    images = models.ImageField()
    price = models.IntegerField(default=0)
