# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20161006_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='2016/10/7/'),
        ),
    ]
