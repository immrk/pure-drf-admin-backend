from django.db import models
from utils.models import UuidModel, BaseModel


class Role(UuidModel, BaseModel):
    name = models.CharField(max_length=128, verbose_name=("角色名称"), unique=True)
    code = models.CharField(max_length=128, verbose_name=("角色代码"), unique=True)
    status = models.BooleanField(verbose_name=("激活状态"), default=True)
    menu = models.ManyToManyField("system.Menu", verbose_name=("菜单/权限"), blank=True)
    parent = models.ForeignKey("system.Role", on_delete=models.SET_NULL, verbose_name=("父级角色"), null=True, blank=True)

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = verbose_name
        ordering = ("create_time",)

    def __str__(self):
        return f"{self.name}({self.code})"


class Menu(UuidModel, BaseModel):
    class MenuChoices(models.IntegerChoices):
        DIRECTORY = 0, "Directory"
        MENU = 1, "Menu"
        PERMISSION = 2, "Permission"

    class MethodChoices(models.TextChoices):
        GET = "GET", "GET"
        POST = "POST", "POST"
        PUT = "PUT", "PUT"
        DELETE = "DELETE", "DELETE"
        PATCH = "PATCH", "PATCH"

    parent = models.ForeignKey("system.Menu", on_delete=models.SET_NULL, verbose_name=("父级菜单"), null=True, blank=True)
    menu_type = models.SmallIntegerField(choices=MenuChoices.choices, default=MenuChoices.DIRECTORY, verbose_name=("菜单类型"))
    name = models.CharField(verbose_name=("标识名称"), max_length=128)
    code = models.CharField(verbose_name=("权限标识"), max_length=128, unique=True, null=True, default=None)
    path = models.CharField(verbose_name=("路由地址"), max_length=255, null=True)
    component = models.CharField(verbose_name=("组件地址"), max_length=255, null=True, blank=True)
    status = models.BooleanField(verbose_name=("激活"), default=True)
    meta = models.OneToOneField(
        "system.MenuMeta",
        on_delete=models.CASCADE,
        verbose_name=("Menu meta"),
        null=True,
    )
    method = models.CharField(choices=MethodChoices.choices, null=True, blank=True, verbose_name=("Method"), max_length=10)
    redirect = models.CharField(verbose_name=("Redirect"), max_length=255, null=True, blank=True, help_text=("Redirect address"))

    def delete(self, using=None, keep_parents=False):
        if self.meta:
            self.meta.delete(using, keep_parents)
        super().delete(using, keep_parents)

    class Meta:
        verbose_name = "菜单/权限"
        verbose_name_plural = verbose_name
        ordering = ("create_time",)

    def __str__(self):
        return f"{self.meta.title}-{self.get_menu_type_display()}({self.name})"


class MenuMeta(UuidModel, BaseModel):
    title = models.CharField(verbose_name=("Menu title"), max_length=255, null=True, blank=True)
    icon = models.CharField(verbose_name=("Left icon"), max_length=255, null=True, blank=True)
    rank = models.IntegerField(verbose_name=("菜单显示优先级"), default=9999)
    r_svg_name = models.CharField(verbose_name=("Right icon"), max_length=255, null=True, blank=True, help_text=("Additional icon to the right of menu name"))
    is_show_menu = models.BooleanField(verbose_name=("Show menu"), default=True)
    is_show_parent = models.BooleanField(verbose_name=("Show parent menu"), default=False)
    is_keepalive = models.BooleanField(verbose_name=("Keepalive"), default=False, help_text=("When enabled, the entire state of the page is saved, and when refreshed, the state is cleared"))
    frame_url = models.CharField(verbose_name=("Iframe URL"), max_length=255, null=True, blank=True, help_text=("The embedded iframe link address"))
    frame_loading = models.BooleanField(verbose_name=("Iframe loading"), default=False)

    transition_enter = models.CharField(verbose_name=("Enter animation"), max_length=255, null=True, blank=True)
    transition_leave = models.CharField(verbose_name=("Leave animation"), max_length=255, null=True, blank=True)

    is_hidden_tag = models.BooleanField(verbose_name=("Hidden tag"), default=False, help_text=("The current menu name or custom information is prohibited from being added to the TAB"))
    fixed_tag = models.BooleanField(verbose_name=("Fixed tag"), default=False, help_text=("Whether the current menu name is fixed to the TAB and cannot be closed"))
    dynamic_level = models.IntegerField(verbose_name=("Dynamic level"), default=0, help_text=("Maximum number of dynamic routes that can be opened"))

    class Meta:
        verbose_name = "Menu meta"
        verbose_name_plural = verbose_name
        ordering = ("-create_time",)

    def __str__(self):
        return f"{self.title}-{self.description}"


class DeptInfo(UuidModel, BaseModel):
    name = models.CharField(verbose_name=("Department name"), max_length=128)
    code = models.CharField(max_length=128, verbose_name=("Department code"), unique=True)
    type = models.SmallIntegerField(verbose_name=("Department type"), default=0)
    parent = models.ForeignKey("system.DeptInfo", on_delete=models.SET_NULL, verbose_name=("Superior department"), null=True, blank=True, related_query_name="parent_query")
    roles = models.ManyToManyField("system.Role", verbose_name=("Role permission"), blank=True)
    rank = models.IntegerField(verbose_name=("Rank"), default=99)
    auto_bind = models.BooleanField(verbose_name=("Auto bind"), default=False, help_text=("If the value of the registration parameter channel is consistent with the department code, the user is automatically bound to the department"))
    status = models.BooleanField(verbose_name=("Is active"), default=True)

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name
        ordering = (
            "rank",
            "create_time",
        )

    def __str__(self):
        return f"{self.name}({self.pk})"

    # 定义一个方法，获取当前部门以及其所有子部门包括子部门id列表
    def get_child_dept_ids(self):
        dept_ids = [self.pk]
        children = DeptInfo.objects.filter(parent=self)
        for child in children:
            dept_ids.extend(child.get_child_dept_ids())
        return dept_ids
