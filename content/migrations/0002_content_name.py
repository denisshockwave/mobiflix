# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
