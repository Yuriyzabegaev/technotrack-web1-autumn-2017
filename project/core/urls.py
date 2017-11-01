from django.conf.urls import url, include
from django.contrib.auth import get_user_model

from core.views import subscriptions, ProfileView, profile, feedback, RegisterView
from core.views import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^logout/$', login_required(LogoutView.as_view(template_name='core/logout.html')), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='registration'),
    url(r'^profile_(P?\d+)/subscriptions/$', subscriptions),
    url(r'^profile_list/$', ProfileView.as_view(), name='profile_list'),
    url(r'^profile/(?P<user_pk>\d+)/$', profile, name='profile'),
    url(r'^feedback/$', feedback),
]