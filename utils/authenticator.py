from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from utils.response import CustomResponse


class CustomTokenRefreshView(TokenRefreshView):
    """自定义刷新令牌视图，返回自定义格式的响应，适配pure前端需求"""

    def post(self, request, *args, **kwargs):
        # 调用父类的 post 方法来获取默认的响应
        current_time = timezone.now()

        # 检查响应状态是否为 200 (OK)
        try:
            # 获取原始数据
            response = super().post(request, *args, **kwargs)
            original_data = response.data
            access_token = original_data.get('access')
            refresh_token = original_data.get('refresh')

            # 计算访问令牌的到期时间
            access_token_lifetime = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
            expiration_time = current_time + \
                access_token_lifetime + timedelta(hours=8)
            expiration_time_str = expiration_time.strftime('%Y/%m/%d %H:%M:%S')
            
            data = {
                    'accessToken': access_token,
                    'refreshToken': refresh_token,
                    'expires': expiration_time_str
                }
            return CustomResponse(data=data, msg="token刷新成功")
        except:
            # 处理错误响应
            return CustomResponse(success=False, msg="登录信息已失效", status=status.HTTP_401_UNAUTHORIZED)
