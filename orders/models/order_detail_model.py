from django.db import models
from .order_model import Order
from products.models.product_model import Product

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_details', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order.id} - {self.product.name}"