from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from post_app.views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^new/(?P<blog_id>\d+)/$', login_required(PostNew.as_view()), name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(PostUpadte.as_view()), name="post_edit"),
    url(r'^(?P<pk>\d+)/likecount$', PostLikeAjaxView.as_view(), name='like'),
    # url(r'^(?P<pk>\d+)/create_comment$', login_required(CommentNew.as_view()), name="comment_new"),
]