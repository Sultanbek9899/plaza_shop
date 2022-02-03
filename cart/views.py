from django.shortcuts import render
from django.views import  View
# Create your views here.
from cart.cart import Cart
from products.models import Product
from django.http import  HttpResponseRedirect
from django.shortcuts import  reverse
from django.views.generic import  TemplateView

class AddCartView(View):
    template_name = "cart.html"
    cart_class = Cart

    def get(self,request,product_id):
        cart = self.cart_class(self.request)
        product = Product.objects.get(id=product_id)
        cart.add(product=product)
        return HttpResponseRedirect(reverse("index"))


class CartPageView(TemplateView):
    template_name = "cart.html"

