from django.contrib.auth.models import User, Group
from rest_framework import serializers

from catalog.models import Cart, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'last_login']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'order', 'date_created', 'last_add', 'is_paid']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
#class CartSerializer(serializers.Serializer):
    # customer = serializers.IntegerField(source='customer.name')
    # order = serializers.IntegerField(source='order.id')
    # date_created = serializers.DateTimeField()
    # last_add = serializers.DateTimeField()
    # is_paid = serializers.BooleanField()

