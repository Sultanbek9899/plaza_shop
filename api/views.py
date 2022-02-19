from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductSerializer, CategorySerializer , SubCategorySerializer
from products.models import Product, Category, SubCategory


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



# Create your views here.
