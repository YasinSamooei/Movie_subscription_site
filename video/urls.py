from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [

    path('<str:slug>/', views.VideoDetailView.as_view(), name='video_detail'),
    path("add-favorite/<int:pk>", views.AddFavoriteView.as_view(), name="favorite_add"),
    path("like", views.LikeView.as_view(), name="like"),
    path('search', views.SearchView.as_view(), name='search'),
    path("watch", views.WatchListView.as_view(), name="watch"),

]