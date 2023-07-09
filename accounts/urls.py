from django.urls import path

from .views import (account_settings, createOrder, customers, customers_view,
                    deleteOrder, home, loginPage, logoutPage, orders_view,
                    products, registerPage, updateOrder, userPage)

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),

    path('', home, name='home'),
    path('user', userPage, name='userPage'),
    path('products/', products, name='products'),
    path('settings/', account_settings, name='settings'),

    path('customers/<str:pk>', customers, name='customers'),
    path('create_order/<str:pk>', createOrder, name='create_order'),
    path('update_order/<str:pk>', updateOrder, name='update_order'),
    path('delete_order/<str:pk>', deleteOrder, name='delete_order'),

    path('customers/', customers_view, name='customers_view'),
    path('orders/', orders_view, name='orders_view'),
    path('orders/<str:status>/', orders_view, name='filtered_orders_view'),
]