from blog.models import*
from video.models import *
from django.shortcuts import *

def category(request):
    """
    To have categories and tags
    """
    
    categories = Category.objects.all()
    context = {"categories": categories}
    context['latest_blogs'] = Blog.objects.all()[:6]
    context['tags']=Tag.objects.all()

    return context
