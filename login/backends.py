from django.contrib.sessions.models import Session
from django.contrib.auth.backends import ModelBackend
from RollerSiteCms import settings
from login.models import MyUser


class MyBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        # Session.objects.all().delete()
        try:
            phone = kwargs['username']
        except:
            phone = kwargs['phone']
        password = kwargs['password']
        try:
            regex = r'^(8|\+7)' + '(' + phone[1:] + ')'
            user = MyUser.objects.get(phone__regex=regex)
            if user.check_password(password) is True:
                return user
        except MyUser.DoesNotExist:
            pass

