from django.shortcuts import render
from .models import Product
#from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def catalog(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'html/shop.html', context)

def about(request):
    return render(request, 'html/about.html')

def contact(request):
    return render(request, 'html/contact.html')

def products(request):
    return render(request, 'html/products.html')