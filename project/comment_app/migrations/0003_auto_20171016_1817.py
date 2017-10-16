# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0003_auto_20171015_2116'),
        ('comment_app', '0002_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='data',
            field=models.TextField(default=''),
        ),
    ]