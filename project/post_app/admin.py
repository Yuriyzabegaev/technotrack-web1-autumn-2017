# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from comment_app.models import Comment
from .models import Post

class CommentInline(admin.TabularInline):

    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = 'postId', 'title', 'author', 'blog', 'text',
    list_editable = 'title', 'text',
    inlines = CommentInline,

