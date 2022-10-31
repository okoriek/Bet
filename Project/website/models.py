import datetime
from datetime import time
from multiprocessing.reduction import duplicate
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from . utils import RoundResult
import random


class MyUserManager(BaseUserManager):
    def create_user(self,email, first_name,last_name,username,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have username')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,email,last_name,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name = last_name,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Custom(AbstractBaseUser):
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    username     = models.CharField(max_length=100, unique=True)
    email         = models.EmailField(max_length=100, unique=True)
    phone_number  = models.CharField(max_length=100)
    code = models.CharField(max_length=8, blank=True, unique=True, null=True,default=get_random_string(length=8))
    recommended_by = models.CharField(blank=True, null=True, max_length=300)
    balance = models.IntegerField(default=0)
    
    date_joined   = models.DateTimeField(auto_now_add=True) 
    last_login    = models.DateTimeField(auto_now_add=True)   
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name',]

    objects = MyUserManager()


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
class Result(models.Model):
    round = models.CharField(max_length=10000000)
    outcome =  models.CharField(max_length=50, blank=True)
    date_generated =  models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.outcome
        
class Duration(models.Model):
    time = models.IntegerField(default=10)

    def __str__(self):
       return str(self.time)



class NumberedValue(models.Model):
    option_value = models.IntegerField(verbose_name='number')

    def __str__(self):
        return str(self.option_value)

class GameRound(models.Model):
    week =  models.IntegerField(blank=True, null=True)
    result = ArrayField(models.CharField(max_length=2), blank=True, null=True)
    returns = models.IntegerField(default= 0, blank=True, null=True)
    players = models.IntegerField(default=0, blank=True, null=True)
    time_generated = models.DateTimeField(default=timezone.now)
    time_ending = models.DateTimeField(blank=True, null=True)
    ended =  models.BooleanField(default=False)

    class Meta:
        ordering = ('time_generated',)

    def __str__(self):
        return str(self.week)


    def save(self, *args, **kwargs):
        self.time_ending = self.time_generated + timezone.timedelta(minutes=3)
        if self.time_ending > timezone.now():
            self.ended = False
        else:
            self.ended =  True
        if self.ended == True:
            self.result = [random.randrange(1,20,1)for i in range(8)]
        super().save(*args, **kwargs)



class Game(models.Model):
    STATUS = (
        ('won', 'WON'),
        ('pending', 'PENDING'),
        ('loss', 'LOSS')
    )
    week = models.ForeignKey(GameRound, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Custom, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, blank=True, null=True)
    generatedresult = ArrayField(models.CharField(max_length=2),blank=True, null=True)
    winning =  models.IntegerField(blank=True, null=True)
    selectednumber =ArrayField(models.CharField(max_length= 10),blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.generatedresult = self.week.result
        try:
            nonduplicategenerated = []
            nonduplicateselected = []
            duplicategenerated = []
            duplicateselected = []
            confirmed = []
            if self.generatedresult:
                if not confirmed:
                    self.status = 'loss'

            for result in self.generatedresult:
                if result not in nonduplicategenerated:
                    nonduplicategenerated.append(result)
                else:
                    duplicategenerated.append(result)

            for selected in self.selectednumber:
                if selected not in nonduplicateselected:
                    nonduplicateselected.append(selected)
                else:
                    duplicateselected.append(selected)
            for selectvalue in nonduplicateselected:
                try:
                    for dupvalue in duplicateselected:
                        if dupvalue in duplicategenerated:
                            confirmed.append(dupvalue)
                except:
                    pass
                if selectvalue in nonduplicategenerated:
                    confirmed.append(selectvalue)
                    if len(confirmed) == 3:
                        self.winning = int(self.amount * 3)
                        self.status = 'won'
                    elif len(confirmed) == 4:
                        self.winning = int(self.amount * 4)
                        self.status = 'won'
                    elif len(confirmed) == 4:
                        self.winning = int(self.amount * 10)
                        self.status = 'won'
                    else:
                        self.status ='loss'
        except:
            pass
        super().save(*args, **kwargs)
         
class WithdrawalPayment(models.Model):
    STATUS = (
        ('pending', 'PENDING'),
        ('conpleted', 'COMPLETED')
    )
    user  =  models.ForeignKey(Custom, on_delete=models.CASCADE, blank=True, null=True)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    bank_code = models.CharField(max_length=50, blank=True, null=True)
    bank_name =  models.CharField(max_length=50, blank=True, null=True)
    account_no = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, choices=STATUS)
    

    def __str__(self):
        return f"{self.user} {self.amount}"


    




    


