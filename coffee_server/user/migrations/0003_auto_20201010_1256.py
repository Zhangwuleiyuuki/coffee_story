# Generated by Django 2.2.12 on 2020-10-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201009_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=32, verbose_name='地址select'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='administrator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='detailed_address',
            field=models.TextField(verbose_name='详细地址/text'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(max_length=32, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
    ]