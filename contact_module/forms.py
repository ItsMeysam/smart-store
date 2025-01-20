from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام')
    email = forms.EmailField(label='ایمیل')
    mobile = forms.CharField(max_length=15, required=False, label='موبایل')
    subject = forms.CharField(max_length=200, label='عنوان')