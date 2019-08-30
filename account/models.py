from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)  #注意外键和引用需要最佳删除一致性的作用 此处类似引用
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)  #self表示类本身 实例名 user表示类下的一个表 username表示该表下面的一个字段