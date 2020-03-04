from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import ProductSet, Product
from main.serializers import ProductSetSerializer, ProductSerializer


class ProductAndSetsListVIew(APIView):
    product_list = ProductSerializer(Product.get_product_list(), many=True)
    product_sets_list = ProductSetSerializer(ProductSet.get_product_sets_list(), many=True)

    def get(self, request, *args, **kwargs):
        return Response(self.get_products_and_sets())

    def get_products_and_sets(self):
        return {'products_and_sets': self.product_list.data + self.product_sets_list.data}
