from django.shortcuts import redirect, render

from .forms import OrderForm
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    orders_total = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'orders_total': orders_total,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
    }
    return render(request, 'accounts/dashboard.html', context=context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_total = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'orders_total': orders_total
    }
    return render(request, 'accounts/customer.html', context=context)

def createOrder(request):    
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context=context)

def updateOrder(request, pk):
    # Get the order
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    # Save the order into the same instance
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context=context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)


    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order': order}
    return render(request, 'accounts/delete.html', context=context)

    