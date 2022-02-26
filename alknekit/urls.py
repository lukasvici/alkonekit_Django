from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>', views.product, name='product'),
    path('<str:category>/', views.list_categories, name='catalog'),
    path('<str:category>/<str:subcategory>', views.list_subcategories, name='subcatalog'),

]
