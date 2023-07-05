from django.urls import path

from .views import (createOrder, customers, deleteOrder, home, products,
                    updateOrder)

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customers/<str:pk>', customers, name='customers'),
    path('create_order/', createOrder, name='create_order'),
    path('update_order/<str:pk>', updateOrder, name='update_order'),
    path('delete_order/<str:pk>', deleteOrder, name='delete_order'),
]