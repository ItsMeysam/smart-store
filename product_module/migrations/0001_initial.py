# Generated by Django 5.1.1 on 2024-12-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('short_description', models.CharField(db_index=True, max_length=200, verbose_name='توضیحات کوتاه')),
                ('price', models.IntegerField(verbose_name='قیمت محصول')),
                ('description', models.TextField(max_length=300, verbose_name='درباره محصول')),
                ('slug', models.SlugField(default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images', verbose_name='عکس محصول')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
