from rest_framework import serializers
from website.models import WithdrawalPayment
from paystack.models import Paystack

class SerializeModel(serializers.ModelSerializer):
    class Meta:
        model = Paystack
        fields = '__all__'