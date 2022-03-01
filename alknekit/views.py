from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Subcategory, Category
from django.http import HttpResponse


def index(request):
    obj = Products.objects.filter(main=3)[:4]
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        "category": category,
        "subcategory": subcategory,
        'obj': obj,
    }
    return render(request, "../templates/alknekit/index.html", context)


def list_categories(request, category):
    category_id = Category.objects.get(title_url=category)
    products = Products.objects.filter(category=category_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 20)
    try:
        obj = paginator.page(page)
    except:
        obj = paginator.page(1)
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        "category": category,
        "subcategory": subcategory,
        'obj': obj,
        "title":category
    }
    return render(request, "../templates/alknekit/catalog.html", context)


def list_subcategories(request, category, subcategory):
    category_id = Category.objects.get(title_url=category)
    subcategory_id = Subcategory.objects.get(title_url=subcategory, Category=category_id)
    products = Products.objects.filter(category=category_id, subcategory=subcategory_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 20)
    try:
        obj = paginator.page(page)
    except:
        obj = paginator.page(1)
    categoryprod = Category.objects.all()
    subcategoryprod = Subcategory.objects.all()
    context = {
        "category": categoryprod,
        "subcategory": subcategoryprod,
        'obj': obj,
        "title": category + " " + subcategory
    }
    return render(request, "../templates/alknekit/catalog.html", context)


def product(request, product_id):
    product = Products.objects.filter(id=product_id)
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        "category": category,
        "subcategory": subcategory,
        'obj': product,
    }
    return render(request, "../templates/alknekit/product.html", context)


def cart_show(request):
    if request.session.session_key == None:
        request.session.save()
    return HttpResponse(request.session.session_key)
