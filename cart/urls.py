from django.urls import path
from . import views

urlpatterns = [
    path("", views.CartPageView.as_view(), name="cart_page"),
    path("add/<int:product_id>/", views.add_cart, name="add_cart")
]