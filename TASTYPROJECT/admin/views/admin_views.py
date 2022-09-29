from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from products.models import orders,messages
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.

def dashboard(request):
    context = dict()
    context['orders'] = orders.objects.all().order_by('-date')
    context['messages'] = messages.objects.all().order_by('-date')
    return render(request,'admin/dashboard.html',context)

def update_profile(request):
    context = dict()
    admin_user = User.objects.filter(is_superuser = True ).first()
    context['user'] = admin_user
    if request == request.POST:
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        admin_user.username = username
        admin_user.first_name = first_name
        admin_user.email = email
        admin_user.save()
        form= update_profile(request.POST)
        if form.is_valid():
           form.save()
        messages.success(request, 'Your profile is updated successfully')
        return redirect(to='admin:update-profile')
        
    return render(request,'admin/update_profile.html',context)

def user_list(request):
    context = dict()
    user = User.objects.filter(is_superuser = False )
    context['users'] = user
    return render(request,'admin/user_list.html',context)

