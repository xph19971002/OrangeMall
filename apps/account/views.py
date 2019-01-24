
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate ,logout, login
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from apps.main.models import User


def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render(request,'login.html',{'next':next})
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            next = request.POST.get('next')
            # 判断密码和账号输入是否为空
            if username and password:
                # 验证用户名和密码是否存在
                user = authenticate(username=username,password=password)
                if user:
                    # 如果用户名与密码都正确，表示登录成功，记住登录状态
                    login(request,user)
                    # 如果是验证登录就跳转登录界面，如果是直接登录的就跳转首页
                    next = next if next else '/'
                    return redirect(next)
                else:
                    return render(request,'login.html',{'msg':'用户名或密码有误'})
            else:
                return render(request,'login.html',{'msg':'密码或账号不能为空'})
        except Exception as e:
            return render(request,'login.html',{'msg':'登录失败'})
    else:
        return render(request,'login.html',{'msg':'无效请求方式'})



def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            pwdRepeat = request.POST.get('pwdRepeat')
            # 判断输入用户名、密码.....输入是否为空
            if username and password and phone and email and pwdRepeat:
                #注册
                user = User.objects.filter(Q(username=username) | Q(phone=phone) | Q(email=email))
                if user.exists():
                    return render(request,'register.html',{'msg':'用户名、手机号或邮箱已存在！'})
                else:
                    # 保存用户操作
                    user = User.objects.create_user(username=username,password=password,phone=phone,email=email)
                    if user:
                        # 如果注册成功，直接记住用户登录状态，跳转登录界面
                        login(request,user)
                        # 反向解析
                        url=reverse('account:login_view')
                        return redirect(url)
                    else:
                        return render(request,'register.html',{'msg':'注册失败'})
            else:
                return render(request, 'register.html', {'msg': '输入信息不能为空'})
        except Exception as e:
           return render(request,'register.html',{'msg':'注册失败'})
    else:
        return render(request,'404.html')



def logout_view(request):
    logout(request)
    return redirect('/')

#验证用户是否登录
@login_required(login_url='/account/login/')
def update(request):
    user = request.user
    return redirect('/')

def detall(request):
    pass