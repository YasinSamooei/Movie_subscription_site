from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "account"
urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign-in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("verify-otp/", views.CheckOTPView.as_view(), name="verify-otp"),
    path("logout/", LogoutView.as_view(next_page="home:main"), name="logout"),
    path("user/setting", views.UserSettingsView.as_view(), name="user-setting"),
    path("manage/profile", views.ManageProfileView.as_view(), name="manage-profile"),
    path("pricing/plan", views.PricingPlanView.as_view(), name="pricing-plan"),
    path("select-plan", views.SelectPricingPlanView.as_view(), name="select-plan"),
    path(
        "delete-pricing-plan/<int:pk>",
        views.PricingPlanDeleteView.as_view(),
        name="delete-pricing-plan",
    ),
    path("change-email/", views.ChangeEmailView.as_view(), name="change-email"),
    path("change-otp/", views.ChangeOTPView.as_view(), name="change-otp"),
    path("change/password", views.ChangePasswordView.as_view(), name="change-password"),
    path("password_reset/", views.PasswordReset.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDone.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirm.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetComplete.as_view(),
        name="password_reset_complete",
    ),
]
