
from video.models import *
from django.shortcuts import *

def category(request):
    """
    To have categories
    """
    
    categories = Category.objects.all()
    context = {"categories": categories}

    return context
