# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20160426_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missions',
            name='crewmembers',
            field=models.IntegerField(default=0),
        ),
    ]