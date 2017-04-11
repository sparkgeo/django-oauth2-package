import urllib

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.template import loader


class LoginView(View):

    def get(self, request):
        data = {
            'next': request.GET.get('next'),
            'error': request.GET.get('error') or '',
            'logo': settings.LOGIN_FORM_LOGO
        }
        template = loader.get_template('oauth2_package/login.html')
        return HttpResponse(template.render(data, request))

    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        next = request.POST.get('next')

        if user and user.is_active:
            login(request, user)
            print('Is authenticated: {}'.format(user.is_authenticated()))
            authorize_url = '{}'.format(next)
            print('authorize_url: {}\n'.format(authorize_url))
            return redirect(authorize_url, False)

        login_url = reverse('login')
        qp = {
            'error': 'Invalid login credentials.'
        }
        if next:
            qp['next'] = next

        login_url += '?{}'.format(urllib.urlencode(qp))
        return redirect(login_url, False)
