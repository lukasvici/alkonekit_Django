from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Subcategory, Category
from math import ceil


def index(request):
    obj = Products.objects.filter(main=3)[:4]
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        "cat": category,
        "subcat": subcategory,
        'obj': obj,
    }
    return render(request, "../templates/alknekit/index.html", context)


def list_categories(request, category):
    category_id = Category.objects.get(title=category)
    products = Products.objects.filter(category=category_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 20)
    try:
        obj = paginator.page(page)
    except:
        obj = paginator.page(1)
    return render(request, "../templates/alknekit/catalog.html", {"obj": obj,"count":int(ceil(paginator.count/20))})


def list_subcategories(request, category, subcategory):
    category_id = Category.objects.get(title=category)
    subcategory_id = Subcategory.objects.get(Subcategory=subcategory, Category=category_id)
    products = Products.objects.filter(category=category_id, subcategory=subcategory_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 20)
    try:
        obj = paginator.page(page)
    except:
        obj = paginator.page(1)
    return render(request, "../templates/alknekit/catalog.html", {"obj": obj})

def product(request, product_id):
    product = Products.objects.filter(id=product_id)
    return render(request, "../templates/alknekit/product.html", {"obj": product})
