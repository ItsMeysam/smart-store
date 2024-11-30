from django.urls import path
from product_module import views

urlpatterns = [
    path('product', views.product_page_view, name='product_page_view'),
]