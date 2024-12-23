from django.shortcuts import render
from django.views.generic import View


class ContactView(View):
    def get(self, request):
        return render(request, 'contact_module/contact_page.html')

    def post(self, request):
        pass