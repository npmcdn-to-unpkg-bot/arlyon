# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipper', '0004_auto_20160513_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flip',
            name='listeddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flip',
            name='purchasedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flip',
            name='solddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
