# Generated by Django 4.0.3 on 2022-09-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_remove_product_price_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='100', max_length=30),
        ),
    ]
