from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name count'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = 'id title description price category rating'.split()



class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id product text stars '.split()


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    count = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=1000, decimal_places=2)
    category_id = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category does not exist")
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    product_id = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product does not exist")
        return product_id
    
    def validate_stars(self, stars):
        if stars < 1 or stars > 5:
            raise serializers.ValidationError("Stars must be between 1 and 5")
        return stars
