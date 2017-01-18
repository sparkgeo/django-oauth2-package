from django.conf import settings

INSTALLED_APPS = getattr(settings, 'INSTALLED_APPS', tuple())
MIDDLEWARE = getattr(settings, 'MIDDLEWARE', tuple())
AUTHENTICATION_BACKENDS = getattr(settings, 'AUTHENTICATION_BACKENDS', tuple())
REST_FRAMEWORK = getattr(settings, 'REST_FRAMEWORK', {})
TEMPLATE_LOADERS = getattr(settings, 'TEMPLATE_LOADERS', tuple())


def _append(setting, additions, index=None):
    setts = getattr(settings, setting, [])
    additions = [a for a in additions if a not in setts]
    if isinstance(setts, tuple):
        additions = tuple(additions)

    return setts + additions

AUTH_USER_MODEL = 'oauth2_package.User'
LOGIN_URL = '/auth/login/'
CORS_ORIGIN_ALLOW_ALL = True
ACCESS_TOKEN_EXPIRE_SECONDS = getattr(settings, 'ACCESS_TOKEN_EXPIRE_SECONDS', 7200)
LOGIN_FORM_LOGO = ''

INSTALLED_APPS = _append('INSTALLED_APPS', (
    'rest_framework.authtoken',
    'oauth2_provider',
    'corsheaders',
))

MIDDLEWARE = _append('MIDDLEWARE', (
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
))

AUTHENTICATION_BACKENDS = _append('AUTHENTICATION_BACKENDS',(
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
))

#
# RESTFRAMEWORK SETTINGS
#

REST_FRAMEWORK = getattr(settings, 'REST_FRAMEWORK', {})
if 'DEFAULT_RENDERER_CLASSES' not in REST_FRAMEWORK:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ()
if 'oauth2_provider.ext.rest_framework.OAuth2Authentication' not in REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ('oauth2_provider.ext.rest_framework.OAuth2Authentication',) + REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']

if 'rest_framework.authentication.SessionAuthentication' not in REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += ('rest_framework.authentication.SessionAuthentication',)
