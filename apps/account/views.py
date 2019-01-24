import re

from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate ,logout, login
from django.db.models import Q
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from apps.main.models import User

#登录
def login_view(request):
    if request.method =='GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        # 进行数据的校验
        if not all([username, password]):
            # 数据不完整
            return render(request, 'register.html', {'msg': '数据不完整 用户密码不能为空'})

        # 验证用户名首字母大写,并且长度为6
        if re.match(r'[A-Z]{1}[a-zA-Z0-9]{7,16}$', username) and len(password) >= 6:
            users = User.objects.filter(username=username)
            # 判断用户密码是否存在
            if users.exists():
                user = users.first()
                if user.verify_paypasswd(password):
                        # 登录成功 跳转到首页
                    request.session['username'] = user.username
                    return redirect('/')
                else:
                    return render(request, 'login.html', {'msg': '密码错误'})
            else:
                return render(request, 'login.html', {'msg': '用户名不存在'})
        else:
            return render(request, 'login.html', {'msg': '账号密码不符合规范'})






#注册
def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            pwdRepeat = request.POST.get('pwdRepeat')

            # 进行数据的校验
            if not all([username, phone, email, password, pwdRepeat]):
                # 数据不完整
                return render(request, 'register.html', {'msg': '内容不能为空'})
            #判断两次密码是否一致
            if not password == pwdRepeat:
                return render(request,'register.html',{'msg':'两次密码不一致'})
            #校验用户名格式是否正确
            if  not re.match(r'[a-zA-Z0-9]{7,16}$', username) and len(password) >= 6:
                return render(request,'register.html',{'msg':'用户名由至少6位0-9或a-zA-Z组成'})
            #验证电话号码
            if not re.compile(r'(^1(3[\d])|(47|45)|(5[^3|4])|(66)|(7[013678])|(8[\d])|(9[89]))\d{8}$',phone):
                return render(request, 'register.html', {'msg': '电话号码格式不对'})
            # 校验邮箱
            if not re.match(r"^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
                return render(request, 'register.html', {'msg': '邮箱格式不正确'})

            #判断用户信息是否已被注册过
            # if username and password and phone:
            #     # 注册
            #     user = User.objects.filter(Q(username=username) | Q(phone=phone))
            #     if user.exists():
            #         print('用户名或者手机已经被注册')
            #     else:
            #         # 保存用户的操作
            #         user = User.objects.create_user(username=username, password=password, phone=phone, email=email)
            #         if user:
            #
            #              #用户注册成功，跳转首页
            #              # login(request,user)
            #              # return redirect('/')
            #              #跳转到登录页面
            #              return redirect('account:login')
            #         else:
            #             pass
            #             #注册失败
            # 进行业务处理 ，进行用户注册
            user = User.objects.create_user(username,email,phone,password)
            #返回，跳转首页
            return redirect(reverse('/'))

        except Exception as e:
            return render(request,'404.html')


def logout_view(request):
    # del request.session['username']
    logout(request)
    return redirect('/')

#验证用户是否登录
@login_required(login_url='/account/login/')
def update(request):
    user = request.user
    return redirect('/')

def detall(request):
    pass