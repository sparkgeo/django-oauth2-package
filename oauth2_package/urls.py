from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import get_user_model

import oauth2_provider.views as oauth2_views
from .views import LoginView

User = get_user_model()

oauth2_provider_urlpatterns = (
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name='authorize'),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name='token'),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name='revoke-token'),
)

auth_urlpatterns = (
    url(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^logout/$', djoser_views.LogoutView.as_view(), name='logout'),
    # url(r'^me/$', djoser_views.UserView.as_view(), name='user'),
    # url(r'^register/$', djoser_views.RegistrationView.as_view(), name='register'),
    # url(r'^activate/$', djoser_views.ActivationView.as_view(), name='activate'),
    # url(r'^{0}/$'.format(User.USERNAME_FIELD), djoser_views.SetUsernameView.as_view(), name='set_username'),
    # url(r'^password/$', djoser_views.SetPasswordView.as_view(), name='set_password'),
    # url(r'^password/reset/$', djoser_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password/reset/confirm/$', djoser_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
)

urlpatterns = (oauth2_provider_urlpatterns +
               auth_urlpatterns)
