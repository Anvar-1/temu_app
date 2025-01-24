from rest_framework import generics, permissions, status
from rest_framework.response import Response

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

class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductLikeView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        product = self.get_object()
        if request.user in product.likes.all():
            product.likes.remove(request.user)  # Agar foydalanuvchi allaqachon like bosgan bo'lsa, olib tashlaymiz
            return Response({'message': 'Like removed.'}, status=status.HTTP_200_OK)
        else:
            product.likes.add(request.user)  # Aks holda like qo'shamiz
            return Response({'message': 'Like added.'}, status=status.HTTP_201_CREATED)


