from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=((1, "Верх"), (2, "Низ"), (3, "Не выбран")))
    price = models.DecimalField(max_digits=5, decimal_places=2)

    @staticmethod
    def get_product_list():
        filtered_product_list = Product.objects.filter(bottom__isnull=True, top__isnull=True)
        return filtered_product_list


class ProductSet(models.Model):
    name = models.CharField(max_length=200)
    top = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='top')
    bottom = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bottom')

    @staticmethod
    def get_product_sets_list():
        product_sets_list = ProductSet.objects.all()
        return product_sets_list
