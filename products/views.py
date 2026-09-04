
from products.models import CartItem
from products.models import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}

    return render(request, "products/products.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}

    return render(request, "products/product_detail.html", context)

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = []
    total = 0
    if cart:
        items = CartItem.objects.filter(cart=cart)
        for item in items:
            total += item.product.price * item.quantity
    context = {"items": items,"total": total}

    return render(request, "products/cart.html", context)

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart')