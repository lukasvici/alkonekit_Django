from django.http import HttpResponse
from django.shortcuts import render


from .models import Products


def index(request):
    obj = Products.objects.all()[:4]
    context = {
        'obj':obj,
    }
    return  render(request, "../templates/alknekit/products.html", context)
