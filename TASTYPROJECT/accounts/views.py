from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages as mssg
from products.models import cake_list,orders,messages
from .forms import SignUpForm
from products.forms import make_order_form,message_form
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.db.models import Q
# Create your views here.

def indexpage(request):
    # context = dict()
    # context['title'] = 'indexpage'
    # return render(request,'home/index1.html',context)
    return redirect('/home/')

def aboutus(request):
    context = dict()
    context['title'] = 'about-us'
    return render(request,'accounts/about-us.html',context)


def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    items = cake_list.objects.filter(
        Q(name__contains=q) |
        Q(category__contains = q) |
        Q(description__contains=q) |
        Q(price__contains=q) 
        )
    # context = dict()
    # items = cake_list.objects.all()
    # product = get_object_or_404(cake_list,id=id,slug = slug)
    cart_product_form = CartAddProductForm()
    # context['items'] = items
    context = {'items':items,'cart_product_form':cart_product_form}
    return render(request,'accounts/homepage.html',context)

def category_filter(request,category_name):
    context = dict()
    items = cake_list.objects.filter(category = category_name)
    context['items'] = items
    return render(request,'accounts/homepage.html',context)

def sign_up(request):
    form = SignUpForm(request.POST or None)
    context= dict()
    context["form"] = form
    
    if request.method == "POST":
        if form.is_valid(): 
            user=form.save()
            
            login(request,user)      
            return redirect(reverse('accounts:homepage'))
        else:
            mssg.info(request,form.errors)
            return render(request,'accounts/sign_up.html',context)
    return render(request,'accounts/sign_up.html',context)

def log_in(request):
    form = AuthenticationForm(request, data=request.POST)
    context= dict()
    context["form"] = form
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username,password=password)
            login(request,user)  
            if user.is_superuser:
                return redirect(reverse('admin:dashboard'))
            if user:    
                return redirect(reverse('accounts:homepage'))
        else:
            return render(request,'accounts/log_in.html',context)    
    return render(request,'accounts/log_in.html',context)

def log_out(request):
    logout(request)
    return redirect(reverse('accounts:log-in'))

def my_orders(request):
    context = dict()
    user = request.user
    myorders = orders.objects.filter(user_id = user.id).order_by('-date')
    context['orders'] = myorders
    return render(request,'accounts/my_orders.html',context)

def cancel_order(request,id):
    order = orders.objects.get(id = id)
    order.order_status = 'Cancelled'
    order.save()
    mssg.info(request,'Order cancelled successfully. Refund will be credited to your bank account within 3-4 working days')
    return redirect(reverse('accounts:my-orders'))


def messages(request):
    context = dict()
    form = message_form(request.POST or None)
    context['form'] = form
    if request == request.POST:
        if form.is_valid: 
            
            mssg.info(request,'Thank you for filling the form. Will get back to you soon')
    return render(request,'accounts/messages.html',context)


def checkout(request,id):
    cart = Cart(request)
    context = dict()
    customer=request.user
    form = make_order_form(request.POST or None)
    context['customer'] = customer
    context['form'] = form
    context['cart'] = cart
    if request.method == "POST":
        if form.is_valid(): 
            order=form.save(commit=False)

            # order.user_id = customer.id
            order.user = request.user
            # order.cake_list_id = id
            order.save()
            # context['id'] = id
            return render(request,'accounts/landingpage.html',context)

    return render(request,'accounts/delivery_details.html',context)


def payment_cancelled(request):
    cancel_order = orders.objects.latest('id')
    if cancel_order.status == 'Pending':
        cancel_order.delete()
    return redirect(reverse('accounts:homepage'))

def payment_successfull(request):
    success_order = orders.objects.latest('id')
    success_order.status = 'Success'
    success_order.save()
    return redirect(reverse('accounts:my-orders'))
