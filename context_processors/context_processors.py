
from video.models import *
from django.shortcuts import *

def category(request):
    """
    To have categories
    """
    
    categories = Category.objects.all()
    context = {"categories": categories}

    # Check if the video is liked by the user
 
    return context
