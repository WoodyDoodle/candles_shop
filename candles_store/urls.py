"""
URL configuration for candles_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from catalog import views as catalog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog_views.index, name='index'),
    path('shop/', catalog_views.catalog, name='shop'),
    path('about/', catalog_views.about, name='about'),
    path('contact/', catalog_views.contact, name='contact'),
    path('cart/', catalog_views.cart, name='cart'),
    path('api/', include('api.urls')),
    
    ####### path('product/<int:product_id>/', catalog_views.product, name='product'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('order_summary/', views.order_summary, name='order_summary'),
    
    
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
