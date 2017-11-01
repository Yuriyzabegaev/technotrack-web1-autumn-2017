# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from post_app.models import Post
from .models import Blog

class PostInline(admin.TabularInline):

    model = Post

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'author', )
    list_editable = ('title', 'author', )
    inlines = PostInline,
