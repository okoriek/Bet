from time import time
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.utils import timezone

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


class User(AbstractBaseUser):
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
    outcome =  models.CharField(max_length=50, blank=True, null=True)
    date_generated =  models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.outcome
        
class Duration(models.Model):
    time = models.IntegerField(default=10)

    def __str__(self):
       return str(self.time)

class NumberedValue(models.Model):
    option_value = models.IntegerField(verbose_name='number')
    correct_value = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.option_value)



class Game(models.Model):
    STATUS = (
        ('won', 'WON'),
        ('pending', 'PENDING'),
        ('loss', 'LOSS')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.SET_NULL, blank=True, null=True )
    winning =  models.IntegerField(blank=True, null=True)
    option = models.ManyToManyField(NumberedValue, blank=True  )
    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user
    



