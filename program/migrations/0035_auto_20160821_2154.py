# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0034_auto_20160511_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_flag',
            field=models.FilePathField(path='/Users/arlyon/Documents/Projects/arlyon/program/static/flags/'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='image',
            field=models.FilePathField(path='/Users/arlyon/Documents/Projects/arlyon/program/static/programs/'),
        ),
        migrations.AlterField(
            model_name='shiptypes',
            name='image',
            field=models.FilePathField(path='/Users/arlyon/Documents/Projects/arlyon/program/static/shiptypes/'),
        ),
    ]
