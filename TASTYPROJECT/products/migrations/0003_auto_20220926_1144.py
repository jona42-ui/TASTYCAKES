# Generated by Django 3.2.15 on 2022-09-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake_list',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cake_list',
            name='slug',
            field=models.SlugField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='cake_list',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
