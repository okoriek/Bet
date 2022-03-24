from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string

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



