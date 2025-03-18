from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product, Cart, Customer, Cart_Product
#from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def catalog(request:HttpRequest):
    if not request.user.is_authenticated:
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key
        user = User.objects.get_or_create(username=session_id)[0]
    else:
        user = request.user

    customer = Customer.objects.get_or_create(user=user)[0]
    cart = Cart.objects.get_or_create(customer=customer)[0]
    
    cart_items = Cart_Product.objects.filter(cart=cart).all()
    #cart_items_ids = [cart_item.product.id for cart_item in cart_items]
    products = Product.objects.all()
    context = {
        'cart_items': cart_items,
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

