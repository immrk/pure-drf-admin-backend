from django.apps import AppConfig


class SystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.system"

    def ready(self):
        # 导入信号处理器
        import apps.system.signals
