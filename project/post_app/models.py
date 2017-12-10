# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.db import models

from blog_app.models import Blog


class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    blog = models.ForeignKey(Blog, related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField(default='')
    is_deleted = models.BooleanField(default=False)
    likecount = models.IntegerField(default=0)

    def __unicode__(self):
        return u'{}, (author:{} blog:{})'.format(self.title, self.author, self.blog)

class Like(models.Model):

    post_object = models.ForeignKey(Post, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')