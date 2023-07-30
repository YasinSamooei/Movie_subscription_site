from django.shortcuts import render
from django.db.models import Q
from django.views import View
from urllib.parse import unquote
from django.shortcuts import *
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView,DetailView
# local 
from video.models import *


class VideoDetailView(HitCountDetailView):
    """
    View for video detail view
    with comment and reply capability
    """
    count_hit = True
    model = Video
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        video = self.get_object()
        video_categories = video.category.all()
        
        suggested_videos = Video.objects.filter(
            Q(category__in=video_categories) &
            ~Q(id=video.id)  # Exclude the current video from the results
        ).order_by('?').distinct()[:5]

        context = {
                "video": video,
                "suggested_videos": suggested_videos,
            }

        # Check if the video is liked by the user
        if self.request.user.likes.filter(video__slug=self.object.slug, user_id=self.request.user.id).exists():
            context["liked"] = True
        else:
            context["liked"] = False

        # Check if video is added to favorites by user
        if video.favorites.filter(id=request.user.id).exists():
            context["is_fav"] = True
        else:
            context["is_fav"] = False
        return context


class SearchView(ListView):
    template_name = "video/search-result.html"
    model = Video
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Video.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q))


class AddFavoriteView(View):
    """
    Add or remove a video from favorites
    """

    def get(self, request, pk):
        video = get_object_or_404(Video, id=pk)

        if video.favorites.filter(id=request.user.id).exists():
            video.favorites.remove(request.user)
            return JsonResponse({"response": "deleted"})
        else:
            video.favorites.add(request.user)
            return JsonResponse({"response": "added"})


class WatchListView(ListView):
    template_name = 'video/watch.html'
    model = Video
    paginate_by = 10

    def get_queryset(self):
        return Video.objects.filter(favorites=self.request.user)


class DeleteNotif(View):
    def get(self, req, pk):
        notif = Notification.objects.get(id=pk)
        notif.delete()
        pass


class DeletePublicNotif(View):
    def get(self, req, pk):
        notif = PublicNotification.objects.get(id=pk)
        notif.user.remove(req.user)
        notif.save()
        pass



def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(video__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({"response": "unliked"})
        except:
            Like.objects.create(video_id=pk, user_id=request.user.id)
            return JsonResponse({"response": "liked"})
    else:
        return redirect("accounts:login")




class CategoryDetailView(View):
    """
    View for returning videos
    of the selected category
    """

    def get(self, request, slug):
        slug = unquote(slug)
        category = get_object_or_404(Category, slug=slug)
        videos = Video.objects.filter(category__title=category)

        # pagination
        page_number = request.GET.get('page')
        paginator = Paginator(videos, 15)
        objects_list = paginator.get_page(page_number)

        context = {"videos": objects_list, "category": category}
        return render(request, 'video/video_category.html', context)


class SerialDetailView(HitCountDetailView):
    """
    View for serial detail view
    with parts of serial
    """
    count_hit = True
    model = Serial
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        serial = self.get_object()
        if serial.seasons:
            videos = serial.seasons.all()
            season=True
        else:
            videos = serial.video.all()
            season=False

        context = {
                "serial": serial,
                "videos": videos,
                "season":season,
            }
        return context

class SerialListView(ListView):
    template_name = "video/serial-list.html"
    model = Serial
    paginate_by = 10


class SeasonDetailView(DetailView):
    """
    View for season detail view
    with videos of each season
    """
    model = Season
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        season = self.get_object()
        videos = season.video.all()

        context = {
                "season": season,
                "videos": videos,
            }
        return context


class VideoListView(ListView):
    template_name = 'video/video_list.html'
    model = Video
    paginate_by = 10

    def get_queryset(self):
        # Return queryset based on filter
        filter = self.request.GET.get("filter")
        videos = Video.objects.all()
        if not filter or filter=="most-viewed":
            return Video.objects.order_by('-hit_count_generic__hits')
        elif filter == "most-liked":
            return Video.objects.all().order_by("-likes")
        elif filter == "most-recent":
            return Video.objects.all().order_by("-created_at")

