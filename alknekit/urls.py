from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product, name='product'),
    path('cart/', views.cart_show, name='cart'),
    path('cartadd/', views.cart_add, name='cart'),
    path('amount/', views.prod_amount, name='amount'),
    path('Catalog/<str:category>/', views.list_categories, name='catalog'),
    path('Catalog/<str:category>/<str:subcategory>', views.list_subcategories, name='subcatalog'),
    path('sendtelegram/', views.sendcart, name='telegramsend'),
]
