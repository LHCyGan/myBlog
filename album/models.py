from django.db import models
from account.models import MyUser
# Create your models here.
class AlbumInfo(models.Model):
    """图片墙"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')  # 与User 是 一对多关系
    title = models.CharField('标题', max_length=50, blank=True)
    introduce = models.CharField('描述', max_length=200, blank=True)
    photo = models.ImageField('图片', blank=True, upload_to='images/album/')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '图片墙管理'
        verbose_name_plural = verbose_name
