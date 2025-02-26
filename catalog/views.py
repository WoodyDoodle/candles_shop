from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def catalog(request):
    return render(request, 'html/shop.html')

def about(request):
    return render(request, 'html/about.html')

def contact(request):
    return render(request, 'html/contact.html')
