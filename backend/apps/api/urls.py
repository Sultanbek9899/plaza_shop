from django.urls import path

from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    SubCategoryListAPIView,
    ProductCreateAPIView
)
urlpatterns = [
    path('products_list/', ProductListAPIView.as_view()),
    path('product_details/<int:pk>/', ProductDetailAPIView.as_view()),
    path('category_list/', CategoryListAPIView.as_view()),
    path('subcategory_list/', SubCategoryListAPIView.as_view()),
    path('subcategories_by_category/<slug:category_slug>/', SubCategoryListAPIView.as_view()),
    path('create/product/', ProductCreateAPIView.as_view())
]