# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipper', '0007_auto_20160516_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelog',
            name='date',
            field=models.DateTimeField(),
        ),
    ]