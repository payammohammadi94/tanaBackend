# Generated by Django 4.0.5 on 2022-07-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_comment_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='varientproduct',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد موجودی محصول'),
        ),
    ]
