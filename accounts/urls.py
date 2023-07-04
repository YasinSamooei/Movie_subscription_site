from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('activate/',views.Activate.as_view(),name='ativate'),
    path('logout/',views.user_logout,name='logout'),
    path('user/setting',views.UserSettingsView.as_view(),name="user-setting"),
    path('change/password',views.ChangePasswordView.as_view(),name="change-password"),
    path('manage/profile',views.ManageProfileView.as_view(),name="manage-profile")
]