from django.conf.urls import url
from post_app.views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
]