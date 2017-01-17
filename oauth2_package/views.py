from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from djoser import views as djoser_views

class LoginView(djoser_views.LoginView):

    def get(self, request):
        data = {
            'next': request.GET.get('next')
        }
        return render(request, 'oauth2_package/login.html', context=data)
