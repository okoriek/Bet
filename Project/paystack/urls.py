from django.urls import path
from . import views
app_name = 'paystack'

urlpatterns = [
    path('paystack/', views.InitializeDeposit, name='paystack_deposit'),
    path('<str:reference>/', views.verify_payment, name='verify_payment'),   
]