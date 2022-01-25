from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
# Create your views here.

from products.models import Category, Product, SubCategory


class IndexView(TemplateView):
    template_name = "index.html"


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


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
