from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.core.cache import cache
from django.conf import settings
from apps.system.models import Menu
import re

# 用于自定义装饰器，实现权限验证(激活且拥有权限代码)
def require_permission(permission_code=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            # 判断用户是否激活
            if not request.user.is_active():
                raise PermissionDenied("用户未激活")

            # 检查是否使用缓存
            use_cache = getattr(settings, 'USE_REDIS', False)

            def check_menu_permissions(code):
                """检查是否存在权限代码"""
                permissions = cache.get("all_permissions")
                if not permissions:
                    permissions = Menu.objects.filter(
                        menu_type=Menu.MenuChoices.PERMISSION,
                        status=True
                    ).values_list("code", flat=True)
                    permissions = list(permissions)
                    cache.set("all_permissions", permissions, timeout=settings.CACHES_TTL)
                return code in permissions

            def check_user_permissions(code, user):
                """检查用户是否拥有权限代码"""
                permissions = cache.get(f"user_permissions_{user.id}")
                if not permissions:
                    permissions = user.get_all_permissions()
                    cache.set(f"user_permissions_{user.id}", permissions, timeout=settings.CACHES_TTL)
                return code in permissions

            # 若permission_code是一个字典, 则根据请求方法获取权限代码，并判断用户是否拥有权限代码
            if isinstance(permission_code, dict):
                method = request.method.lower()
                perm_code = permission_code.get(method)

                if perm_code:
                    if use_cache:
                        # 使用缓存进行权限判断
                        if not check_menu_permissions(perm_code):
                            return func(self, request, *args, **kwargs)  # 权限不存在则直接放行
                        if not check_user_permissions(perm_code, request.user):
                            raise PermissionDenied("用户无权限")
                    else:
                        # 不使用缓存，直接查询数据库
                        if not Menu.objects.filter(
                            code=perm_code, menu_type=Menu.MenuChoices.PERMISSION, status=True
                        ).exists():
                            return func(self, request, *args, **kwargs)
                        if not request.user.has_perm(perm_code):
                            raise PermissionDenied("用户无权限")

            # 若permission_code是一个字符串, 则直接判断用户是否拥有权限代码
            elif isinstance(permission_code, str):
                if permission_code:
                    if use_cache:
                        if not check_menu_permissions(permission_code):
                            return func(self, request, *args, **kwargs)
                        if not check_user_permissions(permission_code, request.user):
                            raise PermissionDenied("用户无权限")
                    else:
                        if not Menu.objects.filter(
                            code=permission_code, menu_type=Menu.MenuChoices.PERMISSION, status=True
                        ).exists():
                            return func(self, request, *args, **kwargs)
                        if not request.user.has_perm(permission_code):
                            raise PermissionDenied("用户无权限")

            return func(self, request, *args, **kwargs)

        return wrapper

    return decorator