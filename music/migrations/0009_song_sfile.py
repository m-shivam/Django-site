# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20170716_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='sfile',
            field=models.FileField(default=78, upload_to=b'', validators=[music.models.valSong]),
            preserve_default=False,
        ),
    ]
