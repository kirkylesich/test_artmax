from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=((1, "Верх"), (2, "Низ"), (3, "Не выбран")))
    price = models.DecimalField(max_digits=5, decimal_places=2)


class ProductSet(models.Model):
    name = models.CharField(max_length=200)
    top = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='top')
    bottom = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bottom')
