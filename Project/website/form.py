from dataclasses import field
import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from paystack.models import Userhistory
import django_filters


class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username', 'phone_number')

class FileterForm(django_filters.FilterSet):
    start_date =  django_filters.DateFilter(field_name='date_created', lookup_expr='gte')
    end_date =  django_filters.DateFilter(field_name='date_created', lookup_expr='lte')
    class Meta:
        model = Userhistory
        fields = ('date_created',)




