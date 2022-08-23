from django.shortcuts import render,redirect
from dkapp.models import *
from dkapp.forms import OrderForm,CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

def user(request):
    return render(request,'user.html')

@unauthenticated_user
def register(request):
   
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
              user=form.save()
              username =form.cleaned_data.get('username')
               
              group = Group.objects.get(name='customer')
              user.groups.add(group)
               
          
               
              messages.success(request, 'Account was created for ' + username )
              return redirect('login')
            
    context={'form':form}
    return render(request,'register.html',context)

@unauthenticated_user
def user_login(request):
     if request.user.is_authenticated:
            return redirect('home')
     else:
         if request.method == 'POST':
          username=request.POST['username']
          password=request.POST['password']
          user = authenticate(request,username=username,password=password) 
          if user is not None:
              login(request,user)
              return redirect('/')
          else:
               messages.info(request,'Username OR Password is incorrect')
     context= {}
     return render(request,'login.html',context)
from .decorators import unauthenticated_user, allowed_users, admin_only


def logoutuser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders =   orders.count()
    deliverd =   orders.filter(status='Delivereds').count()
    pending =   orders.filter(status='Pending').count()
    outfor= orders.filter(status='Out of delivery').count()
    
 
    context= { 'orders':orders,
              'customers':customers,
              'total_customers':total_customers,
              'total_orders':total_orders,
              'deliverd':deliverd,
              'pending':pending ,
              'outfor':outfor
              }
    return render(request,'index.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products=Product.objects.all()
    
    return render(request,'products.html',{'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    orders_count=orders.count()
    
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders= myFilter.qs
 
    
    context={'customer':customer,
             'orders':orders,
             'orders_count':orders_count,
             'myFilter':myFilter}
    
    return render(request,'customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def createorder(request, pk):
    #OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    #formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
            form = OrderForm(request.POST)
          #  formset = OrderFormSet(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('/')

    context = {'form':form}
    return render(request, 'order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateorder(request,pk):
    order = Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context={'form':form}
    return render(request,'update_order.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context={'item': order }
    return render(request,'delete.html',context)

