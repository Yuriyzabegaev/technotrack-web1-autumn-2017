# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from blog_app.models import Blog
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

class BlogListForm(forms.Form):

    order_by = forms.ChoiceField(choices=(
        ('title', 'Title asc'),
        ('-title', 'Title desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)
    threshold = forms.IntegerField(required=False)


class BlogNew(CreateView):

    template_name = 'blog_app/new_blog.html'
    model = Blog
    fields = 'title', 'description'

    def get_success_url(self):

        return reverse("blog_app:blog_detail", kwargs={'pk' : self.object.pk})

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super(BlogNew, self).form_valid(form)


class BlogUpadte(UpdateView):

    template_name = 'blog_app/edit_blog.html'
    model = Blog
    fields = 'title', 'description'

    def get_queryset(self):
        return super(BlogUpadte, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse("blog_app:blog_detail", kwargs={'pk' : self.object.pk})


def blog(request, ident):
    return render(request, 'blog_app/blog.html', {'ident': ident})


class BlogList(ListView):
    template_name = "blog_app/blog_list.html"
    model = Blog
    paginate_by = 5
    def get_queryset(self):

        q = super(BlogList, self).get_queryset()
        self.form = BlogListForm(self.request.GET)

        if self.form.is_valid():
            if self.form.cleaned_data['threshold']:
                q = q.annotate(question_count=models.Count('posts')).filter(question_count__gt=self.form.cleaned_data['threshold'])
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
        p = Paginator(q, 5)
        return q

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['searchform'] = self.form
        return context



class BlogDetail(DetailView):
    template_name = 'blog_app/blog.html'
    context_object_name = 'blog'
    model = Blog
    paginate_by = 5




