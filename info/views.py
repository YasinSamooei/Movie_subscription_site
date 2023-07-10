from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages

# local
from .forms import ContactForm


class ContactView(CreateView):
    template_name = 'info/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "پیام شما با موفقیت ثبت گردید")
        return redirect("info:contact")


