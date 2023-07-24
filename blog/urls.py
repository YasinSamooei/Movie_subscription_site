from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('blog/<str:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog-search', views.SearchView.as_view(), name='blog-search'),
    path('blog-list', views.BlogListView.as_view(), name='blog-list'),
    path('papular-blogs', views.PopularBlogListView.as_view(), name='papular-blogs'),
    path('tag/<str:slug>', views.TagDetailView.as_view(), name='tag-detail'),
    path("remove/<int:pk>", views.RemoveCommentView.as_view(), name='remove_comment'),
    
]