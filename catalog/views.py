from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Product, Cart, Customer, Cart_Product
from api.views import user_handler
#from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def catalog(request:HttpRequest):
    products = Product.objects.all()
    context = {
        'products': products,
        'current_page': 'shop',
        }
    return render(request, 'html/shop.html', context)

def about(request):
    context = {'current_page': 'about'}
    return render(request, 'html/about.html', context)

def contact(request):
    context = {'current_page': 'contact'}
    return render(request, 'html/contact.html', context)

def products(request):
    return render(request, 'html/products.html')

@user_handler
def cart(request, customer:Customer, cart:Cart):
    cart_items = Cart_Product.objects.filter(cart=cart).all()
    context = {
        'cart_items': cart_items,
        'current_page': 'cart'
        }
    return render(request, 'html/cart.html', context)

