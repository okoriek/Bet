import django
from django.shortcuts import redirect, render
from .models import User
from django.http import HttpResponse
from . form import RegisterationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import TokenGenerator
from django.contrib import messages


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

def Dashboard(request):
    user = request.user
    profile = User.objects.filter(recommended_by = user.username)
    context = {'profile':profile}
    return render(request, 'website/dashboard.html', context)