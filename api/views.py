import logging

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from rest_framework import renderers

from catalog.models import Cart, Product, Customer
from .serializers import CartSerializer, ProductSerializer, UserSerializer


logger = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
@require_GET
def cart(request:HttpRequest):
    if not request.user.is_authenticated:
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key
        user = User.objects.get_or_create(username=session_id)[0]
    else:
        user = request.user

    customer = Customer.objects.get_or_create(user=user)[0]
    cart = Cart.objects.get_or_create(customer=customer)[0]
    products = cart.products.all()
    data = []
    for product in products:
        serializer = ProductSerializer(product)
        data.append(serializer.data)
    serialized_user = UserSerializer(customer.user).data
    return JsonResponse({'success': True, 'user':serialized_user, "data": data}, 
                        safe=False)
            


@csrf_exempt
@require_POST
def add_to_cart(request:HttpRequest):
    if not request.user.is_authenticated:
        if not request.session.session_key:
            request.session.create()
        session_id = request.session.session_key
        user = User.objects.get_or_create(username=session_id)[0]
    else:
        user = request.user

    customer = Customer.objects.get_or_create(user=user)[0]
    cart = Cart.objects.get_or_create(customer=customer)[0]

    try:
        product_id = request.POST.get('product_id')
        print(product_id)
        cart = Cart.objects.get_or_create(customer=customer)[0]
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
