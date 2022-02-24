from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<int:category_id>/', views.list_products, name='catalog'),
]
