# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20171016_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]