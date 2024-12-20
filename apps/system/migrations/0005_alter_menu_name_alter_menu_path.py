# Generated by Django 4.1.8 on 2024-09-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_rename_is_active_deptinfo_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='菜单名称'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='path',
            field=models.CharField(max_length=255, null=True, verbose_name='路由地址'),
        ),
    ]
