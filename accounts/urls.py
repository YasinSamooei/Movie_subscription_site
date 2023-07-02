from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('activate/',views.Activate.as_view(),name='ativate'),
    path('logout/',views.user_logout,name='logout')
]