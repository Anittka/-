from django.db import models


class Product(models.Model):
    article = models.CharField(max_length=50)

    name = models.CharField(max_length=255)

    category = models.CharField(max_length=100)

    description = models.TextField()

    manufacturer = models.CharField(max_length=100)

    supplier = models.CharField(max_length=100)

    unit = models.CharField(max_length=50)

    stock = models.IntegerField(default=0)

    discount = models.IntegerField(default=0)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.name