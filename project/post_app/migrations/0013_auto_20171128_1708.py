# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0012_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='post',
            new_name='post_object',
        ),
    ]