from django.urls import path
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('category_product_list/<int:category_id>',views.category_product_list, name='category_product_list'),
    path('search', views.search, name='search'),
    path('category_list',views.category_list, name='category_list'),
    path('color_list',views.color_list, name='color_list'),
    path('product_list',views.product_list, name='product_list'),
    path('category_product_list/<int:cat_id>',views.category_product_list, name='category_product_list'),
    path('color_product_list/<int:color_id>',views.color_product_list, name='color_product_list'),
    # path('product/<str:slug>/<int:id>',views.product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)