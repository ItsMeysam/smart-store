from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from product_module.models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list_view.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # دریافت پارامتر 'sort' از URL (اگر وجود داشته باشد)
        sort_order = self.request.GET.get('sort', 'asc')  # به طور پیش‌فرض صعودی است


        # بخش دوم: جدیدترین محصولات (بر اساس تاریخ اضافه شدن)
        latest_products = Product.objects.all().order_by('-created_at')[:4]

        # مرتب‌سازی محصولات بر اساس قیمت
        if sort_order == 'desc':
            products = Product.objects.all().order_by('-price')  # بالاترین قیمت به پایین
        else:
            products = Product.objects.all().order_by('price')  # پایین‌ترین قیمت به بالا

        # محصولات تصادفی برای نمایش در بخش رندوم
        random_products = Product.objects.all().order_by('?')[:4]

        # صفحه‌بندی
        paginator = Paginator(products, self.paginate_by)
        page_number = self.request.GET.get('page', 1)

        try:
            page_obj = paginator.get_page(page_number)
        except:
            raise Http404("صفحه مورد نظر موجود نیست.")

        # اضافه کردن محصولات صفحه‌بندی شده و دیگر اطلاعات به context
        context['random_products'] = random_products
        context['page_obj'] = page_obj
        context['products'] = page_obj.object_list
        context['paginator'] = paginator
        context['latest_products'] = latest_products 

        return context



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




