# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from core.views import *
from blog_app.views import *
from .views import *


urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^blog_(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^blog_(?P<blog_pk>\d+)/', include('post_app.urls', namespace="post_app")),
]