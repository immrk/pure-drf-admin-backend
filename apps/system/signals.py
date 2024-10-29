from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.conf import settings
from .models import Menu

def update_permissions_cache():
    """更新 Redis 中的权限数据"""
    if settings.USE_REDIS:
        print("更新 Redis 中的权限数据")
        permissions = Menu.objects.filter(menu_type=Menu.MenuChoices.PERMISSION, status=True).values_list("code", flat=True)
        permissions = list(permissions)
        cache.set("all_permissions", permissions, timeout=settings.CACHES_TTL)

@receiver(post_save, sender=Menu)
def menu_saved(sender, instance, **kwargs):
    # 当 Menu 表有数据创建或更新时，更新 Redis 缓存
    update_permissions_cache()

@receiver(post_delete, sender=Menu)
def menu_deleted(sender, instance, **kwargs):
    # 当 Menu 表有数据删除时，更新 Redis 缓存
    update_permissions_cache()