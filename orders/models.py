from django.db import models
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=50)

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    status = models.CharField(max_length=100)

    def __str__(self):
        return self.order_number