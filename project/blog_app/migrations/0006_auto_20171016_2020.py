# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_blog_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]
