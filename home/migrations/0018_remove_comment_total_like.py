# Generated by Django 4.0.5 on 2022-07-01 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='total_like',
        ),
    ]
