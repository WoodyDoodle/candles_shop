from django.urls import path
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('add-to-cart', views.add_product_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('change-count-product', views.change_count_product_cart, 
         name='change_count_product'),
]