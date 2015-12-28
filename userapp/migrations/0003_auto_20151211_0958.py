# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_user_next'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_new',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User_next',
        ),
    ]
