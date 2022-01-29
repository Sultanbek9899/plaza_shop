from django.urls import path
from . import views
urlpatterns = [
    path("add/<int:product_id>/", views.AddCartView.as_view(), name="add_cart")
]