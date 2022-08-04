from django.urls import path
from . import views
app_name = 'flutterwave'

urlpatterns = [
    path('flutterwave/', views.Deposit, name='flutterwave_deposit'),
    path('<str:reference>/', views.confirm_payment, name='confirm_payment'),   
]