# signals.py

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Role


@receiver(pre_delete, sender=Role)
def delete_role_user_relationship(sender, instance, **kwargs):
    # 清除与被删除角色相关的所有用户关联
    for user in instance.user_set.all():  # 访问与 Role 相关联的所有 User 对象
        user.role.remove(instance)  # 从每个用户的角色中删除当前的 Role 实例
