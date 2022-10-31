
from dataclasses import field
import email
import django_filters
from django.contrib.auth import forms
from website.models import Custom
from paystack.models import Paystack


class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name='email', lookup_expr='iexact')
    mobile_no = django_filters.CharFilter(field_name='phone_number', lookup_expr='iexact')

    class Meta:
        model = Custom
        fields = ('email', 'phone_number')

class PaystackFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name='email', lookup_expr='iexact')
    amount = django_filters.CharFilter(field_name='amount', lookup_expr='iexact')
    date = django_filters.DateFilter(field_name='generated', lookup_expr='iexact')

    class Meta:
        model = Paystack
        fields = ('email','amount', 'generated')

class FlutterwaveFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name='email', lookup_expr='iexact')
    amount = django_filters.CharFilter(field_name='amount', lookup_expr='iexact')
    date = django_filters.DateFilter(field_name='generated', lookup_expr='iexact')

    class Meta:
        model = Paystack
        fields = ('email','amount', 'generated')