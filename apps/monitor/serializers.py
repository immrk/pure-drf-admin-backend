from rest_framework import serializers
from .models import LoginLog, OperationLog


class LoginLogSerializer(serializers.ModelSerializer):
    """登录日志序列化器"""

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    login_type = serializers.CharField(source="get_login_type_display", read_only=True)

    class Meta:
        model = LoginLog
        fields = "__all__"


class OperationLogSerializer(serializers.ModelSerializer):
    """操作日志序列化器"""

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    creator = serializers.CharField(source="creator.username", read_only=True)

    class Meta:
        model = OperationLog
        fields = "__all__"