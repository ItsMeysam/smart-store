from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from product_module.models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list_view.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 4



    def get_queryset(self):
        """
        این متد برای انجام مرتب‌سازی محصولات بر اساس قیمت است.
        اگر پارامتر 'sort' در URL باشد، از آن استفاده می‌کند.
        """
        sort_order = self.request.GET.get('sort', 'asc')  # پیش‌فرض 'asc'
        
        if sort_order == 'asc':
            return Product.objects.all().order_by('price')
        elif sort_order == 'desc':
            return Product.objects.all().order_by('-price')
        else:
            return Product.objects.all() 

class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail_view.html'
    model = Product




