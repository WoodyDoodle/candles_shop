import logging
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import renderers

from catalog.models import Cart, Product
from .serializers import CartSerializer, ProductSerializer


logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def cart(request:HttpRequest):
    if request.method == 'GET':
        cart = Cart.objects.get_or_create(customer=request.user)[0]
        products = cart.products.all()
        data = []
        for product in products:
            serializer = ProductSerializer(product)
            data.append(serializer.data)
            


@csrf_exempt
def add_to_cart(request:HttpRequest):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            cart = Cart.objects.get_or_create(user=request.user)[0]
            product = Product.objects.get(id=product_id)
            cart.products.add(product)
            cart.save()
        except Exception as e:
            count_products = cart.products.count()
            logger.error(str(e))
            return JsonResponse({
                'error': 'Произошла ошибка при добавлении товара в корзину',
                'count_products': count_products}, 
                status=500)
    count_products = cart.products.count()
    return JsonResponse({'success': True, 'count_products': count_products})
