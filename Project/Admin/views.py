from .form import UserFilter,PaystackFilter, FlutterwaveFilter
from django.shortcuts import render,redirect
from website.models import Custom, GameRound
from paystack.models import Paystack
from flutterwave.models import FlutterWave


def CustomAdmin(request):
    if request.user.is_staff:
        paystack = Paystack.objects.all().filter(verified=True)
        flutter = FlutterWave.objects.all().filter(verified=True)
        user = Custom.objects.all().count()
        amount = 0
        for i in paystack:
            amount += int(i.amount)
        for x in flutter:
            amount += int(x.amount) 
        args = {'amount':amount, 'user':user}
        return render(request, 'Admin/dashboard.html', args)
    else:
        return redirect('/dashboard')

def Userfilter(request):
    if request.user.is_staff:
        user = Custom.objects.all()
        users = UserFilter(request.GET, queryset=user)
        user = users.qs
        args = {'user':user,'users':users}
        return render(request, 'Admin/user.html', args )
    else:
        return redirect('/dashboard')

def Paystackfilter(request):
    if request.user.is_staff:
        paystack =  Paystack.objects.all()
        paystackfilter = PaystackFilter(request.GET, queryset=paystack)
        paystack = paystackfilter.qs
        args = {'paystack':paystack,'paystackfilter':paystackfilter}
        return render(request, 'Admin/paystack.html', args )
    else:
        return redirect('/dashboard')

def Flutterwavefilter(request):
    if request.user.is_staff:
        flutterwave =  FlutterWave.objects.all()
        flutterwavefilter = FlutterwaveFilter(request.GET, queryset=flutterwave)
        flutterwave = flutterwavefilter.qs
        args = {'flutterwave':flutterwave,'flutterwavefilter':flutterwavefilter}
        return render(request, 'Admin/flutterwave.html', args )
    else:
        return redirect('/dashboard')

def RandomGamefilter(request):
    if request.user.is_staff:
        gameround =  GameRound.objects.all().order_by('-time_generated')[:7]
        args = {'gameround':gameround}
        return render(request, 'Admin/gameround.html', args )
    else:
        return redirect('/dashboard')
