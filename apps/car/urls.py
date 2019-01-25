# -*- coding：utf-8 -*-
__author__ = 'madl'
__date__ = '2019/1/24 0024 下午 12:09'

from django.conf.urls import url
from apps.car import views



urlpatterns = [
    url('list/', views.car_list,name='car_list'),
]