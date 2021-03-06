from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product, name='product'),
    path('cart/', views.cart_show, name='cart'),
    path('Catalog/<str:category>/', views.list_categories, name='catalog'),
    path('Catalog/<str:category>/<str:subcategory>', views.list_subcategories, name='subcatalog'),
]
