# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial', '0003_auto_20161117_2216'),
    ]
    operation = [
    	migrations.CreateModel(
            name='PoliceCall',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('street_number', models.IntegerField(null=True)),
                ('street_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]