from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('profile', views.Profile.as_view(), name="profile"),
    path('article-list', views.ArticleList.as_view(), name='article-list'),

]