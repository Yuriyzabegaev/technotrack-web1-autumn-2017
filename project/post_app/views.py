# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog_app.models import Blog
from comment_app.models import Comment
from post_app.models import Post


#def post(request, blog_pk=None, post_pk=None):
#    return render(request, 'post_app/post.html', {'blog_pk' : blog_pk, 'post_pk' : post_pk})


class PostDetail(CreateView):

    template_name = 'post_app/post.html'
    context_object_name = 'post'
    model = Comment
    fields = ('data',)

    def get_context_data(self, **kwargs):

        context = super(PostDetail, self).get_context_data(**kwargs)
        post_obj = Post.objects.filter(pk=self.kwargs.get('pk'))

        context['post'] = self.post_object
        context['comment_count'] = Comment.objects.filter(post=post_obj).count()
        print context
        return context

    def dispatch(self, request, pk=None, *args, **kwargs):
        #self.post = get_object_or_404(Post.objects.filter(id=self.kwargs.get('pk')))
        #self.post = get_object_or_404(Post.objects.all, id=kwargs.get("pk"))
        self.post_object = Post.objects.all().get(pk=pk)   # !!

        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_app:post_detail', kwargs={'pk': self.object.post.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.post_object.blog
        form.instance.post = self.post_object
        return super(PostDetail, self).form_valid(form)

    # def get_queryset(self):
    #
    #     return super(PostDetail, self).get_queryset()


class PostUpadte(UpdateView):

    template_name = 'post_app/edit_post.html'
    model = Post
    fields = 'title', 'text'

    def get_queryset(self):
        return super(PostUpadte, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse("post_app:post_detail", kwargs={'pk' : self.object.pk})


class PostNew(CreateView):
    template_name = 'post_app/new_post.html'
    model = Post
    fields = 'title', 'text'

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, pk=kwargs.get('blog_id'))
        return super(PostNew, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_app:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(PostNew, self).form_valid(form)
