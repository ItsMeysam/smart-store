from django.db import models
from django.urls import reverse


# creat main class for products

class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='نام محصول')
    short_description = models.CharField(max_length=200, null=False, db_index=True, verbose_name='توضیحات کوتاه')
    price = models.IntegerField(verbose_name='قیمت محصول')
    description = models.TextField(max_length=300, verbose_name='درباره محصول')
    slug = models.SlugField(default='', null=False, db_index=True, blank=False,
                            max_length=200, unique=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to ='images/products', null=True, blank=True, verbose_name='عکس محصول')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')

    
    def get_absolute_url(self):
        return reverse('product_detail', args=[(self.id)])
    
    
    def __str__(self):
        return f'{self.title} - ({self.price})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
