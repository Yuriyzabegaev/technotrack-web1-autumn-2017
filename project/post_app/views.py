# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from comment_app.models import Comment
from post_app.models import Post


#def post(request, blog_pk=None, post_pk=None):
#    return render(request, 'post_app/post.html', {'blog_pk' : blog_pk, 'post_pk' : post_pk})


class PostDetail(DetailView):

    template_name = 'post_app/post.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comment_count'] = Comment.objects.filter(post=self.object).count()
        return context