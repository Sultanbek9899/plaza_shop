from django.shortcuts import render, redirect
from django.views import  View
# Create your views here.
from cart.cart import Cart
from products.models import Product
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import TemplateView


# class AddCartView(View):
#     template_name = "cart.html"
#     cart_class = Cart
#
#     def get(self, product_id):

def add_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product, quantity=1)
    print(request.session.get('cart'))
    cart.save()
    return redirect("cart_page")


class CartPageView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartPageView, self).get_context_data(**kwargs)
        cart = Cart(self.request)
        print(len(cart))

        print(self.request.session.get("cart"))
        print(cart)
        context['cart'] = cart
        return context

