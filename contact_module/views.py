from django.shortcuts import render
from django.views.generic import View
from contact_module.forms import ContactForm


class ContactView(View):
    template_name = ('contact_module/contact_page.html')
    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, context={'form' : form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # ذخیره اطلاعات در دیتابیس
            ContactForm.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                mobile=form.cleaned_data['mobile'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            return render(request, self.template_name, {
                'form': ContactForm(),  # فرم جدید برای نمایش
                'success_message': 'پیام شما با موفقیت ارسال شد!'
            })
        return render(request, self.template_name, {'form': form})