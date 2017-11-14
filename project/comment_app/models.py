# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from application import settings


class Comment(models.Model):

    title = models.CharField(max_length=255, default='')
    data = models.TextField(default='')
    post = models.ForeignKey('post_app.Post', related_name='comments')
    blog = models.ForeignKey('blog_app.Blog', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    def __unicode__(self):
        return u'{}, (author:{} blog:{} post:{})'.format(self.title, self.author, self.blog, self.post)