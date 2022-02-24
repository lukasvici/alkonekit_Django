from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Category


def index(request):
    obj = Products.objects.filter(main=3)[:4]
    category = Category.objects.filter()
    context = {
        "cat": category,
        'obj': obj,
    }
    return render(request, "../templates/alknekit/index.html", context)


def list_products(request, category_id):
    products = Products.objects.filter(subcategory=category_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 20)
    obj = paginator.page(page)
    return render(request, "../templates/alknekit/catalog.html", {"obj": obj})
