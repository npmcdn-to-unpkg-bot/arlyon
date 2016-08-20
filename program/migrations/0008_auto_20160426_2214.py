# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_auto_20160426_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='mods',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mods',
            name='ksp_version',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='mods',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='missionstatuses',
            name='color',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='mods',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mods',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mods',
            name='version',
            field=models.CharField(max_length=20),
        ),
    ]
