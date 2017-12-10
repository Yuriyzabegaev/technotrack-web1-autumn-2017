# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.views.generic import DetailView

from blog_app.models import Blog
from comment_app.models import Comment
from core.models import User
from post_app.models import Post


def base(request):
    return render(request, 'core/base.html', {'pk': 0})


def profile(request, user_pk=None):
    profile = get_object_or_404(User.objects.all(), pk=user_pk)  # !!
    return render(request, 'core/profile.html', {'user': profile})


def subscriptions(request, profile_id=None):
    return render(request, 'core/subscriptions.html', {'profile_id': profile_id})


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = "username", "first_name", "last_name", "password1", "password2", "email"


class RegisterView(CreateView):
    template_name = 'core/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("home")


class HomePageView(TemplateView):
    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Post.objects.all().order_by('-created_at')[:5]
        context['blog_count'] = Blog.objects.all().count()
        context['post_count'] = Post.objects.all().count()
        context['comment_count'] = Comment.objects.all().count()
        context['user_check'] = self.check()
        return context

    def check(self):
        if self.request.user.is_authenticated():
            return True
        return False

class ProfileView(ListView):
    template_name = 'core/profile_list.html'
    model = User


class ProfileDetailView(DetailView):
    template_name = 'core/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['show_blogs_by_user'] = Blog.objects.filter(author=self.request.user).order_by('updated_at')
        return context

        # class MyPageView(ProfileDetailView):

        #   template_name = 'core/mypage.html'
        #    model = request.user
