import logging
import json
import traceback

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from rest_framework import renderers

from catalog.models import Cart, Product, Customer, Cart_Product
from .serializers import CartSerializer, ProductSerializer, UserSerializer


logger = logging.getLogger(__name__)

# Create your views here.
def user_handler(func):
    def wrapper(request:HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            if not request.session.session_key:
                request.session.create()
            session_id = request.session.session_key
            user = User.objects.get_or_create(username=session_id)[0]
        else:
            user = request.user
        customer = Customer.objects.get_or_create(user=user)[0]
        cart = Cart.objects.get_or_create(customer=customer)[0]
        return func(request, *args, **kwargs,  cart=cart, customer=customer)
    return wrapper

@csrf_exempt
@require_GET
@user_handler
def cart(request:HttpRequest, customer:Customer, cart:Cart):
    products = Cart_Product.objects.filter(cart=cart).all()
    data = []
    for product in products:
        serializer = ProductSerializer(product)
        data.append(serializer.data)
    serialized_user = UserSerializer(customer.user).data
    return JsonResponse({'success': True, 'user':serialized_user, "data": data}, 
                        safe=False)
            


@csrf_exempt
@require_POST
@user_handler
def add_product_to_cart(request:HttpRequest, customer:Customer, cart:Cart):
    try:
        body = json.loads(request.body)
        product_id = body['product_id']
        cart = Cart.objects.get_or_create(customer=customer)[0]
        product = Product.objects.filter(id=product_id).first()
        cart.products.add(product)
    except:
        traceback.print_exc()
        products = Cart_Product.objects.filter(cart=cart)
        count_products = sum([product.count for product in products.all()])
        return JsonResponse({
            'success': False,
            'error': 'Произошла ошибка при добавлении товара в корзину',
            'count_products': count_products},
            status=500)
    
    products = Cart_Product.objects.filter(cart=cart)
    count_products = sum([product.count for product in products.all()])
    return JsonResponse({'success': True, 'count_products': count_products})

@csrf_exempt
@require_POST
@user_handler
def change_count_product_cart(request:HttpRequest, customer:Customer, cart:Cart):
    body = json.loads(request.body)
    product_id = body['product_id']
    count = body['count']

    product = Product.objects.get(id=product_id)
    if not product:
        return JsonResponse({'success': False, 
                             'error': f'Товар c id {product_id} не найден'})
    
    cart_product = Cart_Product.objects.filter(cart=cart,product=product_id).first()
    if not cart_product:
        return JsonResponse({'success': False, 
                             'error': 'Товара нет в корзине'})
    
    if count == 0:
        cart_product.delete()
    elif count < 0:
        return JsonResponse({'success': False,
                             'error': f'Некорректное значение количества:{count}'})
    else:
        cart_product.count = count
        cart_product.save() 

    return JsonResponse({'success': True,
                         'count_product': count})