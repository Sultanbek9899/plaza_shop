from django.urls import path
from products import views

urlpatterns = [
    path("", views.index, name='index'),
    path("products/", views.product_list, name="product_list"),
    path("products/<str:category_slug>/", views.product_list, name="category_list"),
    path("products/<str:category_slug>/<str:subcategory_slug>/",
         views.product_list,
         name="subcategory_list"
         )
    #http://127.0.0.1:8000/products/elektronika/televizory/
]
