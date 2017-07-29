# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20170716_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='ftype',
        ),
        migrations.RemoveField(
            model_name='song',
            name='sfile',
        ),
    ]
