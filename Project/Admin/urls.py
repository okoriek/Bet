from django.urls import path
from Admin import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'Admin'

urlpatterns = [
    path('adminstrator/', LoginView.as_view(template_name = 'Admin/stafflogin.html'), name='staff'),
    path('logout/', LogoutView.as_view(), name='stafflogout'),
    path('dashboard/', views.CustomAdmin, name='staff_dashboard'),
    path('users_details', views.Userfilter, name='userdetails'),
    path('paystack_details', views.Paystackfilter, name='paystackdetails'),
    path('flutterwave_details', views.Flutterwavefilter, name='flutterwavedetails'),
    path('gameround', views.RandomGamefilter, name='gameround'),
    
]