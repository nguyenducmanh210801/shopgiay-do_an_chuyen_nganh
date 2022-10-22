from django.db import models
from shop.user.models import CustomerUser
from shop.cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    is_complete = models.BooleanField(default=False)