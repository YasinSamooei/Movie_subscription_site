from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import *
from hitcount.views import HitCountDetailView
from django.views.generic import ListView
# local 
from blog.models import *


class BlogDetailView(HitCountDetailView):
    """
    View for blog detail view
    with comment and reply capability
    """    
    count_hit=True
    model=Blog
    slug_field = 'slug'
    template_name="blog/blog_detail.html"
    context_object_name="blog"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)

        context['latest_blogs'] = Blog.objects.all()[:6]
        context['tags']=Tag.objects.all()
        return context





class SearchView(ListView):
    template_name = "blog/blog_search.html"
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Blog.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q))


