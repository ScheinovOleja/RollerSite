import random
import string

import requests
from django.contrib import messages
from django.contrib.auth import get_user, authenticate, login, update_session_auth_hash
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views import View


class ChangePasswordOrEmail(View):

    def get(self, request):
        return render(request, template_name='personal_area.html')

    def post(self, request):
        email = request.POST['email']
        if email:
            user = get_user(request)
            if user.email == email:
                messages.error(request, 'Email совпадает с текущим!', extra_tags='incorrect_email')
            else:
                try:
                    user.email = email
                    user.save()
                except IntegrityError as err:
                    user.email = request.user.email
                    messages.error(request, 'Пользователь с таким email уже существует!', extra_tags='incorrect_email')
                    user.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        cur_pass = request.POST['cur_pass']
        user = authenticate(phone=request.user.phone, password=cur_pass)
        if user is not None:
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                request.user.set_password(pass1)
                request.user.save()
                update_session_auth_hash(request, request.user)
                login(request, request.user)
            else:
                messages.error(request, 'Пароли не совпадают', extra_tags='pass_mismatch')
        else:
            messages.error(request, 'Неверный текущий пароль!', extra_tags='incorrect_pass')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeAvatar(View):

    def post(self, request):
        if request.is_ajax():
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for i in range(8))
            avatar = requests.get(
                url=f'https://avatars.dicebear.com/api/initials/{request.user.first_name}_{request.user.last_name}'
                    f'{rand_string}.svg?size=32')
            request.user.avatar = avatar.content.decode(encoding='utf-8').replace('\'', '')
            request.user.save()
            return HttpResponse(True)
