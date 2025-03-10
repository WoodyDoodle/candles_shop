from rest_framework import serializers

from catalog.models import Cart, Product


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

