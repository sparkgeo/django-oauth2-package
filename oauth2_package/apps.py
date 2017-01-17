from __future__ import unicode_literals

from django.apps import AppConfig


class OAuth2PackageConfig(AppConfig):
    name = 'oauth2_package'

    settings_module = "oauth2_package.app_settings"
