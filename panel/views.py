from typing import Any, Dict
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Local apps

from blog.models import Blog
from accounts.models import User
from .forms import ProfileForm
from .mixins import*


class Profile(AuthorsAccessMixin,LoginRequiredMixin ,UpdateView):
    model = User
    template_name = "panel/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("panel:profile")

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class ArticleList(ListView):
    """
    view that returns the list 
    of article of each author
    """
    template_name="panel/article-list.html"
    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class ArticleCreate(FormValidMixin,FieldsMixin,CreateView):
    model=Blog
    fields=['author','tag','title','description','meta_description','created_at','image','age','slug']
    template_name="panel/article-create-update.html"
    success_url=reverse_lazy("panel:article-list")



class ArticleUpdate(AuthorAccessMixin,UpdateFormMixin,FieldsMixin, UpdateView):
    model = Blog
    template_name = "panel/article-create-update.html"
    success_url=reverse_lazy("panel:article-list")



class ArticleDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('panel:article-list')
    template_name = "panel/article_confirm_delete.html"


