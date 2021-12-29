from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime

# 引入内置信号
from django.db.models.signals import post_save

# 引入信号接收器的装饰器
from django.dispatch import receiver


# 用户扩展信息
class Profile(models.Model):
    # 与 User 模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # 学号
    number = models.CharField(max_length=10, blank=True)
    # 个人简介
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return "user {}".format(self.user.username)


# 信号接收函数，每当新建 User 实例时自动调用
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 信号接收函数，每当更新 User 实例时自动调用
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(
        verbose_name=u"验证码类型",
        max_length=10,
        choices=(("register", u"注册"), ("forget", u"找回密码")),
    )
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.date)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0}({1})".format(self.code, self.email)
