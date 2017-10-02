# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render

def base(request):

    return render(request, 'base.html', {'arg' : unicode(request.META)})

def blogList(request):

    return render(request, 'blogs.html')

def blog(request, blog_nmb):

    return render(request, 'blog.html', {'blog_nmb' : blog_nmb})

def feedback(request):

    return render(request, 'feedback.html')

def post(request, blog_id=None, post_id=None):

    return render(request, 'post.html', {'blog_id' : blog_id, 'post_id' : post_id})

def profile (request, profile_id=None):

    return render(request, 'profile.html', {'profile_id' : profile_id})

def subscriptions (request, profile_id=None):

    return render(request, 'subscriptions.html', {'profile_id' : profile_id})
