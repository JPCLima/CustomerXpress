from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, ModelForm

from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer']


class CreateUserForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']