from django.http import HttpResponse
from django.shortcuts import render


from .models import Products, Category


def index(request):
    obj = Products.objects.filter(main=3)[:4]
    category = Category.objects.filter()
    context = {
        "cat":category,
        'obj':obj,
    }
    return render(request, "../templates/alknekit/index.html", context)

def list_products(request, category_id):
    obj = Products.objects.filter(subcategory=category_id)[:20]
    context = {
        'obj': obj,
    }
    return render(request, "../templates/alknekit/catalog.html", context)
