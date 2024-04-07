from django.urls import path
from .views import OrderList, OrderDetail, OrderDetailList, OrderDetailDetail

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order-details/', OrderDetailList.as_view(), name='orderdetail-list'),
    path('order-details/<int:pk>/', OrderDetailDetail.as_view(), name='orderdetail-detail'),
]
