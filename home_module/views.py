from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from product_module.models import Product


class HomeView(TemplateView):
    template_name = 'home_module/home_page_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context



def site_header_component(request):
    return render(request, 'shared/site_header_component.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')


def about_us(request):
    return render(request, 'home_module/about_us.html')

def popular_question(request):
    return render(request, 'home_module/popular_question.html')

