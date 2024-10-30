from django.shortcuts import render
from .serializers import LoginLogSerializer, OperationLogSerializer
from .models import LoginLog, OperationLog
from utils.viewset import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import LoginLogFilter, OperationLogFilter
from utils.pagination import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination,
)
from rest_framework.views import APIView
from utils.response import CustomResponse

class LoginLogViewSet(CustomModelViewSet):
    """登录日志视图集"""

    queryset = LoginLog.objects.all().order_by("-id")
    serializer_class = LoginLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LoginLogFilter
    pagination_class = CustomPageNumberPagination

# 新增一个删除所有日志视图集
class DeleteAllLoginLogView(APIView):
    """删除所有日志视图"""

    def delete(self, request):
        LoginLog.objects.all().delete()
        return CustomResponse(success=True, msg="登录日志已清空")

class OperationLogViewSet(CustomModelViewSet):
    """操作日志视图集"""

    queryset = OperationLog.objects.all().order_by("-id")
    serializer_class = OperationLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OperationLogFilter
    pagination_class = CustomPageNumberPagination

# 新增一个删除所有日志视图集
class DeleteAllOperationView(APIView):
    """删除所有日志视图"""

    def delete(self, request):
        OperationLog.objects.all().delete()
        return CustomResponse(success=True, msg="删除所有日志成功")