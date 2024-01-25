from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
import datetime
import pytz

from . import message
from .forms import *
from .mixins import *
from .models import *
from .otp_service import OTP


class SignInView(generic.FormView):
    template_name = "accounts/sign-in.html"
    form_class = SignInForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(
                username=clean_data["email"], password=clean_data["password"]
            )
            if user is not None:
                login(self.request, user)
                return redirect("home:main")
            else:
                form.add_error("email", message.Wrong_Email_Or_Password)
        return render(request, "accounts/sign-in.html", context={"form": form})


class SignUpView(generic.FormView):
    template_name = "accounts/sign-up.html"
    form_class = SignUpForm

    def form_valid(self, form):
        data = form.cleaned_data
        otp_service = OTP()
        otp_service.generate_otp(data["email"])
        cache.set(
            key="register",
            value={
                "email": data["email"],
                "password": data["password"],
                "full_name": data["full_name"],
            },
            timeout=300,
        )
        return redirect("account:verify-otp")


class CheckOTPView(generic.View):
    form_class = CheckOTPForm

    def get(self, request):
        form = self.form_class()
        return render(request, "accounts/verify_otp.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data_cache = cache.get(key="register")
            otp_obj = OTP()
            if data is None:
                messages.add_message(
                    request, messages.WARNING, "کد وجود ندارد یا نامعتبر است"
                )
            try:
                if otp_obj.verify_otp(otp=data["code"], data=data_cache["email"]):
                    user = User.objects.create_user(
                        email=data_cache["email"],
                        full_name=data_cache["full_name"],
                        password=data_cache["password"],
                    )
                    login(request, user)
                    return redirect("home:main")
                else:
                    messages.add_message(
                        request, messages.WARNING, "کد وجود ندارد یا نامعتبر است"
                    )
            except:
                messages.add_message(
                    request, messages.WARNING, "کد وجود ندارد یا نامعتبر است"
                )
                return render(request, "accounts/verify_otp.html", {"form": form})

        return render(request, "accounts/verify_otp.html", {"form": form})


class ChangeEmailView(generic.FormView):
    template_name = "accounts/change-email.html"
    form_class = ChangeEmailForm

    def form_valid(self, form):
        data = form.cleaned_data
        otp_service = OTP()
        otp_service.generate_otp(data["email"])
        cache.set(key="change", value={"email": data["email"]}, timeout=300)
        if User.objects.filter(email=data["email"]):
            messages.add_message(
                self.request,
                messages.WARNING,
                "ایمیل وارد شده قبلا توسط کاربر دیگری استفاده شده.",
            )
            return redirect("account:change-email")
        else:
            return redirect("account:change-otp")


class ChangeOTPView(generic.View):
    form_class = CheckOTPForm

    def get(self, request):
        form = self.form_class()
        return render(request, "accounts/change-otp.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data_cache = cache.get(key="change")
            otp_obj = OTP()
            if data is None:
                messages.add_message(
                    request, messages.WARNING, "کد وجود ندارد یا نامعتبر است"
                )
            try:
                if otp_obj.verify_otp(otp=data["code"], data=data_cache["email"]):
                    user = request.user
                    user.email = data_cache["email"]
                    user.save()
                    return redirect("home:main")
                else:
                    messages.add_message(
                        request, messages.WARNING, "کد وجود ندارد یا نامعتبر است"
                    )
            except:
                messages.add_message(
                    request, messages.WARNING, "کد وجود ندارد یا نامعتبر است"
                )
                return render(request, "accounts/change-otp.html", {"form": form})

        return render(request, "accounts/change-otp.html", {"form": form})


# user panel views


class UserSettingsView(RequiredLoginMixin, generic.View):
    def get(self, request):
        utc = pytz.UTC
        if request.user.subs.all():
            if request.user.subs.first().expiration.replace(
                tzinfo=utc
            ) <= datetime.datetime.now().replace(tzinfo=utc):
                endtime = True
            else:
                endtime = False
        else:
            endtime = False
        return render(
            request,
            "accounts/user-setting.html",
            {"user": request.user, "endtime": endtime},
        )


class ManageProfileView(FieldsMixin, generic.UpdateView):
    model = User
    fields = ["language", "gender", "full_name", "image", "bio"]
    template_name = "accounts/manage-profile.html"
    success_url = reverse_lazy("account:user-setting")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


class PricingPlanView(generic.ListView):
    model = Subscription
    template_name = "accounts/pricing-plan.html"
    context_object_name = "subscription"

    def get_queryset(self):
        return Subscription.objects.all()


# Customized password change and reset views


class ChangePasswordView(PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("account:user-setting")
    form_class = ChangePasswordForm


class PasswordReset(PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    success_url = reverse_lazy("account:password_reset_done")


class PasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"
    success_url = reverse_lazy("account:password_reset_confirm")


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("account:password_reset_complete")


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


# select pricing plan


class SelectPricingPlanView(PricingFieldsMixin, FormValidMixin, generic.CreateView):
    model = SelectedSubscription
    fields = ["Subscription_plan"]
    template_name = "accounts/selection_pricing_plan.html"
    success_url = reverse_lazy("account:user-setting")


class PricingPlanDeleteView(generic.View):
    def get(self, req, pk):
        pricing = SelectedSubscription.objects.get(id=pk)
        pricing.delete()
        return render("accounts/selection_pricing_plan")
