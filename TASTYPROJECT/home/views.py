from itertools import product
from turtle import color
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Category,Color,Product,ProductAttribute
from products.models import cake_list

#Home page 
def index(request):
    data=cake_list.objects.all()
    return render(request, 'index1.html',{'data':data})

#Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})

#Flavours
def color_list(request):
    data=Color.objects.all().order_by('-id')
    return render(request,'color_list.html',{'data':data})

#Product list
def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('Category__title')
    Colors=Product.objects.distinct().values('Color__title','Color__id','Color__color_code')
    Sizes=Product.objects.distinct().values('Size__title','Size__id')
    #price=ProductAttribute.distinct().values('')
    return render(request,'product_list.html',
                  {
                      'data':data,
                      'cats':cats,
                      'Colors':Colors,
                      'Sizes':Sizes,
                  }
                  )
#product list according to category
def category_product_list(request,cat_id,):
    category=Category.objects.get(id=cat_id)
    data=Product.objects.filter(Category=category).order_by('-id')
    cats=Product.objects.distinct().values('Category__title','Category__id')
    Colors=Product.objects.distinct().values('Color__title','Color__id','Color__color_code')
    Sizes=Product.objects.distinct().values('Size__title','Size__id')
    return render(request,'category_product_list.html',
                  {
                      'data':data,
                      'cats':cats,
                      'Colors':Colors,
                      'Sizes':Sizes,
                  }
                  )    
#product list according to color
def color_product_list(request,color_id):
    color=Color.objects.get(id=color_id)
    data=Product.objects.filter(Color=color).order_by('-id')
    cats=Product.objects.distinct().values('Category__title','Category__id')
    Colors=Product.objects.distinct().values('Color__title','Color__id','Color__color_code')
    Sizes=Product.objects.distinct().values('Size__title','Size__id')
    return render(request,'color_product_list.html',
                  {
                      'data':data,
                      'cats':cats,
                      'Colors':Colors,
                      'Sizes':Sizes,
                  }
                  )        
#product_detail
# def product_detail(request,slug,id):
#     product=Product.objects.get(id=id)
#     return render(request,'product_detail.html',{'data':product})

#Search
def search(request):
    q=request.GET['q']
    data=Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})    