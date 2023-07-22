from django.views.generic import TemplateView
from accounts.mixins import RequiredLoginMixin

# local
from video.models import Video

class HomeView(RequiredLoginMixin,TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['latest_videos'] = Video.objects.all()[:6]

        most_visited=Video.objects.order_by('-hit_count_generic__hits')
        context['most_visited'] = most_visited[:6]

        popular_videos=Video.objects.order_by('-like_count')
        context['popular_videos'] = popular_videos[:6]
        
        return context


