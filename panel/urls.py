from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('profile', views.Profile.as_view(), name="profile"),
    path('article-list', views.ArticleList.as_view(), name='article-list'),
    path("article-create",views.ArticleCreate.as_view(),name="article-create"),
    path('update/article/<int:pk>', views.ArticleUpdate.as_view(), name="article-update"),
    path('delete/article/<int:pk>', views.ArticleDelete.as_view(), name="article-delete"),

    # video URLs
    path('video-list', views.VideoListView.as_view(), name='video-list'),
    path('video-create',views.CreateVideoView.as_view(),name="video-create"),
    path('update/video/<int:pk>',views.VideoUpdateView.as_view(),name="video-update"),

]