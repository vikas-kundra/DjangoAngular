# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_userdetails_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default=20, max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=b'India', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'None', max_length=30),
        ),
    ]
