from django.shortcuts import render
from .models import Product
#from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def catalog(request):
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