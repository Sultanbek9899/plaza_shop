from rest_framework import  serializers
from products.models import Product

class ProductListSerializer(serializers.ModelSerializer):

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


