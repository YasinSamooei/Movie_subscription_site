from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib import messages

# local
from .forms import ContactForm
from accounts.models import User
from .models import Question


class ContactView(CreateView):
    template_name = "info/contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request, messages.SUCCESS, "پیام شما با موفقیت ثبت گردید"
        )
        return redirect("info:contact")


class PrivacyPolicyView(TemplateView):
    template_name = "info/privacy-policy.html"


class AboutUsView(ListView):
    template_name = "info/about-us.html"
    queryset = User.objects.filter(is_staff=True)


class FaqView(ListView):
    template_name = "info/faq.html"
    queryset = Question.objects.all()
