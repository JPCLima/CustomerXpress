import django_filters
from django_filters import CharFilter, DateFilter

from .models import *


class OrderFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='start date')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='end date')
    note = CharFilter(field_name='note', lookup_expr='icontains')


    class Meta:
        model = Order
        fields = ['product', 'status','start_date', 'end_date', 'note'] 
        