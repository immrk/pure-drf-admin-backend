from .serializers import RoleSerializer, MenuSerializer, MenuMetaSerializer, DeptInfoSerializer, RouteSerializer
from .models import Role, Menu, MenuMeta, DeptInfo
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.viewset import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoleFilter, MenuFilter, DeptFilter
from rest_framework.views import APIView
from utils.response import CustomResponse


class RoleViewSet(CustomModelViewSet):
    """角色表视图集"""

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoleFilter


class MenuViewSet(CustomModelViewSet):
    """菜单/权限视图集"""

    queryset = Menu.objects.all().order_by("meta__rank")
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuFilter


class MenuMetaViewSet(CustomModelViewSet):
    """菜单meta视图集"""

    queryset = MenuMeta.objects.all()
    serializer_class = MenuMetaSerializer


class DeptInfoViewSet(CustomModelViewSet):
    """部门信息视图集"""

    queryset = DeptInfo.objects.all()
    serializer_class = DeptInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DeptFilter


class AsyncRoutesView(APIView):
    """动态路由视图"""

    permission_classes = [IsAuthenticated]  # 仅保留登录用户访问权限限制；去除其余默认权限限制

    def get(self, request):
        user = request.user
        roles = user.role.all()
        # 根据用户角色获取所有关联的菜单，避免重复通过 distinct 去重
        menus = Menu.objects.filter(role__in=roles, menu_type=Menu.MenuChoices.MENU, status=True).distinct().order_by("meta__rank")

        # 获取用户关联的所有权限，并按照 parent_id 进行分组
        permissions = Menu.objects.filter(role__in=roles, menu_type=Menu.MenuChoices.PERMISSION, status=True).distinct()
        # 将权限根据 parent_id 进行分组
        permission_dict = {}
        for perm in permissions:
            parent_id = perm.parent_id
            if parent_id not in permission_dict:
                permission_dict[parent_id] = []
            permission_dict[parent_id].append(perm.code)

        serializer = RouteSerializer(menus, many=True, context={"permission_dict": permission_dict})
        # 返回 JSON 响应
        return CustomResponse(success=True, data=serializer.data, msg="成功获取动态路由")
