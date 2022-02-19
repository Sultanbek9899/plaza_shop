from django.shortcuts import render, reverse

# Create your views here.
from django.views.generic import FormView
from .forms import OrderCheckoutForm
from .models import OrderItem, Order
from backend.apps.cart.cart import Cart


class CheckoutView(FormView):
    template_name = "checkout.html"
    form_class = OrderCheckoutForm

    def form_valid(self, form):
        instance = form.save(commit=False) # Создается Order
        cart = Cart(self.request)
        instance.total_sum = cart.get_total_price()
        instance.save()
        for item in cart:
            OrderItem.objects.create(
                order=instance,
                quantity=item['quantity'],
                price=item['price'],
                product=item['product']
            )
        cart.clear()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")
