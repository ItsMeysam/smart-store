# Generated by Django 5.1.5 on 2025-02-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت محصول'),
        ),
    ]
