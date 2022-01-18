from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from products.models import Category


def index(request):
    return render(request, "index.html" )


def product_list(request):
    return render(request, 'product_list.html')

