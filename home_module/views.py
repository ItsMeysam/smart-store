from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from product_module.models import Product


class HomeView(TemplateView):
    template_name = 'home_module/home_page_view.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products:Product = Product.objects.all()
        Product.objects.order_by('-created_at')[:5]



        paginator = Paginator(products, 4)
        page_number = self.request.GET.get('page', 1)

        try:
            page_obj = paginator.get_page(page_number)
        except:
            raise Http404("صفحه مورد نظر موجود نیست.")

        context['page_obj'] = page_obj
        context['products'] = page_obj.object_list
        context['paginator'] = paginator
        return context



def site_header_component(request):
    return render(request, 'shared/site_header_component.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')


def about_us(request):
    return render(request, 'home_module/about_us.html')

def popular_question(request):
    return render(request, 'home_module/popular_question.html')
