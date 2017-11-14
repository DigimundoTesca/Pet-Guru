# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.TextField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='staff_only',
        ),
        migrations.RemoveField(
            model_name='room',
            name='title',
        ),
        migrations.AddField(
            model_name='room',
            name='label',
            field=models.SlugField(default='Room 1', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.TextField(default='name 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.Room'),
        ),
    ]