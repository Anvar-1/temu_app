from django.urls import path
from .views import ProductListView, CategoryListView, SubcategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('subcategories/', SubcategoryListView.as_view(), name='subcategory-list'),
]