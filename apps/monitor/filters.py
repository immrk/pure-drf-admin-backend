from django_filters import rest_framework as filters
from .models import LoginLog, OperationLog

class LoginLogFilter(filters.FilterSet):
    """登录日志筛选器"""

    username = filters.CharFilter(field_name="username", lookup_expr="icontains")  # 为 username 字段设置模糊查询 (icontains)
    status = filters.CharFilter(lookup_expr="exact")  # 保持 status 精确匹配

    class Meta:
        model = LoginLog
        fields = ["username", "status"]


class OperationLogFilter(filters.FilterSet):
    """操作日志筛选器"""

    request_modular = filters.CharFilter(field_name="request_modular", lookup_expr="icontains")  # 为 request_modular 字段设置模糊查询 (icontains)
    status = filters.CharFilter(lookup_expr="exact")  # 保持 status 精确匹配

    class Meta:
        model = OperationLog
        fields = ["request_modular", "status"]