# decorators.py
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied


# 用于自定义装饰器，实现权限验证(激活且拥有权限代码)
def require_permission(permission_code=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            # 判断用户是否激活
            if not request.user.is_active():
                raise PermissionDenied("用户未激活")
            # 若permission_code是一个字典, 则根据请求方法获取权限代码，并判断用户是否拥有权限代码
            if isinstance(permission_code, dict):
                method = request.method.lower()  # 获取请求方法
                perm_code = permission_code.get(method)
                # 判断用户是否拥有权限代码
                if perm_code and not request.user.has_perm(perm_code):
                    raise PermissionDenied("用户无权限")
            # 若permission_code是一个字符串, 则直接判断用户是否拥有权限代码
            elif isinstance(permission_code, str):
                # 判断用户是否拥有权限代码
                if permission_code and not request.user.has_perm(permission_code):
                    raise PermissionDenied("用户无权限")
            return func(self, request, *args, **kwargs)

        return wrapper

    return decorator
