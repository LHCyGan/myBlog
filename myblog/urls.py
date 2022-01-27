"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # Admin 后台系统
    path('admin/', admin.site.urls),
    # 用户注册和登录
    path('user/', include('account.urls')),
    # 博客文章
    path('', include('article.urls')),
    # 图片墙
    path('album/', include('album.urls')),
    # 留言版
    path('board/', include('interflow.urls')),
    # 媒体资源
    re_path('media/(?P<path>.*)', serve,
            {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # 设置编辑器的路由信息
    path('ckeditor/', include('ckeditor_uploader.urls'))
]
