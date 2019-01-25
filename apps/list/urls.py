# -*- coding :utf-8 -*-
from django.conf.urls import url

from apps.list import views

__author__ = 'peiming'
__date__ = '2019/1/24 0024 20:33'

urlpatterns = [
    url(r'sort/', views.sort, name='sort'),
    url('^$',views.list,name='list'),
]