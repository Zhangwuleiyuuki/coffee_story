# Generated by Django 2.2.12 on 2020-10-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goodsinfo_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='imgurl',
            field=models.URLField(default='http://127.0.0.1:8000/static/02.jpg'),
        ),
    ]