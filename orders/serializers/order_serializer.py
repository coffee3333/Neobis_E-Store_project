from rest_framework import serializers
from ..models.order_model import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'created_at', 'updated_at', 'status', 'payment_method']
