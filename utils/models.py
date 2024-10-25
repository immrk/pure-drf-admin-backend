from django.db import models
import uuid


class UuidModel(models.Model):
    """自定义uuid模型"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name=("ID"))

    class Meta:
        abstract = True


class CharModel(models.Model):
    """自定义字符id模型"""

    id = models.CharField(primary_key=True, max_length=128, verbose_name=("ID"))

    class Meta:
        abstract = True


class BaseModel(models.Model):
    """基类模型"""

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True  # 抽象模型类, 用于继承使用
