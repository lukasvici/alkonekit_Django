from django.contrib import admin
from .models import accounts, Products, Category

class ProductsAddAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['tittle']}),
        ('Новая Цена',{'fields':['newprice']}),
        ('Старая Цена',{'fields':['oldprice']}),
        ('Подкатегория',{'fields':['subcategory']}),
        ('Картинка',{'fields':['mainimage']}),
        ('Объем', {'fields': ['Value']}),
        ('id Сортировка',{'fields':['main']}),
    ]
    list_display = ('tittle', 'subcategory', 'main')
    list_filter = ('main',)
admin.site.register(accounts)
admin.site.register(Products, ProductsAddAdmin)
admin.site.register(Category)
# Register your models here.
