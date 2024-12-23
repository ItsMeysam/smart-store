from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from product_module.models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list_view.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 4


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail_view.html'
    model = Product



