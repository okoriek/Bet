from click import confirm
from . models import Game, GameRound
from django.contrib.auth.models import User
from paystack.models import Paystack
from flutterwave.models import FlutterWave
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from paystack.models import Userhistory


@receiver(post_save, sender = Paystack)
def HistoryPaystack(sender, created, instance, **kwargs):
    if created:
        history = Userhistory.objects.create(paystack =instance , email= instance.email ,amount = instance.amount, date_created = instance.generated, transaction = 'Deposit')

@receiver(post_save, sender = Paystack)    
def UpdateHistoryPaystack(sender,  instance, created, **kwargs):
    if created == False:
        history  = Userhistory.objects.filter(paystack=instance).update(confirm = instance.verified)
        instance.userhistory.save()
        print('History updated succesfully')


@receiver(post_save, sender = FlutterWave)
def HistoryFlutterwave(sender, created, instance, **kwargs):
    if created:
        history = Userhistory.objects.create(flutterwave =instance , email= instance.email ,amount = instance.amount, date_created = instance.generated, transaction = 'Deposit')

@receiver(post_save, sender = FlutterWave)    
def UpdateHistoryFlutterwave(sender,  instance, created, **kwargs):
    if created == False:
        history  = Userhistory.objects.filter(flutterwave=instance).update(confirm = instance.verified)
        instance.userhistory.save()
        print('History updated succesfully')


        
    
    
    
               


        
        


        
        