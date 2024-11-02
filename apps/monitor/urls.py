from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginLogViewSet, OperationLogViewSet, DeleteAllLoginLogView, DeleteAllOperationView

router = DefaultRouter()    
router.register("loginlog", LoginLogViewSet, basename="loginlog")
router.register("operationlog", OperationLogViewSet, basename="operationlog")

urlpatterns = [
    path("", include(router.urls)),
    path("clearloginlog/", DeleteAllLoginLogView.as_view(), name="delete_all_loginlog"),
    path("clearoperationlog/", DeleteAllOperationView.as_view(), name="delete_all_operationlog"),
]