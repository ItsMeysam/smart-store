from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    mobile = models.CharField(max_length=11, verbose_name='موبایل')
    message = models.TextField(verbose_name='پیام')
    is_read_by_admin = models.BooleanField(verbose_name='دیده شده / نشده', null=True)
    response = models.TextField(verbose_name='پاسخ به پیام کاربر', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تماس باما'
        verbose_name_plural = 'لیست تماس باما'
