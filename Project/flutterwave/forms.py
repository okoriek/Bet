from django import forms
from . models import FlutterWave


class PaymentForm(forms.ModelForm):
    class Meta:
        model = FlutterWave
        fields = ('amount','email')