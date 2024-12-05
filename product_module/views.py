from django.shortcuts import render
from django.views.generic import View, ListView
from product_module.models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list_view.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        return context


def product_detail(request):
    return render(request, 'product_module/product_detail.html')
