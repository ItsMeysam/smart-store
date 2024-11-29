from django.shortcuts import render
from django.views.generic import View



# productView class for show product page
class ProductView(View):
    template_name = 'product_module/product_view.html'