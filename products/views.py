from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response    
from rest_framework import status
from products.serializers import (
    CategoryDetailSerializer,
    CategoryListSerializer,
    ProductDetailSerializer, 
    ProductListSerializer, 
    ReviewDetailSerializer, 
    ReviewListSerializer,
)
from .models import Category, Product, Review


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        products = Category.objects.get(id=id, is_active=True)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(products, many=False).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        products = Product.objects.get(id=id, is_active=True)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(products, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        products = Review.objects.get(id=id, is_active=True)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(products, many=False).data
    return Response(data=data)

@api_view(['GET'])
def category_list_api_view(request):
    products = Category.objects.filter(is_active=True)
    products_count = products.count()
    data = CategoryListSerializer(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.filter(is_active=True)
    data = ProductListSerializer(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    products = Review.objects.filter(is_active=True)
    data = ReviewListSerializer(products, many=True).data
    return Response(data=data)







