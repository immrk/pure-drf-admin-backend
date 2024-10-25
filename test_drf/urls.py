"""
URL configuration for test_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from utils.authenticator import CustomTokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("apps.user.urls")),  # 包含user应用的URL
    path("api/system/", include("apps.system.urls")),  # 包含user应用的URL
    path("api/test/", include("apps.functiontest.urls")),  # 包含functiontest应用的URL
    path("api/token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
]
