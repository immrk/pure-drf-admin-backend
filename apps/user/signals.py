# users/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings
from django.core.cache import cache

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # 判断USE_REDIS
    if settings.USE_REDIS:
        # 用户登录成功后的处理
        print(f"{user.username}登录成功！")
        # 获取用户权限并存入缓存
        permissions = user.get_all_permissions()
        cache.set(f"user_permissions_{user.id}", permissions, timeout=settings.CACHES_TTL)
        