from django.urls import path
from products import views

from django.conf import settings
from django.conf.urls.static import static
from products.views import (CreateCheckoutSessionView,
                            ProdutLandingPageView,
                            
                            )

app_name='products'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('search', views.search, name='search'),
    # path('category_list',views.category_list, name='category_list'),
    # path('color_list',views.color_list, name='color_list'),
    # path('product_list',views.product_list, name='product_list'),
    # path('category_product_list/<int:cat_id>',views.category_product_list, name='category_product_list'),
    # path('color_product_list/<int:color_id>',views.color_product_list, name='color_product_list'),
    
    
    # path('webhooks/stripe/', views.stripe_webhook, name='stripe_webhook'),
    path('landingpage/',ProdutLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<int:id>',CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)