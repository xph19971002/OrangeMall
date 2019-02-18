# -*- coding :utf-8 -*-
__author__ = 'peiming'
__date__ = '2019/2/18 0018 10:54'
from django.conf.urls import url

from apps.person import views

urlpatterns = [
    url('index/',views.information,name='index'),
    url('information/',views.information,name='information'),
    url('address/',views.information,name='address'),

]