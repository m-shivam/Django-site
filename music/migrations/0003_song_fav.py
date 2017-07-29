# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170711_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='fav',
            field=models.BooleanField(default=False),
        ),
    ]
