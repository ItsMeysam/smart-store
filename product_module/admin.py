from django.contrib import admin
from .models import Product, ProductBrand, ProductCategory, ProductTag

admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
