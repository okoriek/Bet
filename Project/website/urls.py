from os import name
from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import (
   LoginView,
   LogoutView,
   PasswordResetView,
   PasswordResetDoneView,
   PasswordResetConfirmView,
   PasswordResetCompleteView
)
urlpatterns = [
   path('', views.Home, name='home'),
   path('register/', views.Register, name='register'),
   path('login/', LoginView.as_view(template_name = 'website/login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name = 'logout'),
   path('verification/<uidb64>/<token>/', views.EmailVerification, name='verification'),
   path('dashboard/', views.Dashboard, name = 'dashboard'),

   path('password_reset/', PasswordResetView.as_view(template_name = 'password/passwordreset.html'), name='reset_password'),
   path('password_reset_done/', PasswordResetDoneView.as_view(template_name = 'password/passwordresetdone.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'password/passwordresetconfirm.html'), name='password_reset_confirm'),
   path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name = 'password/passwordresetcomplete.html'), name='password_reset_complete'),
]