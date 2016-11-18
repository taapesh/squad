# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='created_by',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squadinvite',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squadinvite',
            name='invited_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
