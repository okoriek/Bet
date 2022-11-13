from django.db import models
from django.utils import timezone
import secrets
from django.conf import settings
from  website.models import *
from .flutterwave import FlutterWavePayment


class FlutterWave(models.Model):
    amount = models.CharField(max_length=1000000)
    email =  models.EmailField(max_length=3000, blank=True, null=True)
    reference = models.CharField(max_length=200, unique=True)
    generated = models.DateTimeField(default=timezone.now)
    verified =  models.BooleanField(default=False)

    class Meta:
        ordering = ('-generated',)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        while not self.reference:
            ref = secrets.token_urlsafe(50)
            same_ref = FlutterWave.objects.filter(reference = ref)
            if not same_ref:
                self.reference = ref
        super().save(*args, **kwargs)

    def confirm_payment(self):
        flutterwave = FlutterWavePayment()
        status, result = flutterwave.confirm_payment(self.reference, self.amount)
        if status:
            if result[0]['amount'] == int(self.amount):
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
