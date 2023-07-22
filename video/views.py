from django.shortcuts import render
from django.db.models import Q
from django.views import View
from urllib.parse import unquote_plus
from django.shortcuts import *
from hitcount.views import HitCountDetailView
from django.http import JsonResponse
from django.views.generic import ListView
# local 
from video.models import *


class VideoDetailView(HitCountDetailView):
    """
    View for video detail view
    with comment and reply capability
    """    
    count_hit=True
    def get(self, request, slug):
        slug = unquote_plus(slug)
        video = get_object_or_404(Video, slug=slug)
        suggested_videos = Video.objects.filter(category__in=video.category.all().reverse()).distinct()[:3]
        suggested_videos = set(suggested_videos)  
        context = {
            "video": video,
            "suggested_videos": suggested_videos,
        }
        # Check if the video is liked by the user
        if request.user.is_authenticated:
            if video.likes.filter(email=request.user.email).exists():
                context["is_liked"] = True
            else:
                context["is_liked"] = False

        # Check if video is added to favorites by user
        if video.favorites.filter(id=request.user.id).exists():
            context["is_fav"] = True
        else:
            context["is_fav"] = False

        return render(request, "video/video_detail.html", context)


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


class LikeView(View):
    """
    View to like videos with ajax
    """

    def post(self, request):
        result = ""
        id = int(request.POST.get("videoid"))
        video = get_object_or_404(Video, id=id)

        # If user has already liked the video, so unlike it.
        if video.likes.filter(id=request.user.id).exists():
            video.likes.remove(request.user)
            video.like_count -= 1
            result = video.like_count,
            liked = False
            video.save()
        # If user hasn't liked the video yet, like it.
        else:
            video.likes.add(request.user)
            video.like_count += 1
            result = video.like_count
            liked = True
            video.save()

        return JsonResponse({"result": result, "liked": liked})


class WatchListView(ListView):
    template_name = 'video/watch.html'
    model = Video
    paginate_by = 10

    def get_queryset(self):
        return Video.objects.filter(favorites=self.request.user)


def delete_notification(request,pk):
    notif=Notification.objects.get(id=pk)
    notif.delete()
    return JsonResponse({"response":"deleted"})