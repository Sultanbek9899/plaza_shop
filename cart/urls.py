from django.urls import path
from . import views

urlpatterns = [
    path("", views.CartPageView.as_view(), name="cart_page"),
    path("add/<int:product_id>/", views.add_cart, name="add_cart"),
    path("add_from_from/<int:product_id>/", views.add_cart_from_form, name="add_from_form"),
    path("remove/<int:id>/", views.cart_remove, name='cart_remove'),
    path('clear/', views.cart_clear, name='cart_clear'),
]