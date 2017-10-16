from django.conf.urls import url, include
from core.views import *

urlpatterns = [
#    url(r'^mypage$', MyPageView.as_view(), name='mypage'),
    url(r'^profile_(P?\d+)/subscriptions/$', subscriptions),
    url(r'^profile_list/$', ProfileView.as_view(), name='profile_list'),
    url(r'^profile_(?P<user_pk>\d+)/$', profile, name='profile'),
    url(r'^feedback/$', feedback),
]