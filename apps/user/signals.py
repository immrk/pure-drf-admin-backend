# users/signals.py

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import User


@receiver(pre_delete, sender=User)
def delete_user_role_relationship(sender, instance, **kwargs):
    # 清除与被删除用户相关的所有角色关联
    instance.role.clear()
