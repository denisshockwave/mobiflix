# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.FileField(blank=True, null=True, upload_to=b'')),
                ('status', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('movie_unique', models.TextField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device1', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('device2', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watchers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('code_expiration', models.DateTimeField(blank=True, default=None, null=True)),
                ('logged_in_counter', models.IntegerField(blank=True, default=None, null=True)),
                ('last_login', models.DateTimeField(blank=True, default=None, null=True)),
                ('devices', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Devices')),
            ],
        ),
    ]
