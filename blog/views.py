from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import *
from hitcount.views import HitCountDetailView
from django.views.generic import ListView
from django.views import View
from django.core.paginator import Paginator
from urllib.parse import unquote
# local 
from blog.models import *


class BlogDetailView(HitCountDetailView):
    """
    View for blog detail view
    with comment and reply capability
    """
    count_hit = True
    model = Blog
    slug_field = 'slug'
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog=self.get_object()
        comment = blog.comments.all().order_by('-created_at')
        context = {
                "comments": comment,
                "blog":blog,
            }
        return context

    def post(self, request, slug):
        if not request.user.is_authenticated:
            return redirect("account:sign-in")
        slug = unquote(slug)
        blog = get_object_or_404(Blog, slug=slug)
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        Comment.objects.create(body=body, blog=blog, user=request.user, parent_id=parent_id)
        return redirect(reverse("blog:blog-detail",kwargs={"slug": slug}))




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
    context_object_name = "blogs"



class PopularBlogListView(ListView):
    template_name = "blog/papular-blog.html"
    model = Blog
    paginate_by = 10
    context_object_name = "blogs"
    queryset = Blog.objects.order_by('-hit_count_generic__hits')



class TagDetailView(View):
    """
    View for returning videos
    of the selected category
    """

    def get(self, request, slug):
        slug = unquote(slug)
        tag = get_object_or_404(Tag, slug=slug)
        blogs = Blog.objects.filter(tag__title=tag)

        # pagination
        page_number = request.GET.get('page')
        paginator = Paginator(blogs, 15)
        objects_list = paginator.get_page(page_number)

        context = {"blogs": objects_list, "tag": tag}
        return render(request, 'blog/blog-tags.html', context)


class RemoveCommentView(View):
    
    def get(self, req, **kwargs):
        comment_obj = Comment.objects.get(id=self.kwargs.get('pk'))
        comment_obj.delete()
        return redirect('home:main')
        