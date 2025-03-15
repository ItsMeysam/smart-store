from django.urls import path
from product_module import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)