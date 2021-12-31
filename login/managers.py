import requests
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The given email must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        avatar = requests.get(url=f'https://avatars.dicebear.com/api/initials/{user.first_name}_{user.last_name}.svg?size=32')
        user.avatar = avatar.content.decode(encoding='utf-8').replace('\'', '')
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(phone, password, **extra_fields)

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None
