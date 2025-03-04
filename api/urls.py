from django.urls import path
from django.conf.urls.static import static

import views


urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]