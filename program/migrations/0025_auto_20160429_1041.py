# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0024_auto_20160429_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_flag',
            field=models.FilePathField(path='D:/program/static/flags/'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='image',
            field=models.FilePathField(path='D:/program/static/programs/'),
        ),
        migrations.AlterField(
            model_name='shiptypes',
            name='image',
            field=models.FilePathField(path='D:\\Documents\\Programming\\kml/program/static/shiptypes/'),
        ),
    ]
