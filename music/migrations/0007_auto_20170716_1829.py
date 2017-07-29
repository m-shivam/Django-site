# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_song_sfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='sfile',
            field=models.FileField(upload_to=b''),
        ),
    ]
