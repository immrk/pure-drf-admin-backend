# users/signals.py

from django.db.models.signals import pre_delete
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import User
from django.conf import settings
from django.core.cache import cache


@receiver(pre_delete, sender=User)
def delete_user_role_relationship(sender, instance, **kwargs):
    # 清除与被删除用户相关的所有角色关联
    instance.role.clear()

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # 判断USE_REDIS
    if settings.USE_REDIS:
        # 用户登录成功后的处理
        print(f"{user.username}登录成功！")
        # 获取用户权限并存入缓存
        permissions = user.get_all_permissions()
        cache.set(f"user_permissions_{user.id}", permissions, timeout=settings.CACHES_TTL)
        