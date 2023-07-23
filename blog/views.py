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



class SearchView(ListView):
    template_name = "blog/blog_search.html"
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Blog.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q))


class BlogListView(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    paginate_by = 10
    context_object_name="blogs"
    


class PopularBlogListView(ListView):
    template_name = "blog/papular-blog.html"
    model = Blog
    paginate_by = 10
    context_object_name="blogs"
    queryset=Blog.objects.order_by('-hit_count_generic__hits')

