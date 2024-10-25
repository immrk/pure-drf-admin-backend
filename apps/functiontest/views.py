from django.shortcuts import render
from utils.response import CustomResponse
from rest_framework.views import APIView
from utils.decorators import require_permission
from utils.permissions import ActiveAndPermission
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class PermissionView(APIView):
    """
    用于后端装饰器方法权限测试, 需要手动添加权限装饰器并传入权限代码
    """

    permission_classes = [AllowAny]

    @require_permission("/api/test/permission/:read")
    def get(self, request, *args, **kwargs):
        return CustomResponse(success=True, data=None, msg="权限测试成功")


class PermissionView2(APIView):
    """
    用于改写权限鉴别方法权限测试, 根据请求的路径自动匹配权限代码进行权限鉴别
    """

    def get(self, request, *args, **kwargs):
        return CustomResponse(success=True, data=None, msg="权限测试成功")
