# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipper', '0005_auto_20160513_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flip',
            name='requestdate',
            field=models.DateTimeField(),
        ),
    ]