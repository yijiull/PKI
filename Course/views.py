from django.shortcuts import render

# Create your views here.

from .models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .util import verify_password


def index(request):
    return render(request, 'index.html')


def login_verify(request):
    id = request.POST["userid"]
    password = request.POST["password"]
    print(id, password)
    user = get_object_or_404(User, u_id=id)
    if verify_password(user.u_pwdhash, password):
        return render(request, 'index.html', {'user': user})
    else:
        return render(request, 'index.html', {'user': user, 'error': '用户名或密码错误'})


def login(request):
    return render(request, 'login.html')
