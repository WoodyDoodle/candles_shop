from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def catalog(request):
    return render(request, 'html/shop.html')

def base(request):
    return render(request, 'html/base.html')