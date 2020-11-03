# Generated by Django 2.2.12 on 2020-10-03 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='商品名')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='单价')),
                ('temperature', models.CharField(max_length=16, verbose_name='温度')),
                ('brand', models.CharField(max_length=16, verbose_name='品牌')),
                ('indent_num', models.IntegerField(verbose_name='订单数')),
                ('inventory', models.IntegerField(verbose_name='库存')),
                ('score', models.DecimalField(decimal_places=1, default=5, max_digits=2, verbose_name='评分')),
                ('pnumber', models.IntegerField(default=0, verbose_name='评分人数')),
                ('remark', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'goods_goods_info',
            },
        ),
    ]