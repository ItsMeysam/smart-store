from django.urls import path
from product_module import views

urlpatterns = [
    path('product-list', views.ProductListView.as_view(), name='product_list'),

]