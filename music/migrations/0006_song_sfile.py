# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20170716_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='sfile',
            field=models.FileField(default=b'', upload_to=b''),
        ),
    ]
