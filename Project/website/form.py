from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username', 'phone_number')