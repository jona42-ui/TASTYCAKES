from distutils.command import upload
from tabnanny import verbose
from django.db import models
from django.utils.html import mark_safe

#Banner
class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/")
    alt_text=models.CharField(max_length=300)
    
    class Meta:
        verbose_name_plural='1. Banners'

#define category model
class Category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="cat_imgs/")
    price=models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural='2. Categories'
        
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

#color
class Color(models.Model):
    title=models.CharField(max_length=50)
    color_code=models.CharField(max_length=50)
    image=models.ImageField(upload_to="color_imgs/")
    price=models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural='3. Color'

    def __str__(self):
        return self.title

#size
class Size(models.Model):
    title=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural='4. Size'

    def __str__(self):
        return self.title

#Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=200)
    detail=models.TextField()
    specs=models.TextField()
    price=models.PositiveIntegerField()
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Color=models.ForeignKey(Color,on_delete=models.CASCADE)
    Size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default= True)  
    is_featured=models.BooleanField(default=True) 
    
    class Meta:
        verbose_name_plural='5. Product'
 
    
#ProductAttribute    
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Color=models.ForeignKey(Color,on_delete=models.CASCADE)
    Size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    class Meta:
        verbose_name_plural='6. ProductAttribute'

    def __str__(self):
        return self.product.title