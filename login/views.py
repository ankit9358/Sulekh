from django.shortcuts import render, redirect
from signup.models import Signup
from django.http import HttpResponse


# Create your views here.
def login(request):
    if not request.session.get('user'):
        if request.method == "POST":
            user = request.POST.get('email')
            pwd = request.POST.get('password')
            s = Signup.objects.filter(email=user, password=pwd)

            if s.exists():
                request.session['user'] = user
                return redirect('profile')
            else:
                msg = 'Invalid Username/Password'
                cont = {'message': msg}
                return redirect('home')

        return redirect('home')
    else:
        return redirect('profile')


def logout(request):
    try:
        del request.session['user']
        return redirect('home')
    except:
        return HttpResponse("Session Timeout")
