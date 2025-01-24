from rest_framework import serializers
from .models import Product, Category, Subcategory

class ProductSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_total_likes(self, obj):
        return obj.total_likes()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'