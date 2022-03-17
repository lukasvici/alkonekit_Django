from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products, Subcategory, Category
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import telebot

bot = telebot.TeleBot("5233868676:AAFbJBML227uGM7mEPVDrrKcFTjGLlM8s4U", parse_mode=None)

def checkcookie(request):
    if request.session.session_key == None:
        request.session.save()
        request.session["cart"] = []
    return 0

def getcartprice(request):
    allprice = 0
    for i in request.session["cart"]:
        allprice += Products.objects.filter(id=int(json.loads(json.dumps(i))["id"]))[0].newprice*json.loads(json.dumps(i))["amount"]
    return allprice

def index(request):
    checkcookie(request)
    obj = Products.objects.filter(main=3)[:4]
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        "category": category,
        "subcategory": subcategory,
        'obj': obj,
        "title": "",
        "cartprice": getcartprice(request)
    }
    return render(request, "../templates/alknekit/index.html", context)


def list_categories(request, category):
    checkcookie(request)
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
        "title":category_id.title,
        "cartprice": getcartprice(request)
    }
    return render(request, "../templates/alknekit/catalog.html", context)


def list_subcategories(request, category, subcategory):
    checkcookie(request)
    category_id = Category.objects.get(title_url=category)
    subcategory_id = Subcategory.objects.get(title_url=subcategory, Category=category_id)
    products = Products.objects.filter(category=category_id, subcategory=subcategory_id)
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
        "title": category_id.title + subcategory_id.title,
        "cartprice": getcartprice(request)
    }
    return render(request, "../templates/alknekit/catalog.html", context)


def product(request, product_id):
    checkcookie(request)
    product = Products.objects.filter(id=product_id)
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        "category": category,
        "subcategory": subcategory,
        'obj': product,
        "cartprice": getcartprice(request),
        "title": product[0].tittle
    }
    return render(request, "../templates/alknekit/product.html", context)


def cart_show(request):
    checkcookie(request)
    temp = []
    for i in request.session["cart"]:
        temp.append(Products.objects.filter(id=int(i["id"])))
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    prodlistprice = []
    for i in request.session["cart"]:
        i["price"] = Products.objects.filter(id=i["id"])[0].newprice*i["amount"]
        prodlistprice.append(i)
    context = {
        "category": category,
        "subcategory": subcategory,
        'prod': temp,
        "am": request.session["cart"],
        "cartprice": getcartprice(request),
        "priceprod":prodlistprice,
        "title": "Корзина"
    }
    return render(request, "../templates/alknekit/cart.html", context)


@api_view(['POST'])
def cart_add(request):
    product_json = None
    checkcookie(request)
    prodincart = False
    for i in request.session["cart"]:
        if i["id"] == int(json.loads(json.dumps(request.data))["id"]):
            prodincart = True
            break
    if prodincart == False:
        product_json = json.loads(json.dumps(request.data))
        product_json["id"] = int(product_json["id"])
        product_json["amount"] = int(product_json["amount"])
        product_json["price"] = Products.objects.filter(id=int(json.loads(json.dumps(request.data))["id"]))[0].newprice
        request.session["cart"].append(product_json)
        request.session["cart"] = request.session["cart"]
    return Response(product_json)

@api_view(['POST'])
def prod_amount(request):
    checkcookie(request)
    newprod = ""
    temp = []
    for i in request.session["cart"]:
        if i["id"] == int(json.loads(json.dumps(request.data))["id"]):
            if json.loads(json.dumps(request.data))["type"] == "plus":
                i["amount"] = int(i["amount"]) + 1
                temp.append(i)
            else:
                i["amount"] = int(i["amount"]) - 1
                if i["amount"] > 0:
                    temp.append(i)
                else:
                    pass
            newprod = i
        else:
            temp.append(i)
    newprod["allprice"] = getcartprice(request)
    request.session["cart"] = temp
    return Response(newprod)


@api_view(['POST'])
def sendcart(request):
    cart = "test\n"
    for i in request.session["cart"]:
        prod = Products.objects.filter(id=i["id"])[0]
        cart+=prod.tittle + " " + str(prod.newprice) + "₽ " + str(i["amount"]) + "шт\n"
    cart += str(getcartprice(request)) + "₽"
    send(cart)
    return Response(0)


@bot.message_handler(func=lambda m: True)
def send(message):
    bot.send_message(648136076, message)
