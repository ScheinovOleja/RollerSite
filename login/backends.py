from django.contrib.auth.backends import ModelBackend
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
            if '+7' in phone:
                index = 2
            else:
                index = 1
            regex = r'^(8|\+7)' + '(' + phone[index:] + ')'
            user = MyUser.objects.get(phone__regex=regex)
            if user.check_password(password) is True:
                return user
        except MyUser.DoesNotExist:
            pass

