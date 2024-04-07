from rest_framework import serializers
from ..models.order_detail_model import OrderDetails


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ['id', 'order', 'product', 'quantity', 'price']