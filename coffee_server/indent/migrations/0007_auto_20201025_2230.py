# Generated by Django 2.2.12 on 2020-10-25 22:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userinfo_city'),
        ('goods', '0004_goodsinfo_num'),
        ('indent', '0006_auto_20201024_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indentinfo',
            name='state',
        ),
        migrations.AlterField(
            model_name='indentinfo',
            name='timeout',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 26, 22, 30, 24, 530721), verbose_name='过期时间'),
        ),
        migrations.CreateModel(
            name='Yizhif_indent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inum', models.CharField(max_length=64, verbose_name='商品编号')),
                ('info', models.TextField(verbose_name='订单信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('goods_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo', verbose_name='商品')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo', verbose_name='用户')),
            ],
        ),
    ]
