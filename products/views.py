from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from products.models import Category, Product, SubCategory


def index(request):
    return render(request, "index.html")


def product_list(request, category_slug=None, subcategory_slug=None):
    if subcategory_slug:
        try:
            subcategory=SubCategory.objects.get(slug=subcategory_slug)
        except Subcategory.DoesNotExist:
            print("Не найдено")
        products = Product.objects.filter(is_active=True, subcategory=subcategory)
    elif category_slug: # telefony-i-akss
        try:
            category = Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            print("Не найдено")
        products = Product.objects.filter(is_active=True, category=category)
    else:
        products = Product.objects.filter(is_active=True)
    context = {
        "products": products,
    }
    return render(request, 'product_list.html', context=context)

