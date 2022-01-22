from django.urls import path
from products import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/<str:category_slug>/", views.ProductListView.as_view(), name="category_list"),
    path("products/<str:category_slug>/<str:subcategory_slug>/",
         views.ProductListView.as_view(),
         name="subcategory_list"
         )
    #http://127.0.0.1:8000/products/elektronika/televizory/
]
