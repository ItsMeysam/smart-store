from django.urls import path
from product_module import views

urlpatterns = [
    path('product-view', views.ProductView.as_view(), name='product_view'),
]