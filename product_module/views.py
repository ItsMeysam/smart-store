from django.shortcuts import render
from django.views.generic import View


def product_page_view(request):
    return render(request, 'product_module/product_page_view.html')