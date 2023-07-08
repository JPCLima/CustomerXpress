from django.urls import path

from .views import (account_settings, createOrder, customers, deleteOrder,
                    home, loginPage, logoutPage, products, registerPage,
                    updateOrder, userPage)

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
]