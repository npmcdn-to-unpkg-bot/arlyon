# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0014_agency_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_flag',
            field=models.FilePathField(path='D:\\Documents\\Programming\\kmlD:/Documents/Programming/kml/program/static/flags'),
        ),
    ]
