# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='命令标题')),
                ('command', models.CharField(max_length=2000, verbose_name='命令')),
                ('describe', models.CharField(max_length=300, verbose_name='命令描述')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '命令',
                'verbose_name': '命令',
            },
        ),
    ]