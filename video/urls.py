from django.urls import path,re_path
from . import views

app_name = 'video'

urlpatterns = [

    path('<str:slug>/', views.VideoDetailView.as_view(), name='video_detail'),
    path('category/<str:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
    path("add-favorite/<int:pk>", views.AddFavoriteView.as_view(), name="favorite_add"),
    path('search', views.SearchView.as_view(), name='search'),
    path("watch", views.WatchListView.as_view(), name="watch"),
    path('delete-notif/<int:pk>',views.delete_notification,name="delete-notif"),
    re_path(r"like/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)",views.like,name="like"),

]