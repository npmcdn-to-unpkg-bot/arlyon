# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipper', '0008_auto_20160516_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='buylimit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='highalch',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]