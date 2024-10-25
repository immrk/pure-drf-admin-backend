from rest_framework import serializers
from .models import Role, Menu, MenuMeta, DeptInfo


class RoleSerializer(serializers.ModelSerializer):
    """角色表序列化器"""

    menu = serializers.PrimaryKeyRelatedField(many=True, queryset=Menu.objects.all(), required=False, default=list)
    parent = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Role
        fields = ["id", "name", "code", "status", "menu", "parent"]


class MenuMetaSerializer(serializers.ModelSerializer):
    """菜单meta序列化器"""

    extraIcon = serializers.CharField(source="r_svg_name", allow_null=True, required=False)
    showLink = serializers.BooleanField(source="is_show_menu")
    showParent = serializers.BooleanField(source="is_show_parent")
    keepAlive = serializers.BooleanField(source="is_keepalive")
    frameSrc = serializers.CharField(source="frame_url", allow_null=True, required=False)
    frameLoading = serializers.BooleanField(source="frame_loading", allow_null=True, required=False)
    hiddenTag = serializers.BooleanField(source="is_hidden_tag")
    fixedTag = serializers.BooleanField(source="fixed_tag")
    # 进离场动画数据自定义格式
    transition = serializers.SerializerMethodField()

    class Meta:
        model = MenuMeta
        fields = ["id", "title", "icon", "rank", "extraIcon", "showLink", "showParent", "keepAlive", "frameSrc", "frameLoading", "hiddenTag", "fixedTag", "transition"]

    def get_transition(self, obj):
        return {
            "enterTransition": obj.transition_enter,
            "leaveTransition": obj.transition_leave,
        }


class MenuSerializer(serializers.ModelSerializer):
    """菜单/权限序列化器"""

    parent = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all(), allow_null=True, required=False)
    meta = MenuMetaSerializer(required=False, allow_null=True)

    class Meta:
        model = Menu
        fields = ["id", "parent", "menu_type", "name", "code", "path", "component", "status", "meta", "method", "redirect"]

    def create(self, validated_data):
        """重写创建方法，创建menu数据时自动创建meta数据并创建关联关系"""
        # 从请求数据中提取 meta 数据
        meta_data = validated_data.pop("meta", None)
        # 创建 MenuMeta 实例
        if meta_data:
            menu_meta = MenuMeta.objects.create(**meta_data)
        else:
            menu_meta = MenuMeta.objects.create(**{})
        # 创建 Menu 实例并关联 MenuMeta
        menu = Menu.objects.create(meta=menu_meta, **validated_data)
        return menu

    def update(self, instance, validated_data):
        """重写更新方法，更新menu数据时自动更新meta数据"""
        # 从请求数据中提取 meta 数据
        meta_data = validated_data.pop("meta", None)

        # 如果meta数据存在，更新现有的MenuMeta实例
        if meta_data:
            if instance.meta:
                # 更新现有的meta实例
                for attr, value in meta_data.items():
                    setattr(instance.meta, attr, value)
                instance.meta.save()
            else:
                # 如果之前没有meta实例，创建一个新的
                instance.meta = MenuMeta.objects.create(**meta_data)

        # 如果meta数据不存在，但存在一个与之关联的MenuMeta实例，将其保留
        elif instance.meta:
            pass

        # 更新Menu实例的其他字段
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class DeptInfoSerializer(serializers.ModelSerializer):
    """部门信息序列化器"""

    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all(), required=False, default=list)
    parent = serializers.PrimaryKeyRelatedField(queryset=DeptInfo.objects.all(), allow_null=True, required=False)

    class Meta:
        model = DeptInfo
        fields = ["id", "name", "code", "rank", "type", "parent", "status", "roles", "parent"]


class RouteSerializer(serializers.ModelSerializer):
    meta = serializers.SerializerMethodField()  # 嵌套 MenuMeta 的序列化器
    parent = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all(), allow_null=True)

    class Meta:
        model = Menu
        fields = ["id", "name", "path", "menu_type", "component", "code", "meta", "parent", "redirect"]

    def get_meta(self, obj):
        # 获取权限字典，从上下文中提取
        permission_dict = self.context.get("permission_dict", {})
        # Serialize the meta field using MenuMetaSerializer
        meta_serializer = MenuMetaSerializer(obj.meta)
        # Filter out empty fields from the meta data
        meta_data = {key: value for key, value in meta_serializer.data.items() if value not in [None, "", [], {}]}

        # 添加 auth 列表
        meta_data["auths"] = permission_dict.get(obj.id, [])
        return meta_data

    def to_representation(self, instance):
        # Serialize the main instance data
        representation = super().to_representation(instance)
        # Filter out empty fields from the main data
        return {key: value for key, value in representation.items() if value not in [None, "", [], {}]}
