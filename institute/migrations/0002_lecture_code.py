# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-19 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='code',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]