import requests
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from social_treatment.mailing import send_register_user
from .models import MyUser, RegisterFromMessangers


class CustomUserCreationForm(forms.ModelForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('phone',)

    def _post_clean(self):
        super()._post_clean()
        self.password = MyUser.objects.make_random_password(length=8)
        if self.password:
            try:
                password_validation.validate_password(self.password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.password)
        phone = self.cleaned_data['phone']
        messenger_user = RegisterFromMessangers.objects.get_or_none(phone=phone)
        avatar = requests.get(
            url=f'https://avatars.dicebear.com/api/initials/{user.first_name}_{user.last_name}.svg?size=32')
        user.avatar = avatar.content.decode(encoding='utf-8').replace('\'', '')
        user.save()
        if messenger_user:
            text = f"Доброго времени суток!\n\n" \
                      f"Вы зарегистрированы на сайте group-mgr.ru!\n" \
                      f"Ваши данные для входа на сайт:\n" \
                      f"Логин - <code>{phone}</code>,\n" \
                      f"Пароль - <code>{self.password}</code>.\n\n" \
                      f"Обязательно смените пароль!!"
            messenger_user.user = user
            messenger_user.save()
            try:
                send_register_user(phone, self.password, messenger_user, text)
            except Exception as err:
                import asyncio
                loop = asyncio.new_event_loop()
                bot_token = '5125599420:AAFvc7hcTAR-nOT26w1zq2-SEPO-M9PCtMY'
                from aiogram import Bot
                from aiogram import types
                bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
                loop.run_until_complete(bot.send_message(715845455, f'Ошибка\n {err}'))
                loop.close()
        else:
            import asyncio
            loop = asyncio.new_event_loop()
            bot_token = '5125599420:AAFvc7hcTAR-nOT26w1zq2-SEPO-M9PCtMY'
            from aiogram import Bot
            from aiogram import types
            bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
            loop.run_until_complete(bot.send_message(715845455, f'Пользователя нет'))
            loop.close()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('phone', 'password',)


class LoginForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^((8|\+7)[\-]?)?(\(?\d{3}\)?[\-]?)?[\d\-]{7,10}$',
                                 message="Номер телефона в формате 89123456789")
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}), validators=[phone_regex],
                            max_length=12, label='Номер телефона')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), label='Пароль')

    class Meta:
        model = MyUser
        fields = ['phone', 'password']
