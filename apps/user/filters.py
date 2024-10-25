# 过滤器代码文件
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from apps.system.models import DeptInfo

User = get_user_model()


class UserFilter(filters.FilterSet):
    """用户数据筛选器"""

    dept = filters.CharFilter(method="filter_by_dept")
    username = filters.CharFilter(field_name="username", lookup_expr="icontains")  # 为 name 字段设置模糊查询 (icontains)
    email = filters.CharFilter(field_name="email", lookup_expr="exact")
    status = filters.CharFilter(lookup_expr="exact")  # 保持 status 精确匹配

    class Meta:
        model = User
        fields = ["dept_id", "username", "email", "status"]

    def filter_by_dept(self, queryset, name, value):
        """筛选当前部门以及其所有子部门包括子部门的子部门的用户"""
        dept = DeptInfo.objects.get(id=value)
        dept_ids = dept.get_child_dept_ids()
        return queryset.filter(dept_id__in=dept_ids)
