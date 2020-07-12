from django.shortcuts import render,redirect
from signup.models import Signup

# Create your views here.


def profile(request, msg=""):
    if not request.session.get('user'):
        return redirect('home')

    user = request.session.get('user')
    obj = Signup.objects.get(email=user)
    cont = {'user': user, 'fields': obj, 'msg': msg}

    return render(request, 'basicUser.html', cont)
