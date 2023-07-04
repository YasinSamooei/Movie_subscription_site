from django.views.generic import TemplateView
from accounts.mixins import RequiredLoginMixin


class HomeView(RequiredLoginMixin,TemplateView):
    template_name = 'home/index.html'

