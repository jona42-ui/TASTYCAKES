from django.contrib import admin
from .models import Banner,Category,Color,ProductAttribute,Size,Product,ProductAttribute

admin.site.register(Banner)
admin.site.register(Color)
admin.site.register(Size)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','Category','Color','image','Size','price','status','is_featured')
    list_editable=('status','price','Color','image','Size','is_featured',)
admin.site.register(Product,ProductAdmin)

#productattribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','Color','Size')
    list_editable=('product','price','Color','Size',)

admin.site.register(ProductAttribute,ProductAttributeAdmin)