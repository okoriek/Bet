from os import name
from django import views
from django.urls import path, reverse_lazy
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
   path('loginsuccess', views.Loginsuccess, name='loginsuccess'),
   path('logoutsuccess', views.Logoutsuccess, name='logoutsuccess'),
   path('register/', views.Register, name='register'),
   path('login/', LoginView.as_view(template_name = 'website/login.html', redirect_authenticated_user = True), name='login'),
   path('logout/', LogoutView.as_view(), name = 'logout'),
   path('verification/<uidb64>/<token>/', views.EmailVerification, name='verification'),
   path('change_password/', views.ChangePassword, name = 'changepassword'),
   path('dashboard/', views.Dashboard, name='dashboard'),
   path('getbalance/', views.GetBalance, name='balance'),
   path('affiliate/', views.Affilate, name='affiliate'),
   path('help/', views.Help, name='help'),
   path('contact/', views.ContactUs, name='contact'),
   


   

   #Lottery url
   path('lottery/', views.Lottery, name='lottery'),
   path('lotterygetnumbers/', views.GetLotteryNumber, name='lotterygame'),
   path('lotterydatasubmit/', views.LotteryRecieveNumbers, name = 'lotteryreceivenumbers'),
   path('lotteryverify/', views.LotteryVerify, name='lotteryverify'),
   path('lotteryresults/', views.LotteryResult, name='result'),
    path('ticket_history/', views.Lotteryhistory, name='tickethistory'),
   path('lottery_result_history/', views.LotteryResultHistory, name='lotteryresulthistory'),

   path('games/random10/', views.RandomTen, name='randomten'),
   path('datasubmit/', views.RecieveNumbers, name = 'receivenumbers'),
   path('getnumbers/', views.GetNumbers, name='numbers'),
   path('make_payment/', views.Payment, name='payment'),
   path('withdrawal/', views.Withdrawal, name='withdrawal'),
   path('confirmbankname/', views.ConfirmingWithdrawalDetails, name='bankname'),
   path('confirmdetails/', views.ConfirmDetail, name='confirmdetails'),
   path('initiatepayment/', views.InitiatePay, name='initiatepayment'),
   path('history/', views.FilterHistory, name='history'),
   path('create/', views.CreateNewRound, name='create'),
   path('results/', views.Result, name='result'),
   path('game_history/', views.Roundomhistory, name='gamehistory'),
   path('history_result/', views.ResultHistory, name='resulthistory'),
   
   
   
   path('password_reset/', PasswordResetView.as_view(template_name = 'password/passwordreset.html'), name='reset_password'),
   path('password_reset_done/', PasswordResetDoneView.as_view(template_name = 'password/passwordresetdone.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'password/passwordresetconfirm.html'), name='password_reset_confirm'),
   path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name = 'password/passwordresetcomplete.html'), name='password_reset_complete'),
]