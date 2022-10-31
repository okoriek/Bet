from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from .models import FlutterWave
from .forms import PaymentForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def Deposit(request):
    value = {
        'email': request.user
    }
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment=payment_form.save()
            return render(request, 'flutterwave/confirm.html', {'payment':payment, 'PUBLIC_KEY':settings.FLUTTERWAVE_PUBLIC_KEY})
    else:
        payment_form =  PaymentForm(initial=value)
    args = {'forms':payment_form}
    return render(request, 'flutterwave/payment.html', args)

@login_required(login_url='/login')
def confirm_payment(request, reference):
    payment = get_object_or_404(FlutterWave, reference = reference)
    verified = payment.confirm_payment()
    if verified:
        messages.success(request, 'Successful Deposit')
    else:
        messages.error(request, 'Incomplete Deposit Transaction')
    return redirect('/')