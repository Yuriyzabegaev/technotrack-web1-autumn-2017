# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from core.views import *
from blog_app.views import *
from .views import *
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(BlogUpadte.as_view()), name="blog_edit"),
    url(r'^new/$', login_required(BlogNew.as_view()), name='blog_new'),

]