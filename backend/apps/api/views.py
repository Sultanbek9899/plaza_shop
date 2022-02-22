from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import (
    ProductSerializer,
    CategorySerializer ,
    SubCategorySerializer,
    ProductCreateSerializer
)
from backend.apps.products.models import Product, Category, SubCategory
from rest_framework.response import  Response
from rest_framework import  status

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryListAPIView(ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug', None)
        print(self.kwargs.get('category_slug', None))
        if category_slug is not None:
            qs = SubCategory.objects.filter(category__slug=category_slug)
            return qs
        qs = SubCategory.objects.all()
        return qs


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer




# Create your views here.
