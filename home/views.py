from django.views.generic import TemplateView
from accounts.mixins import RequiredLoginMixin

# local
from video.models import Video,Serial

class HomeView(RequiredLoginMixin,TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['latest_videos'] = Video.objects.all().order_by("-created_at")[:6]

        most_visited=Video.objects.order_by('-hit_count_generic__hits')
        context['most_visited'] = most_visited[:6]

        popular_videos=Video.objects.order_by('-likes')
        context['popular_videos'] = popular_videos[:6]

        serial=Serial.objects.all()
        context['serial']=serial[:6]
               
        return context


