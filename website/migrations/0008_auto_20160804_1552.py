# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0007_auto_20160607_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=6)),
                ('brand', models.ForeignKey(to='website.Brands')),
            ],
            options={
                'verbose_name_plural': 'Furniture',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='types',
            name='image',
            field=models.FilePathField(path=b'/Users/arlyon/Documents/Projects/homecatalog/website/static/icons/fashion/'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='type',
            field=models.ForeignKey(to='website.Types'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
