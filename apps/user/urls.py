from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView

# 创建一个DefaultRouter路由器对象, 会自动按照drf规则创建路由
router = DefaultRouter()
router.register("", UserViewSet, basename="user")

# 自定义不采用鉴权的接口需要放置在DefaultRouter配置的前面，否则会受到鉴权的影响
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
