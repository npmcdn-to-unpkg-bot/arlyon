# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_types_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='type',
        ),
        migrations.AddField(
            model_name='brands',
            name='categories',
            field=models.ManyToManyField(to='website.Categories'),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='library',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wardrobe',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
