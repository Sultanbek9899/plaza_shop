from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from .forms import OrderCheckoutForm
from .models import OrderItem, Order
from cart.cart import Cart


class CheckoutView(FormView):
    template_name = "checkout.html"
    form_class = OrderCheckoutForm
    success_url = 'index'

    def form_valid(self, form):
        instance = form.save() # Создается Order
        cart = Cart(self.request)
        for item in cart:
            OrderItem.objects.create(
                order=instance,
                quantity=item['quantity'],
                price=item['price'],
                product=item['product']
            )
        cart.clear()
        return super().form_valid(form)

