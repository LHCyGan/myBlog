from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = [
        'username', 'email', 'name', 'introduce',
        'company', 'profession', 'address', 'telephone',
        'wx', 'qq', 'wb', 'photo'
    ]
    # 在修改界面添加‘mobile', 'qq', 'weChat'的输入框
    # 获取fielsets --> list
    fieldsets = list(UserAdmin.fieldsets)  # 可修改的
    # 重写 UserAdmin的fieldsets,添加模型字段录入
    fieldsets[1] = (_('Personal info'),
                    {
                        'fields': ('name', 'introduce', 'email',
        'company', 'profession', 'address', 'telephone',
        'wx', 'qq', 'wb', 'photo')
                    })

    # 根据当前用户名设置数据访问权限
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(id=request.user.id)

