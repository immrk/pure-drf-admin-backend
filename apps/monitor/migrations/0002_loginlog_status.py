# Generated by Django 5.1 on 2024-10-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginlog',
            name='status',
            field=models.BooleanField(default=True, help_text='登录状态', verbose_name='登录状态'),
        ),
    ]