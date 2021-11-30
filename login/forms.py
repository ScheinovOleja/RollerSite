import requests
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from social_treatment.mailing import send_register_user
from .models import MyUser


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
        send_register_user(self.cleaned_data['phone'], self.password)
        avatar = requests.get(
            url=f'https://avatars.dicebear.com/api/initials/{user.first_name}_{user.last_name}.svg?size=32')
        user.avatar = avatar.content.decode(encoding='utf-8').replace('\'', '')
        user.save()
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
