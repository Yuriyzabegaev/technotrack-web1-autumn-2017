# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView

from blog_app.models import Blog
from comment_app.models import Comment
from core.models import User
from post_app.models import Post


def base(request):

    return render(request, 'core/base.html', {'pk': 0})


def feedback(request):

    return render(request, 'core/feedback.html')


def profile (request, user_pk=None):
    profile = get_object_or_404(User.objects.all(), pk = user_pk) #!!
    return render(request, 'core/profile.html', {'user' : profile})


def subscriptions (request, profile_id=None):

    return render(request, 'core/subscriptions.html', {'profile_id' : profile_id})

class HomePageView(TemplateView):

    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['latest_articles'] = Blog.objects.order_by('-created_at') [:5] #?
        context['blog_count'] = Blog.objects.all().count()
        context['post_count'] = Post.objects.all().count()
        context['comment_count'] = Comment.objects.all().count()
        return context

class ProfileView(ListView):

    template_name = 'core/profile_list.html'
    model = User

class ProfileDetailView(DetailView):

    template_name = 'core/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['show_blogs_by_user'] = Blog.objects.all().order_by('updated_at') #.filter(author=request.username)
        return context

#class MyPageView(ProfileDetailView):

#   template_name = 'core/mypage.html'
#    model = request.user