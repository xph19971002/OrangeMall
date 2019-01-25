# -*- coding：utf-8 -*-
__author__ = 'madl'
__date__ = '2019/1/25 0025 上午 11:39'

from django.conf.urls import url
from apps.order import views


urlpatterns = [
    url('form/',views.confirm1),
]