from ast import arg
import re
from django.shortcuts import redirect, render
from .models import *
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
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils import timezone
from paystack.models import Userhistory
from .form import FileterForm
from django.contrib.auth.decorators import login_required
from paystack.paystack import BankList, VerifyAccount, InitiatingTransfer, MakePayment



def Loginsuccess(request):
    if request.user.is_staff:
        return redirect('Admin:staff_dashboard')
    else:
        return redirect('/')
def Logoutsuccess(request):
    if request.user.is_staff:
        return redirect('Admin:staff')
    else:
        return redirect('/')

def Home(request):
    return render(request, 'website/home.html')


def EmailVerification(request, uidb64, token):
    try:
        uid =  force_str(urlsafe_base64_decode(uidb64))
        user = Custom.objects.get(pk=uid)
        print(user)
    except(TypeError,ValueError, OverflowError, Custom.DoesNotExist):
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
        referred = Custom.objects.get(code=referal_code)
    except:
        pass
    if request.method == 'POST':
        forms = RegisterationForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            try:
                user.recommended_by = referred.email
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

@login_required(login_url='/login')
def ChangePassword(request):
    profile = Custom.objects.filter(recommended_by = request.user.username)
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

@login_required(login_url='/login')
def Dashboard(request):
    if request.user.is_staff:
        return redirect('Admin:staff_dashboard')
    user = Commission.objects.filter(user = str(request.user.email)).order_by('date_created')[:10]
    history = Userhistory.objects.filter(email=str(request.user.email)).order_by('date_created')[:10]
    arg = {'history':history, 'commission':user}
    return render(request, 'website/dashboard.html', arg)

@login_required(login_url='/login')    
@csrf_exempt
def FilterHistory(request):
    current_time = datetime.date.today()
    print(current_time)
    history =  Userhistory.objects.all().filter(email= request.user.email)
    filter = FileterForm(request.GET, queryset=history)
    history = filter.qs
    args = {'filter': filter, 'history':history}
    return render(request , 'website/transaction.html', args)


def Affilate(request):
    return render(request, 'website/affliate.html')


def Help(request):
    
    return render(request, 'website/contact.html')



def ContactUs(request):
    name = request.POST['name']
    phone_number = request.POST['phone']
    new_call =  CallRequest.objects.create(name = name, mobile_number = phone_number)
    new_call.save()
    return JsonResponse('Call request intiated succesfully', safe=False)

def GetBalance(request):
    user =  request.user
    profile =  Custom.objects.get(email = user)
    bal = profile.balance
    return JsonResponse({'balance': bal})
    
@login_required(login_url='/login')    
def RandomTen(request):
    
    return render(request, 'website/randomten.html')

def Lottery(request):
    return render(request, 'website/lottery.html')

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

@login_required(login_url='/login')   
@csrf_exempt
def RecieveNumbers(request):
    email =  request.user
    selectednum = request.POST.getlist('list[]')
    wk =  request.POST['week']
    amount = request.POST['amount']
    gaming =  GameRound.objects.get(week=int(wk))
    if request.POST:
        new = Game.objects.create(user = email, selectednumber=selectednum, week=gaming, amount=int(amount) )
        new.save()
        user = Custom.objects.get(email = email)
        user.balance -= int(amount)
        user.save()
    return HttpResponse('submitted successfully')

@login_required(login_url='/login')
def Payment(request):
    
    return render(request, 'website/deposit.html')


@csrf_exempt
def CreateNewRound(request):
    current_week = request.POST['week']
    updates = GameRound.objects.get(week = int(current_week))
    updates.save()
    gaming =  Game.objects.filter(week = updates)
    for val in gaming:
        val.save()
    return JsonResponse({'result':current_week})

@login_required(login_url='/login')
def Roundomhistory(request):
    history = Game.objects.all().filter(user = request.user).order_by('date_created')
    args = {'history': history}
    return render(request, 'website/gamehistory.html', args)

@login_required(login_url='/login')
def ResultHistory(request):
    history =  GameRound.objects.filter(ended = True).order_by('time_generated')
    args = {'history':history}
    return render(request, 'website/result.html', args)

def Result(request):
    resultgenerated =  GameRound.objects.filter(ended=True).order_by('-time_generated')[:1]
    data = []
    for i in resultgenerated:
        item = {
            'week': i.week,
            'result': i.result
        }
        data.append(item)
    return JsonResponse({'data': data})

def Withdrawal(request):
    bank_list = BankList()
    values = []
    code = []
    ziplist = zip(values, code)
    for i in bank_list:
        bank_name = i['name']
        bank_code = i['code']
        values.append(bank_name)
        code.append(bank_code)

    args = {'ziplist':ziplist}
    return render(request, 'website/withdrawal.html', args)

@csrf_exempt
def ConfirmingWithdrawalDetails(request):
    amount = request.POST['amount']
    account = request.POST['accounts']
    bank_code = request.POST['bank_code']
    bank_name = request.POST['bank_name']

    name = VerifyAccount(account,bank_code)
    account_name = name['account_name']
    if request.method == 'POST':
        withdraw = WithdrawalPayment.objects.create(user=request.user,account_name= account_name, account_no = account, amount =amount, bank_code=bank_code, bank_name=bank_name)
        withdraw.save()
        return redirect('/confirmdetails')
    
    return JsonResponse('successful', safe=False)

def ConfirmDetail(request):
    user = request.user
    detail = WithdrawalPayment.objects.filter(user=user).order_by('-id')[0]
    args = {'detail':detail}
    return render(request, 'website/withdrawalconfirm.html',args)

@csrf_exempt
def InitiatePay(request):
    user = request.user
    detail = WithdrawalPayment.objects.filter(user=user).values().order_by('-id')[0]
    account_name = detail['account_name']
    account_no = detail['account_no']
    bank_code = detail['bank_code']
    amount = detail['amount']
    print(amount)
    initiate = InitiatingTransfer(account_name, account_no, bank_code)
    recipient_code = initiate['recipient_code']
    print(recipient_code)
    makepayment = MakePayment(amount, recipient_code)
    print(makepayment)
    reference = makepayment['reference']
    status = recipient_code['status']
    transfer = WithdrawalPayment.objects.filter(id = detail['id']).update(reference = reference, status=status )
    return redirect('/')


# Views for lottery includes result generating e.t.c 
@login_required(login_url='/login')
def Lottery(request):
    return render(request, 'website/lottery.html')

def GetLotteryNumber(request):
    number =  NumberedValue.objects.all()
    round = LotteryRound.objects.filter(ended=False)[:1]
    time = []
    data = []
    for i in round:
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
def LotteryRecieveNumbers(request):
    email =  request.user
    selectednum = request.POST.getlist('list[]')
    wk =  request.POST['week']
    amount = 500
    gaming =  LotteryRound.objects.get(week=int(wk))
    if request.POST:
        new = Ticket.objects.create(user = email, selectednumber=selectednum, week=gaming, amount=amount)
        new.save()
        user = Custom.objects.get(email = email)
        user.balance -= amount
        user.save()
    return HttpResponse('submitted successfully')

@csrf_exempt
def LotteryVerify(request):
    current_week = request.POST['week']
    updates = LotteryRound.objects.get(week = int(current_week))
    updates.save()
    gaming =  Ticket.objects.filter(week = updates)
    for val in gaming:
        val.save()
    return JsonResponse({'result':current_week})

def LotteryResult(request):
    try:
        resultgenerated =  LotteryRound.objects.filter(ended=True).order_by('-time_generated')[:1]
        data = []
        for i in resultgenerated:
            item = {
                'week': i.week,
                'result': i.result
            }
            data.append(item)
        return JsonResponse({'data': data})
    except:
        pass


@login_required(login_url='/login')
def Lotteryhistory(request):
    history = Ticket.objects.all().filter(user = request.user).order_by('date_created')
    args = {'history': history}
    print(args)
    return render(request, 'website/ticket.html', args)
    
@login_required(login_url='/login')
def LotteryResultHistory(request):
    history =  LotteryRound.objects.filter(ended = True).order_by('time_generated')
    args = {'history':history}
    return render(request, 'website/lotteryresulthistory.html', args)






