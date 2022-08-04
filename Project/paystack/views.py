from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from  paystack.models import Paystack
from .forms import PaymentForm
from django.conf import settings
from django.contrib import messages
from .models import Userhistory


def InitializeDeposit(request):
    value = {
        'email': request.user
    }
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment=payment_form.save()
            return render(request, 'payment/confirm.html', {'payment':payment, 'PUBLIC_KEY':settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form =  PaymentForm(initial=value)
    args = {'forms':payment_form}
    return render(request, 'payment/deposit.html', args)

def verify_payment(request, reference):
    payment = get_object_or_404(Paystack, reference=reference)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, 'Successful Deposit')
    else:
        messages.error(request, 'Incomplete Deposit Transaction')
    return redirect('/')
        
    
    
