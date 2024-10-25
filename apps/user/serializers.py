from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.system.models import Role

User = get_user_model()  # 获取自定义的用户模型


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器，用于创建和检索用户"""

    dept_name = serializers.SerializerMethodField()
    role_name = serializers.SerializerMethodField()
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True, required=False, default=list)
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = User
        fields = ("id", "email", "username", "nickname", "avatar", "password", "status", "last_login", "dept", "dept_name", "role", "role_name")
        extra_kwargs = {"password": {"write_only": True}}  # 设置密码为只写字段

    def get_dept_name(self, obj):
        """获取部门名称"""
        if obj.dept:
            return obj.dept.name  # 假设DeptInfo表中有一个name字段存储部门名称
        return None

    def get_role_name(self, obj):
        """获取角色名称列表"""
        # 返回角色名称列表
        return [role.name for role in obj.role.all()]

    def create(self, validated_data):
        """重写创建方法以使用set_password方法来创建用户；同时处理role字段"""
        password = validated_data.pop("password")
        roles = validated_data.pop("role", [])
        user = User(**validated_data)
        user.set_password(password)  # 使用set_password来设置密码
        user.save()
        user.role.set(roles)  # 设置用户角色
        return user

    def update(self, instance, validated_data):
        """重写更新方法，以便在更新密码时也能使用set_password；同时处理role字段"""
        password = validated_data.pop("password", None)
        roles = validated_data.pop("role", [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()
        # 更新role多对多字段
        if roles:
            instance.role.set(roles)

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
