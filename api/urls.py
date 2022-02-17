from django.urls import path

from .views import ProductListAPIView, ProductDetailAPIView
urlpatterns = [
    path('products_list/', ProductListAPIView.as_view()),
    path('product_details/<int:pk>/', ProductDetailAPIView.as_view())
]