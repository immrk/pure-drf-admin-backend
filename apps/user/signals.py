# users/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings
from django.core.cache import cache
from utils.request_util import save_login_log
from django.dispatch import Signal
from .models import User

# 定义登录失败信号
user_login_failed = Signal()

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    '''用户登录成功后的信号处理函数'''
    # 判断USE_REDIS
    if settings.USE_REDIS:
        # 获取用户权限并存入缓存
        permissions = user.get_all_permissions()
        cache.set(f"user_permissions_{user.id}", permissions, timeout=settings.CACHES_TTL)
    # 保存登录日志
    save_login_log(request, user.username, status=True)


@receiver(user_login_failed)
def user_login_failed_handler(sender, request, email, **kwargs):
    '''用户登录失败后的信号处理函数'''
    user = User.objects.filter(email=email).first()
    username = user.username if user else email
    # 保存登录日志
    save_login_log(request, username, status=False)