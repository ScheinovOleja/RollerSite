from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from RollerSiteCms.settings import LOGIN_REDIRECT_URL
from login.forms import LoginForm


# Create your views here.


class MyLoginView(LoginView):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(phone=cd['phone'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(LOGIN_REDIRECT_URL)
            else:
                messages.error(request, 'Неверный логин или пароль!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class MyLogoutView(LogoutView):
    next_page = '/'
