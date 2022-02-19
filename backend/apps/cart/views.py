from django.shortcuts import render, redirect
from django.views import  View
# Create your views here.
from .cart import Cart
from backend.apps.products.models import Product
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import TemplateView
from .forms import  CartAddProductForm
from django.views.generic.edit import FormMixin

def add_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product, quantity=1, )
    return redirect("cart_page")


def add_cart_from_form(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(
            product=product,
            quantity=form.cleaned_data.get('quantity'),
            update_quantity=form.cleaned_data.get('update')
        )
        return redirect('cart_page')
    return redirect('cart_page')




class CartPageView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartPageView, self).get_context_data(**kwargs)
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                         'update': True
                         }
            )
        context['cart'] = cart
        return context


def cart_remove(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect('cart_page')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_page')
