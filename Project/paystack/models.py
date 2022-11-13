from django.db import models
from django.utils import timezone
import secrets
from .paystack import PayStackPayment
from  website.models import *
from flutterwave.models import FlutterWave



class Paystack(models.Model):
    amount = models.CharField(max_length=1000000)
    email =  models.EmailField(max_length=3000, blank=True, null=True)
    reference = models.CharField(max_length=200)
    generated = models.DateTimeField(default=timezone.now)
    verified =  models.BooleanField(default=False)

    class Meta:
        ordering = ('-generated',)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        while not self.reference:
            ref = secrets.token_urlsafe(50)
            same_ref = Paystack.objects.filter(reference = ref)
            if not same_ref:
                self.reference = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return int(self.amount)*100

    def verify_payment(self):
        paystack = PayStackPayment()
        status, result = paystack.verify_payment(self.reference, self.amount)
        if status:
            if result['amount']/100 == int(self.amount):
                self.verified = True
            self.save()
        if self.verified:
            user = Custom.objects.get(email = self.email)
            user.balance += int(self.amount)
            try:
                amount = (int(self.amount) * 2) / 100
                ref_bonus =  Commission.objects.create(user = user.recommended_by, reward=amount, completed = self.verified)
                ref_bonus.save()
                referral = Custom.objects.get(email = user.recommended_by)
                referral.commissions += amount
                referral.save()
            except:
                pass
            user.save()
            return True
        return False

class Userhistory(models.Model):
    Status = (
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
    )
    paystack = models.OneToOneField(Paystack, on_delete=models.CASCADE, blank=True, null=True)
    flutterwave = models.OneToOneField(FlutterWave, on_delete=models.CASCADE, blank=True, null=True)
    email  = models.EmailField(max_length=40, blank=True, null=True)
    amount = models.CharField(max_length=30, blank=True, null=True)
    transaction = models.CharField(max_length=20,blank=True, null=True, choices=Status)
    confirm =  models.BooleanField(default=False)
    date_created = models.DateField()

    class Meta:
        ordering = ('-date_created',)
        verbose_name_plural = 'User Histories'


    def __str__(self):
        return f"{self.email}  {self.transaction}: {self.amount}"
    
    
        
