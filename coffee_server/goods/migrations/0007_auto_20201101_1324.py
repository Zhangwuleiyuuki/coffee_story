# Generated by Django 2.2.12 on 2020-11-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20201101_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='imgurl',
            field=models.URLField(default='http://127.0.0.1:8000/static/6.png'),
        ),
    ]