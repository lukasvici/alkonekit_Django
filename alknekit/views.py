from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Subcategory
from math import ceil


def index(request):
    obj = Products.objects.filter(main=3)[:4]
    category = Subcategory.objects.filter()
    context = {
        "cat": category,
        'obj': obj,
    }
    return render(request, "../templates/alknekit/index.html", context)


def list_products(request, category_id):
    products = Products.objects.filter(subcategory=category_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 20)
    try:
        obj = paginator.page(page)
    except:
        obj = paginator.page(1)
    return render(request, "../templates/alknekit/catalog.html", {"obj": obj,"count":int(ceil(paginator.count/20))})


def product(request, product_id, category_id):
    product = Products.objects.filter(id=product_id, subcategory=category_id)
    return render(request, "../templates/alknekit/product.html", {"obj": product})
