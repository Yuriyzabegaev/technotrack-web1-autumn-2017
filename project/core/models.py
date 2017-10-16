# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    class Meta:
        ordering = 'username',
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
