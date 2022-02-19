from django.urls import path

from . import views
urlpatterns = [
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
]