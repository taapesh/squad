# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 21:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SquadUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('token', models.CharField(blank=True, max_length=255)),
                ('friends', models.ManyToManyField(related_name='_squaduser_friends_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=8, max_digits=11)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.CharField(blank=True, default='none', max_length=255, null=True)),
                ('content_url', models.CharField(blank=True, max_length=255, null=True)),
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
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SquadActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=255)),
                ('squad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='app.Squad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SquadInvite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('squad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='app.Squad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pin',
            name='squad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to='app.Squad'),
        ),
        migrations.AddField(
            model_name='pin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='squaduser',
            name='squad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='app.Squad'),
        ),
    ]
