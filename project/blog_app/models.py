# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class Blog(models.Model):

    title = models.CharField(max_length=255, default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    description = models.TextField(default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{}'.format(self.title)

    class Meta:
        ordering = ('-updated_at', )
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
