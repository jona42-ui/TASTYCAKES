
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
import datetime

# Create your models here.

categories = [
    ('Select Category','Select Category'),
    ('Popular flavours','Popular flavours'),
    ('Design Cakes','Design Cakes'),
    ('Jar Cakes','Jar Cakes'),
    ('Brownies','Brownies')
]

class cake_list(models.Model):
    name = models.CharField(max_length=30)
    slug =models.SlugField(max_length=100, db_index=True, default='null')
    category = models.CharField(max_length=30, choices = categories , default = 'Select Category')
    description = models.CharField( max_length=300)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class orders(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField(max_length=64)
    paid_amount = models.IntegerField()
    phone = models.CharField(max_length=30)
    house_name = models.CharField(max_length=80)
    location = models.CharField(max_length=60)
    pin = models.IntegerField()
    date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    cake_list = models.ForeignKey(cake_list,on_delete = models.CASCADE)
    status = models.CharField(max_length=30, default='Pending')
    order_status = models.CharField(max_length=30, default='True')


class messages(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=64)
    message = models.CharField( max_length=250)
    date = models.DateTimeField(auto_now = True)
    
    
class Product(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=70,
        verbose_name='Product Name'
    )

    description = models.TextField(
        max_length=800,
        verbose_name='Description'
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[
            validators.MinValueValidator(50),
            validators.MaxValueValidator(100000)
        ]
    )
    def __str__(self):
        return self.name
    
    file = models.FileField(upload_to="product_files/", blank=True,null=True)
    
    
    