# -*- encoding:utf-8 -*-
# author: liuheng
from django.contrib.admin.apps import AdminConfig

class MyAdminConfig(AdminConfig):
    """将自定义的MyAdminSite进行系统注册"""
    default_site = 'myblog.myadmin.MyAdminSite'