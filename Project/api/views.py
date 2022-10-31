from django.shortcuts import render
from paystack.models import Paystack
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .sterilizer import SerializeModel


@api_view(['POST'])
def GetDepositData(request):
    deposit = Paystack.objects.all()
    serializer = SerializeModel(deposit, many=True)
    return Response(serializer.data)