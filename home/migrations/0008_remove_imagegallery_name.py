# Generated by Django 4.0.5 on 2022-06-27 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagegallery',
            name='name',
        ),
    ]
