from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .decorators import admin_only, allowed_users, unauthorized_user
from .filters import OrderFilter
from .forms import CreateUserForm, CustomerForm, OrderForm
from .models import *


@unauthorized_user
def registerPage(request):   
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # Add the group customer account type
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            # Create a Customer object and link it to the user
            customer = Customer.objects.create(user=user, name=username)

            # Save additional customer data
            customer.phone = form.cleaned_data.get('phone')
            customer.email = form.cleaned_data.get('email')
            customer.address = form.cleaned_data.get('address')

            # Save fields to Customer object
            customer.save()

            messages.success(request, f'User created successfully {username}')
            return redirect('login')

    context = {'form': form}

    return render(request, 'accounts/register.html', context=context)

@unauthorized_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'accounts/login.html', context=context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    orders_total = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'orders_total': orders_total,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending
        }
    return render(request, 'accounts/user.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('userPage')

    context = {'form': form, 'customer':customer}
    return render(request, 'accounts/account_settings.html', context=context)


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    orders_total = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders[:8],
        'customers': customers[:8],
        'orders_total': orders_total,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
    }
    return render(request, 'accounts/dashboard.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_total = orders.count()

    customFilter = OrderFilter(request.GET, queryset=orders)
    orders = customFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'orders_total': orders_total,
        'filter': customFilter
    }
    return render(request, 'accounts/customer.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):    
    customer = Customer.objects.get(pk=pk)
    form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer 
            order.save()
            return redirect('/')

    context = {'form': form, 'customer': customer}
    return render(request, 'accounts/order_form.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    # Get the order
    order = Order.objects.get(id=pk)
    customer = order.customer
    form = OrderForm(instance=order)

    # Save the order into the same instance
    if request.method == 'POST':
        mutable_post = request.POST.copy()  
        mutable_post['customer'] = customer.id 
        form = OrderForm(mutable_post, instance=order)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
        

    context = {'form': form, 'customer':order.customer}
    return render(request, 'accounts/order_form.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers_view(request):
    customers = Customer.objects.all()

    p_customers = Paginator(customers, 7)
    page_c = request.GET.get('customers_page')
    customers = p_customers.get_page(page_c)

    context = {'customers': customers}
    return render(request, 'accounts/customers_page.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def orders_view(request, status=None):
    orders = Order.objects.all()

    if status:
        orders = orders.filter(status=status)

    p_orders = Paginator(orders, 7)
    page_o = request.GET.get('orders_page')
    orders = p_orders.get_page(page_o)

    context = {'orders': orders}
    return render(request, 'accounts/orders_page.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)


    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order': order}
    return render(request, 'accounts/delete.html', context=context)

    