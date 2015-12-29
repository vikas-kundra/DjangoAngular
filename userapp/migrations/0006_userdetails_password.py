# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20151229_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='password',
            field=models.CharField(default=b'none', max_length=8),
        ),
    ]
