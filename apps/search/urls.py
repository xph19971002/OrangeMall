# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.search import views

urlpatterns = [
    url('^$',views.search,name='search'),
    url('result/',views.search_result,name='search_result'),
]
