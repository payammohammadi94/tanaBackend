# Generated by Django 4.0.5 on 2022-07-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_comment_total_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
