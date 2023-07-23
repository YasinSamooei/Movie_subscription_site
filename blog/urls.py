from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('blog/<str:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog-search', views.SearchView.as_view(), name='blog-search'),
]