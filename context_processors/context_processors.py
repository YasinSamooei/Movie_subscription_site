from blog.models import*
from video.models import *
from django.shortcuts import *

def category(request):
    """
    To have categories and tags and public notification
    """
    
    categories = Category.objects.all()
    context = {"categories": categories}
    context['latest_blogs'] = Blog.objects.all()[:6]
    context['tags']=Tag.objects.all()

    if request.user.is_authenticated:
        notifications = PublicNotification.objects.filter(user=request.user)
        context.update({'notifications': notifications})

    return context
