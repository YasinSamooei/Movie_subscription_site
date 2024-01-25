from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path("contact-us", views.ContactView.as_view(), name="contact"),
    path("privacy-policy", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("about-us", views.AboutUsView.as_view(), name="about-us"),
    path("faq", views.FaqView.as_view(), name="faq"),
]
