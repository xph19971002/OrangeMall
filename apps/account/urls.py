# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url('login_view/', views.login_view,name='login_view'),
    url('register',views.register,name='register'),
    url('udate/',views.update),
    url('logout/',views.logout_view),
]
