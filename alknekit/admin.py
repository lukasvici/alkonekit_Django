from django.contrib import admin
from .models import Products, Subcategory, Category


class ProductsAddAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tittle']}),
        ('Новая Цена', {'fields': ['newprice']}),
        ('Старая Цена', {'fields': ['oldprice']}),
        ('категория', {'fields': ['category']}),
        ('Подкатегория', {'fields': ['subcategory']}),
        ('Объем', {'fields': ['Value']}),
        ('id Сортировка', {'fields': ['main']}),
        ('Картинка', {'fields': ['mainimage']}),
    ]
    list_display = ('tittle', 'subcategory', 'main', "image_tag")
    list_filter = ('main', 'subcategory',)


admin.site.register(Products, ProductsAddAdmin)
admin.site.register(Subcategory)
admin.site.register(Category)
# Register your models here.
