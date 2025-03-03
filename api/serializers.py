from rest_framework import serializers

from ..catalog.models import Cart

class CartSerializer(serializers.Serializer):
    customer = serializers.IntegerField(source='customer.name')
    order = serializers.IntegerField(source='order.id')
    date_created = serializers.DateTimeField()
    last_add = serializers.DateTimeField()
    is_paid = serializers.BooleanField()

