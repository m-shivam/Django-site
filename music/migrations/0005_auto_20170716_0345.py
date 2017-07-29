# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170714_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='sbitrate',
            field=models.CharField(default=b'320 kbps', max_length=20),
        ),
        migrations.AddField(
            model_name='song',
            name='slength',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='song',
            name='ssize',
            field=models.CharField(default=b'', max_length=15),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(upload_to=b'', validators=[music.models.validate]),
        ),
    ]
