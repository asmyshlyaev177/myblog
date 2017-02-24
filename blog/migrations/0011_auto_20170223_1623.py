# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170217_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image_small',
            field=models.ImageField(blank=True, null=True, upload_to='2017/2/23/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='2017/2/23/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Черновик/удалён'), ('P', 'Опубликован')], default='D', max_length=1, verbose_name='Статус'),
        ),
    ]
