from abc import ABC

from rest_framework import serializers
from main.models import ProductSet, Product


class ProductSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSet
        fields = '__all__'
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class ProductAndSetsSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    product_sets = ProductSetSerializer(many=True)

