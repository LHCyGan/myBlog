# -*- encoding:utf-8 -*-
# author: liuheng
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/<int:page>.html', album, name='album')
]
