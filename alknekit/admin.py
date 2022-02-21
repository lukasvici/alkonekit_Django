from django.contrib import admin
from .models import accounts, Products, Category

admin.site.register(accounts)
admin.site.register(Products)
admin.site.register(Category)
# Register your models here.
