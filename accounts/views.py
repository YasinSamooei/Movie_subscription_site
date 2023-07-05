from django.contrib.auth import login , authenticate
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import (CreateView, FormView, View,
UpdateView,ListView)
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from uuid import uuid4
from django.contrib.auth.views import (PasswordChangeView,PasswordResetView,
PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)
import random

#local
from .models import *
from .mixins import *
from .forms import *
from . import message
from accounts.models import User,Subscription


class SignInView(FormView):
    template_name = 'accounts/sign-in.html'
    form_class = SignInForm
    def post(self, req, *args, **kwargs):
        form = self.form_class(req.POST)
        if form.is_valid():
            user = authenticate(req, username=form.cleaned_data['email'],
                                              password=form.cleaned_data['password'])
            if user is not None:
                login(req, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home:main')
            else:
                form.add_error('email', message.Wrong_Email_Or_Password)
        return render(req, self.template_name, {'form': form})



class SignUpView(AuthenticatedMixin, CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = SignUpForm

    def form_valid(self, form):
        user= form.save(commit=False)
        user.is_active = False
        user.save()
        cd = form.cleaned_data
        new_email = cd.get("email")
        token = uuid4().hex
        code = random.randint(10000, 99999)
        expiration = timezone.localtime(timezone.now()) + timezone.timedelta(minutes=10)
        Otp.objects.create(email=form.cleaned_data.get('email'), token=token, code=code,
                           full_name=form.cleaned_data.get('full_name')
                           , expiration=expiration, password=form.cleaned_data.get('password'))
        current_site = get_current_site(self.request)  # to get the domain of the current site
        mail_subject = 'لینک تغییر آدرس ایمیل'
        message = render_to_string('accounts/change_email.html', {
            'user': user,
            'url': str(current_site.domain)
            + reverse_lazy("account:ativate")
            + f"?token={token}",
                    })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                mail_subject, message, to=[to_email]
                )
        email.send()
        messages.add_message(self.request, messages.SUCCESS, f"لینک فعالسازی به آدرس {new_email} ارسال گردید")
        return redirect("account:sign-up")


class Activate(View):
    """view for activate user by email confirmation"""
    def get(self, request):
        token = request.GET.get("token")
        otp=Otp.objects.get(token=token)
        if otp.is_not_expired:
            email=otp.email
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(self.request, messages.SUCCESS, "حساب شما با موفقیت فعال گردید.")
            return redirect("account:user-setting")
        else:
            messages.add_message(self.request, messages.ERROR, "توکن شما منقضی شده لطفا دوباره تلاش کنید")
            return redirect("account:user-setting")



# user panel views

class UserSettingsView(RequiredLoginMixin, View):
    def get(self, request):
        return render(request, 'accounts/user-setting.html', {'user': request.user})


class ManageProfileView(FieldsMixin,UpdateView):
    model = User
    fields=['language', 'gender', 'full_name','image']
    template_name = 'accounts/manage-profile.html'
    success_url = reverse_lazy('account:user-setting')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class PricingPlanView(ListView):
    model=Subscription
    template_name="accounts/pricing-plan.html"
    context_object_name="subscription"
    def get_queryset(self):
        return Subscription.objects.all()




# Customized password change and reset views

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('account:user-setting')
    form_class = ChangePasswordForm

class PasswordReset(PasswordResetView):
    template_name="accounts/password_reset_form.html"
    success_url=reverse_lazy("account:password_reset_done")

class PasswordResetDone(PasswordResetDoneView):
    template_name="accounts/password_reset_done.html"
    success_url=reverse_lazy("account:password_reset_confirm")

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name="accounts/password_reset_confirm.html"
    success_url=reverse_lazy("account:password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
    template_name="accounts/password_reset_complete.html"
