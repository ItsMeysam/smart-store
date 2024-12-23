from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import View
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth import login
from home_module import templates


class RegisterVeiw(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data['email']
            user_password = register_form.cleaned_data['password']
            user_name = register_form.cleaned_data['name']
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد ')
            else:
                new_user = User(email=user_email,
                                email_active_code=get_random_string(72),
                                is_active=False,
                                username=user_name, )
                # از این متدد استفاده میکنیم تا در دیتابیس رمز کاربر به صورت هش شده دخیره شود set_password
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:  # بررسی میکنیم اگر کاربر وجود داشت is_active آن را فعال میکنیم و ذخیره میکنیم
            if not user.is_active:
                user.is_active = True
                # دوباره کد فعالسازی را ایجاد میکنیم به دلیل اینکه از یک ایمیل دوبار نتواند حساب را فعال کند
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login_page'))
            else:
                pass
                # todo: show your account activated message to user
        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data['email']
            user_name = login_form.cleaned_data['name']
            user_password = login_form.cleaned_data['password']
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')

                else:
                    #این متدد از داخل AbstractUser  فراخوانی میشود
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        user_name = login_form.cleaned_data['name']
                        login_form.add_error('email', 'کاربری با مشخصات وارد شده وجود ندارد')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده وجود ندارد')
        context = {
            'login_form': login_form,
        }

        return render(request, 'account_module/login_page.html', context)
