from django.urls import path

from .views import customers, home, products

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customers/', customers, name='customers'),
]