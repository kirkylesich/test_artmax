from rest_framework import generics
from main.models import ProductSet, Product
from main.serializers import ProductSetSerializer, ProductSerializer


class ProductSetView(generics.ListCreateAPIView):
    queryset = ProductSet.objects.all()
    serializer_class = ProductSetSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
