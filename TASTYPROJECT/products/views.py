import stripe
from django.core.mail import send_mail

from django.conf import settings
from django.http import JsonResponse
from django.views import View

from TASTYPROJECT.settings import STRIPE_SECRET_KEY
from .models import cake_list
from django.views.generic import TemplateView
from .models import Product
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProdutLandingPageView(TemplateView):
    template_name="landingpage.html"
    
    
    
    def get_context_data(self, **kwargs):
        product = cake_list.objects.get(name="mak")
        context=  super(ProdutLandingPageView,self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "STRIPE_PUBLIC_KEY":settings.STRIPE_PUBLIC_KEY,
            
        })
        return context
    



class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        product = cake_list.objects.get(id = product_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'ugx',
                        'unit_amount': product.price*100,
                        'product_data': {
                            'name': product.name ,
                            # 'images': ['https://www.facebook.com/106681217831349/photos/106683907831080/'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata = {
                "product_id": product.id,
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment-successfull/',
            cancel_url=YOUR_DOMAIN + '/payment-cancelled/',
        )
        return JsonResponse({
            'id' : checkout_session.id
        })
        
        
    @csrf_exempt
    def stripe_webhook(request):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
       )
            
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
    
    # Invalid signature
             return HttpResponse(status=400)
         # Handle the checkout.session.completed event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']

            # Fulfill the purchase...
            customer_email= session["customer_details"]["email"]
            product_id= session["metadata"]["product_id"]  
            
            product = Product.objects.get(id=product_id) 
            
            send_mail(
                subject="Congrats! from TastyCakes Mak Here is your purchased product details.".attach_file('product_files/'),
                message="Thanks for the purchase and here is the product you ordered from Tasty Cakes",
                recipient_list=[customer_email],
                from_email="jonathanthembo123@gmail.com"
                
            )
            


        return HttpResponse(status=200)
        

        
        



#deru product views
   