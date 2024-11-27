from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class ProductView(View):
    template_name = 'product_module/product_view.html'