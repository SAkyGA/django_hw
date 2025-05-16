from django.shortcuts import get_object_or_404
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
    CategoryValidateSerializer,
    ProductValidateSerializer,
    ReviewValidateSerializer,
)
from .models import Category, Product, Review


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        products = Category.objects.get(id=id, is_active=True)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = CategoryDetailSerializer(products, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        products.name = serializer.validated_data.get('name')
        products.count = int(serializer.validated_data.get('count'))
        products.is_active = serializer.validated_data.get('is_active')
        products.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(products, many=False).data)
    elif request.method == 'DELETE':
        products.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        products = Product.objects.get(id=id, is_active=True)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(products, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        products.title = serializer.validated_data.get('title')
        products.description = serializer.validated_data.get('description')
        products.price = serializer.validated_data.get('price')
        products.category_id = serializer.validated_data.get('category_id')
        products.is_active = serializer.validated_data.get('is_active')
        products.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(products, many=False).data)
    elif request.method == 'DELETE':
        products.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        products = Review.objects.get(id=id, is_active=True)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(products, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        products.text = serializer.validated_data.get('text')
        products.stars = serializer.validated_data.get('stars')
        products.product_id = serializer.validated_data.get('product_id')
        products.is_active = serializer.validated_data.get('is_active')
        products.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(products, many=False).data)
    elif request.method == 'DELETE':
        products.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        products = Category.objects.filter(is_active=True)
        count = products.count()
        data = CategoryListSerializer(products, many=True).data
        return Response(data=data)
    
    if request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        name = serializer.validated_data.get('name')
        count = int(serializer.validated_data.get('count'))
        is_active = serializer.validated_data.get('is_active')
        products = Category.objects.create(
            name=name,
            count=count,
            is_active=is_active
        )

        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(products, many=False).data)

@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.filter(is_active=True)
        data = ProductListSerializer(products, many=True).data
        return Response(data=data)
    
    if request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        is_active = serializer.validated_data.get('is_active')

        products = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id,
            is_active=is_active
        )


        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(products, many=False).data)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET': 
        products = Review.objects.filter(is_active=True)
        data = ReviewListSerializer(products, many=True).data
        return Response(data=data)
    
    if request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')
        is_active = serializer.validated_data.get('is_active')
        products = Review.objects.create(
            text=text,
            stars=stars,
            product_id=product_id,
            is_active=is_active
        )

        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(products, many=False).data)
    

