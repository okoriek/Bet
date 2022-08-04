from calendar import week
import email
from inspect import ArgSpec
from time import strptime
from turtle import update
from django.shortcuts import redirect, render
from .models import Duration, Game, GameRound, NumberedValue, Result, User
from django.http import HttpResponse, JsonResponse
from . form import RegisterationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import TokenGenerator
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils import timezone
from paystack.models import Userhistory
from .form import FileterForm




def Home(request):
    return render(request, 'website/home.html')

def EmailVerification(request, uidb64, token):
    try:
        uid =  force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError, OverflowError, User.DoesNotExist):
        user = None
        return HttpResponse(request, 'Your account could not be verified ')
    if user is not None and TokenGenerator.check_token(user, token):
        user.is_active =  True
        user.save()
        messages.success(request, 'Your Account as been verified')
        return redirect('/login')
    

def Register(request):
    try:
        referal_code = request.POST.get('refercode')
        referred = User.objects.get(code=referal_code)
    except:
        pass
    if request.method == 'POST':
        forms = RegisterationForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            try:
                user.recommended_by = referred.username
            except:
                pass
            user.save()
            website = get_current_site(request).domain
            email_subject = 'Email Verification'
            email_body =  render_to_string('website/activation.html',{
                'user':user,
                'domain':website,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': TokenGenerator.make_token(user)
            })
            email = EmailMessage(subject=email_subject, body=email_body,
                from_email=settings.EMAIL_HOST_USER, to=[user.email]
                )
            email.send()
            messages.success(request, 'A Verification Email has been sent to your Email please confirm')
            return redirect('/login')
    else:
        forms = RegisterationForm()
    args = {'forms':forms}
    return render(request, 'website/register.html', args)

def ChangePassword(request):
    profile = User.objects.filter(recommended_by = request.user.username)
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save
            messages.success(request, 'Password updated successfully.')
            return redirect('/login')
    else:
        form = PasswordChangeForm(request.user)
    args = {'form':form, 'profile':profile}
    return render(request, 'website/change_password.html', args)

def Dashboard(request):
    history = Userhistory.objects.all().filter(email=request.user.email).values()[:10]
    arg = {'history':history}
    return render(request, 'website/dashboard.html', arg)
    
@csrf_exempt
def FilterHistory(request):
    current_time = datetime.date.today()
    print(current_time)
    history =  Userhistory.objects.all().filter(email= request.user.email)
    filter = FileterForm(request.GET, queryset=history)
    history = filter.qs
    args = {'filter': filter, 'history':history}
    return render(request , 'website/transaction.html', args)
    


    
    

def RandomTen(request):
    number =  NumberedValue.objects.all()
    args = {'number': number}
    return render(request, 'website/randomten.html', args)

def GetNumbers(request):
    number =  NumberedValue.objects.all()
    duration  = GameRound.objects.filter(ended=False)[:4]
    time = []
    data = []
    for i in duration:
        item={
            'week':i.week,
            'created': i.time_generated,
            'expire': i.time_ending

        }
        time.append(item)
    for obj in number:
        item= {
            'value': obj.option_value
        }
        data.append(item)
    return JsonResponse({'data': data, 'time':time})
    
@csrf_exempt
def RecieveNumbers(request):
    email =  request.user
    selectednum = request.POST.getlist('list[]')
    wk =  request.POST['week']
    gaming =  GameRound.objects.get(week=int(wk))
    if request.POST:
        new = Game.objects.create(user = email, selectednumber=selectednum, week=gaming)
        new.save()
        user = User.objects.get(email = email)
        user.balance -= 500
        user.save()
    return HttpResponse('submitted successfully')

def Payment(request):
    
    return render(request, 'website/deposit.html')




