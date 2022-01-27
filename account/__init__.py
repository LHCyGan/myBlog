from django.apps import AppConfig
import os

# 修改app在admin后台显示的名称
# default_app_config 的值来自apps.py的类名
default_app_config = 'account.IndexConfig'
# 获取当前app的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

# 重写IndexConfig
class IndexConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '用户管理'
