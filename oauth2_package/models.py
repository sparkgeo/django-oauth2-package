from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError('Users must choose a username.')
        if not email:
            raise ValueError('Users must have a valid email address.')

        account = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        account.clean()
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, email, password, **kwargs):
        account = self.create_user(username, email, password, **kwargs)

        account.is_staff = True
        account.is_superuser = True
        account.save()

        return account


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.__unicode__()

    def get_short_name(self):
        return self.__unicode__()
