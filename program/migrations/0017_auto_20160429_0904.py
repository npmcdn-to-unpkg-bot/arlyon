# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0016_auto_20160429_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='image',
            field=models.FilePathField(path='D:\\Documents\\Programming\\kmlprogram/static/shiptypes'),
        ),
        migrations.AlterField(
            model_name='shiptypes',
            name='image',
            field=models.FilePathField(path='D:\\Documents\\Programming\\kmlprogram/static/shiptypes'),
        ),
    ]
