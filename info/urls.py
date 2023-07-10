from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [

    path('contact-us', views.ContactView.as_view(), name='contact'),

]