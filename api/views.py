from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductListSerializer
from products.models import Product


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.filter(is_active=True)


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


# Create your views here.
