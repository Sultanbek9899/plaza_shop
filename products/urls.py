from django.urls import path
from products.views import index

urlpatterns = [
    path("", index, name='index'),
]