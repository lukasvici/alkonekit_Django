from django.db import models


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
    images = models.ImageField()
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.tittle
