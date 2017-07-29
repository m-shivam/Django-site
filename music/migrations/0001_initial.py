# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=30)),
                ('artist', models.CharField(max_length=50)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stitle', models.CharField(max_length=500)),
                ('ftype', models.CharField(max_length=10)),
                ('sartist', models.CharField(max_length=20)),
                ('alb_id', models.ForeignKey(to='music.Album')),
            ],
        ),
    ]
