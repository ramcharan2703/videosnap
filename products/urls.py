from django.urls import path
from . import views

urlpatterns = [

    path('', views.products, name='products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
]