from rest_framework import generics
from .models import Product, Category, Subcategory
from .serializers import ProductSerializer, CategorySerializer, SubcategorySerializer

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_name = self.request.query_params.get('search', None)
        if search_name:
            queryset = queryset.filter(title__icontains=search_name)
        return queryset

class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class SubcategoryListView(generics.ListCreateAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        return Subcategory.objects.all()


