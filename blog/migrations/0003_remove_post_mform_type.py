# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-03 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170403_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mform_type',
        ),
    ]
