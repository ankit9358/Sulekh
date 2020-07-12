from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Signup_forms
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from Activation.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .models import Signup
from django.contrib import messages


def register(request):
    form = Signup_forms(request.POST or None)
    if form.is_valid():
        user = form.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        # user = form.cleaned_data['email']
        message = render_to_string('active_mail.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
            mail_subject, message, to=[user]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')
        # request.session['user'] = form.cleaned_data['email']
        # return redirect('profile')
        # return redirect('register')
    context = {'form': form}

    return render(request, 'register.html', context)


# Create your views here.

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Signup.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.active = True
        user.save()
        request.session['user'] = user.email
        # msg = "Your account is successfully verified! "
        messages.success(request, 'Your account is successfully verified!')
        return redirect('profile')
    else:
        return HttpResponse('Activation link is invalid!')
