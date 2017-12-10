# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog_app.models import Blog
from comment_app.models import Comment
from post_app.models import Post, Like


#def post(request, blog_pk=None, post_pk=None):
#    return render(request, 'post_app/post.html', {'blog_pk' : blog_pk, 'post_pk' : post_pk})


class PostDetail(CreateView):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('core:login')
        return super(PostDetail, self).post(request, *args, **kwargs)

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



    def get_success_url(self):
        return self.request.META['HTTP_REFERER']


class PostNew(CreateView):
    context_object_name = 'post'
    template_name = 'post_app/new_post.html'
    model = Post
    fields = 'title', 'text'

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, pk=kwargs.get('blog_id'))
        return super(PostNew, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def get_context_data(self, **kwargs):
        context = super(PostNew, self).get_context_data()
        context['blog'] = self.blog
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(PostNew, self).form_valid(form)


class PostLikes(View):

    def get(self, request):
        ids = request.GET.get('ids','')
        ids = ids.split(',')
        post_object = dict(Post.objects.filter(id__in=ids).values_list('pk','likecount'))
        return JsonResponse(post_object)


class PostLikeAjaxView(View):

    post_object = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post_object = get_object_or_404(Post, pk=pk)
        return super(PostLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(self.post_object.likecount)

    # def post(self, request):
    #     if not self.post_object.likes.filter()
    #     like = Like.objects.create(self.post_object, self.request.user)
    #
    #     return HttpResponse(self.post_object.likecount)
