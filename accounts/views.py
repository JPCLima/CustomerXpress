from django.shortcuts import render

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
    context = {
        'customer': customer
    }
    return render(request, 'accounts/customer.html', context=context)
