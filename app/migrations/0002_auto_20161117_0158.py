# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 01:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('content_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=8, max_digits=11)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('squad_size', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('size', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='squaduser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='squaduser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='squaduser',
            name='avatar',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='squaduser',
            name='friends',
            field=models.ManyToManyField(related_name='_squaduser_friends_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='squaduser',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='squad',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='app.Pin'),
        ),
        migrations.AddField(
            model_name='squaduser',
            name='squad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='app.Squad'),
        ),
    ]
