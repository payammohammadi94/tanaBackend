# Generated by Django 4.0.5 on 2022-06-27 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_brand_color_comment_product_size_varientproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='home.brand', verbose_name='برند'),
        ),
    ]