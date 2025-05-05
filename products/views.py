from rest_framework.decorators import api_view
from rest_framework.response import Response    
from rest_framework import status
from products.serializers import (
    CategoryDetailSerializer,
    CategoryListSerializer,
    ProductDetailSerializer, 
    ProductListSerializer, 
    RewiewDetailSerializer, 
    RewiewListSerializer
)
from .models import Category, Product, Rewiew


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        film = Category.objects.get(id=id, is_active=True)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(film, many=False).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        film = Product.objects.get(id=id, is_active=True)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(film, many=False).data
    return Response(data=data)


@api_view(['GET'])
def rewiew_detail_api_view(request, id):
    try:
        film = Rewiew.objects.get(id=id, is_active=True)
    except Rewiew.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = RewiewDetailSerializer(film, many=False).data
    return Response(data=data)

@api_view(['GET'])
def category_list_api_view(request):
    films = Category.objects.filter(is_active=True)
    data = CategoryListSerializer(films, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_list_api_view(request):
    films = Product.objects.filter(is_active=True)
    data = ProductListSerializer(films, many=True).data
    return Response(data=data)

@api_view(['GET'])
def rewiew_list_api_view(request):
    films = Rewiew.objects.filter(is_active=True)
    data = RewiewListSerializer(films, many=True).data
    return Response(data=data)





