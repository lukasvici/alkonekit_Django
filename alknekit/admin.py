from django.contrib import admin
from .models import accounts, Products, Category, Images

class ImagesInline(admin.StackedInline):
    model = Images
    extra = 3

class ProductsAddAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['tittle']}),
        ('Articul',{'fields':['articul']}),
        ('price',{'fields':['price']}),
        ('subcategory',{'fields':['subcategory']}),
        ('Main Image',{'fields':['mainimage']}),
    ]
    inlines = [ImagesInline]
admin.site.register(accounts)
admin.site.register(Products, ProductsAddAdmin)
admin.site.register(Category)
# Register your models here.
