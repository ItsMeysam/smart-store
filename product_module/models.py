from django.db import models


#creat main class for product
class Product(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام محصول')
    # category = models.ManyToManyField(ProductCategory, related_name=''product_categories,
    # verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=300, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(default='', null=False, db_index=True, blank=True, max_length=200,
                            unique=True, verbose_name='عنواد در ulr')

    # def absolute_url(self):
    #     return reverse('product_detail', agrs=[self.slug])


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.title} - ({self.price})'


    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'