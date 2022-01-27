# -*- encoding:utf-8 -*-
# author: liuheng
from django.urls import path
from .views import *


urlpatterns = [
    # 用户注册
    path('register.html', register, name='register'),
    path('login.html', userLogin, name='userLogin'),
    path('about/<int:id>.html', about, name='about')
]