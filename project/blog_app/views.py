# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog_app.models import Blog


def blog(request, ident):

    return render(request, 'blog_app/blog.html', {'ident': ident})

class BlogList(ListView):
    template_name = "blog_app/blog_list.html"
    model = Blog

class BlogDetail(DetailView):
    template_name = 'blog_app/blog.html'
    context_object_name = 'blog'
    model = Blog
