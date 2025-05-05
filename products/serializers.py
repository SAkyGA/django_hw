from rest_framework import serializers
from .models import Category, Product, Rewiew



class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category'.split()



class RewiewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewiew
        fields = '__all__'

class RewiewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewiew
        fields = 'id product text'.split()