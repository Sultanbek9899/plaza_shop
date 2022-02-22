from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views import  View
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
# Create your views here.

from .models import Category, Product, SubCategory
from .forms import SearchForm
from backend.apps.cart.forms import CartAddProductForm
from backend.apps.cart.cart import Cart

class IndexView(FormMixin,TemplateView):
    template_name = "index.html"
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['search_form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        print('asf')
        form = self.form_class(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data.get('searchfield')

            products = Product.objects.filter(name__contains=search_text)
            return render(request, 'result.html', {'products': products})


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 2

    def get_queryset(self, **kwargs):
        category_slug = self.kwargs.get("category_slug")
        subcategory_slug = self.kwargs.get("subcategory_slug")
        if subcategory_slug:
            subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
            queryset = self.model.objects.filter(
                is_active=True,
                subcategory=subcategory)
            return queryset
        elif category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(is_active=True, category=category)
            return queryset
        queryset = self.model.objects.filter(is_active=True)
        return queryset


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    form_class = CartAddProductForm

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        related_products = Product.objects.filter(is_active=True, subcategory=self.object.subcategory)
        context["related_products"] = related_products[:4] if len(related_products) > 4 else related_products
        context["cart_form"] = CartAddProductForm()
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            cart = Cart(request)
            cart.add(
                product=product,
                quantity=form.cleaned_data.get('quantity'),
                update_quantity=form.cleaned_data.get('update')
            )
            return redirect('cart_page')







