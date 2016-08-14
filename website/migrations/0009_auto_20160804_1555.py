# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0008_auto_20160804_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='room',
            field=models.ForeignKey(default=1, to='website.Room'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
