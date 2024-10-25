from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from apps.system.models import Menu


class CustomUserManager(BaseUserManager):
    """
    自定义用户管理器，用于创建用户和超级用户
    """

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("用户必须有一个电子邮件地址")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("超级用户必须设置 is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("超级用户必须设置 is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    自定义用户表, 实现auth鉴权与权限管理, 实现自定义字段(会自动补上password与last_login字段)
    """

    avatar = models.CharField(max_length=100, unique=False, default=None, null=True)
    nickname = models.CharField(max_length=100, unique=False, default=None, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    role = models.ManyToManyField("system.Role", verbose_name=("角色"), blank=True)
    dept = models.ForeignKey(to="system.DeptInfo", verbose_name=("部门"), on_delete=models.PROTECT, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"  # 用于登录的字段
    REQUIRED_FIELDS = ["username"]  # 创建超级用户时必须输入的字段

    def __str__(self):
        return self.username

    def is_active(self):
        return self.status

    def has_perm(self, perm_code=None, path=None):
        # 检查所有角色的权限
        for role in self.role.filter(status=True):
            if not path:
                # 获取当前角色关联的权限菜单
                permissions = role.menu.filter(menu_type=Menu.MenuChoices.PERMISSION, status=True).values_list("code", flat=True)
            else:
                # 获取当前角色关联的权限菜单
                permissions = role.menu.filter(menu_type=Menu.MenuChoices.PERMISSION, status=True, path=path).values_list("code", flat=True)

            # 如果权限代码在权限菜单中，返回 True
            if perm_code in permissions:
                return True

        # 如果没有找到匹配的权限，返回 False
        return False
