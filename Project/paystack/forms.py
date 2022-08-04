from django import forms
from . models import Paystack

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Paystack
        fields = ('amount','email')