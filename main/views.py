from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import ProductSet, Product
from main.serializers import ProductSetSerializer, ProductSerializer, ProductAndSetsSerializer


class ProductAndSetsListVIew(APIView):

    def get(self, request, *args, **kwargs):
        product_list = ProductSerializer(self.get_product_list(), many=True)
        product_sets_list = ProductSetSerializer(self.get_product_sets_list(), many=True)
        data = {'products': product_list.data, 'product_sets': product_sets_list.data}
        serializer = ProductAndSetsSerializer(data=data)
        return Response(serializer.initial_data)

    def get_product_list(self):
        queryset = Product.objects.filter(bottom__isnull=True, top__isnull=True)
        return queryset

    def get_product_sets_list(self):
        queryset = ProductSet.objects.all()
        return queryset

