from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин'
    )

    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput,
    )


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        label='Логин'
    )

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        strip=False
    )

    class Meta:
        model = User
        fields = ('username',)