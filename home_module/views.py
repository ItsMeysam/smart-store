from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def view_home_page(request):
    return render(request, 'home_module/view_home_page.html')

def site_header_component(request):
    return render(request, 'shared/site_header_component.html')

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html')