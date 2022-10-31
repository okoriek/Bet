from django.urls import path
from . import views

urlpatterns = [
    path('withdrawal/', views.GetDepositData, name='getdeposit'),
]