# 过滤器代码文件
from django_filters import rest_framework as filters
from .models import Role, Menu, DeptInfo


class RoleFilter(filters.FilterSet):
    """角色表筛选器"""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")  # 为 name 字段设置模糊查询 (icontains)
    status = filters.CharFilter(lookup_expr="exact")  # 保持 status 精确匹配

    class Meta:
        model = Role
        fields = ["name", "status"]


class MenuFilter(filters.FilterSet):
    """角色表筛选器"""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")  # 为 name 字段设置模糊查询 (icontains)
    status = filters.CharFilter(lookup_expr="exact")  # 保持 status 精确匹配

    class Meta:
        model = Menu
        fields = ["name", "status"]


class DeptFilter(filters.FilterSet):
    """部门信息筛选器"""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")  # 为 name 字段设置模糊查询 (icontains)
    status = filters.CharFilter(lookup_expr="exact")  # 保持 status 精确匹配

    class Meta:
        model = DeptInfo
        fields = ["name", "status"]
