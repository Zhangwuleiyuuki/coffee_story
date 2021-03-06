# Generated by Django 2.2.12 on 2020-10-11 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20201010_1944'),
        ('goods', '0003_auto_20201003_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=256)),
                ('goods_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo')),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
    ]
