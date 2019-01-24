from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from apps.main.models import User


def login(request):
    s = 1
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    del request.session['username']
    return redirect('/')
