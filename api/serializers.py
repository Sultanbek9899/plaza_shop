from rest_framework import  serializers
from products.models import Product, Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'category']


class ProductSerializer(serializers.ModelSerializer):
    # Преобразует поля в отношениях в string из модели
    # subcategory = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()


    # subcategory = serializers.SlugRelatedField(slug_field="name",read_only=True)

    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'subcategory',
            'description',
            'price',
            'image',
            'created',
            'updated',
        ]


