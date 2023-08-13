from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  UpdateView)

from accounts.models import User
from blog.models import Blog
from video.models import Video

from .forms import ProfileForm
from .mixins import *



class Profile(AuthorsAccessMixin,LoginRequiredMixin ,UpdateView):
    model = User
    template_name = 'panel/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('panel:profile')

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class ArticleList(BlogAuthorAccessMixin,AuthorsAccessMixin,ListView):
    """
    view that returns the list 
    of article of each author
    """
    template_name='panel/article-list.html'
    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class ArticleCreate(BlogAuthorAccessMixin,AuthorsAccessMixin,FormValidMixin,FieldsMixin,CreateView):
    model=Blog
    fields=['author','tag','title','description','meta_description','created_at','image','age','slug']
    template_name= 'panel/article-create-update.html'
    success_url = reverse_lazy('panel:article-list')



class ArticleUpdate(BlogAuthorAccessMixin,AuthorsAccessMixin,AuthorAccessMixin,UpdateFormMixin,FieldsMixin, UpdateView):
    model = Blog
    template_name = 'panel/article-create-update.html'
    success_url=reverse_lazy('panel:article-list')



class ArticleDelete(BlogAuthorAccessMixin,AuthorsAccessMixin,AuthorAccessMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('panel:article-list')
    template_name = 'panel/article_confirm_delete.html'


class VideoListView(VideoPublisherAccessMixin,AuthorsAccessMixin,ListView):
    template_name = 'panel/video-list.html'

    def get_queryset(self):
        return Video.objects.filter(creator=self.request.user)
    

class CreateVideoView(VideoPublisherAccessMixin,AuthorsAccessMixin,VideoFormValidMixin, CreateView):
    model = Video
    fields = ['title', 'category', 'actors', 'description', 'meta_description', 'image', 'video', 'trailer', 'age', 'time']
    template_name = 'panel/video-create-update.html'
    success_url=reverse_lazy('panel:video-list')


class VideoUpdateView(VideoPublisherAccessMixin,AuthorsAccessMixin,CreatorAccessMixin, UpdateView):
    model = Video
    fields = ['title', 'category', 'actors', 'description', 'meta_description', 'image', 'video', 'trailer', 'age', 'time']
    template_name = 'panel/video-create-update.html'
    success_url=reverse_lazy('panel:video-list')
    

class VideoDeleteView(VideoPublisherAccessMixin,AuthorsAccessMixin,CreatorAccessMixin,DeleteView):
    model = Video
    success_url = reverse_lazy('panel:video-list')
    template_name = 'panel/video_confirm_delete.html'
