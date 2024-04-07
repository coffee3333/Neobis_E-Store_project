from rest_framework import generics
from .models.order_model import Order
from .models.order_detail_model import OrderDetails
from .serializers.order_serializer import OrderSerializer
from .serializers.order_detail_serializer import OrderDetailSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailList(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer

class OrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer
