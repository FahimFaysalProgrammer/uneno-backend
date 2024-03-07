from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
# class ProductViewset(viewsets.ModelViewSet):
#     queryset = models.Product.objects.all()
#     serializer_class = serializers.ProductSerializer
    
    
class SizeViewset(viewsets.ModelViewSet):
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer
    
    
class ColorViewset(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer



class CategorySpecificProduct(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        product_id = request.query_params.get("product_id")
        if product_id:
            return queryset.filter(product=product_id)
        return queryset

class CategoryViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [CategorySpecificProduct]


# Pagination:
class ProductPagination(pagination.PageNumberPagination):
    page_size = 12 # items per page
    page_size_query_param = page_size
    max_page_size = 100


class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = ProductPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer