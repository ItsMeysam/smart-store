from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    name = forms.CharField(
        label='نام',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator,
        ]

    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput()

    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput()

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class LoginForm(forms.Form):
    name = forms.CharField(
        label='نام',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput()

    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator,
        ]

    )

