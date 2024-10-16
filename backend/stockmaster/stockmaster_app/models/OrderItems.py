from django.db import models

from .Orders import Orders
from .Product import Product


class OrderItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_items')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'Order {self.order_id} - {self.product_id.name}'
