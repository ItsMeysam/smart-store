from django.contrib import admin
from .models import Product, ProductBrand, ProductCategory, ProductTag
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
        return "No Image"
    
    image_tag.allow_tags = True
    image_tag.short_description = 'Preview'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
