from django.urls import path
from .views import ProductListView, CategoryListView, SubcategoryListView, ProductDetailView, ProductUpdateView, \
    ProductLikeView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('subcategories/', SubcategoryListView.as_view(), name='subcategory-list'),
    path('products/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/like/', ProductLikeView.as_view(), name='product-like'),

]