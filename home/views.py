from django.shortcuts import render, redirect
from signup.models import Signup
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def home(request, msg=""):
    if not request.session.get('user'):
        if request.method == "POST":
            user = request.POST.get('email')
            pwd = request.POST.get('password')
            s = Signup.objects.filter(email=user, password=pwd)
            if s.exists():
                obj = Signup.objects.get(email=user)
                if obj.active:
                    request.session['user'] = user
                    return redirect('profile')
                else:
                    return HttpResponse('Please confirm your email address to complete the registration')
            else:
                messages.error(request, 'Invalid Login Credentials.')
                return redirect('home')
        return render(request, 'home.html')
    else:
        return redirect('profile')


def home2(request, user=""):
    msg = {'msg': user}
    return render(request, 'home2.html', msg)
