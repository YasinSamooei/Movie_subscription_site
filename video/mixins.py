from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
import datetime
import pytz

# Local apps
from video.models import Video


class UserWatchAccessMixin:
    """
    mixin that validates on
    the request.user for
    see videos
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.subs.all():
                utc = pytz.UTC
                if request.user.subs.first().expiration.replace(
                    tzinfo=utc
                ) <= datetime.datetime.now().replace(tzinfo=utc):
                    return redirect("account:user-setting")
                else:
                    return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("video:no-plan")
        else:
            return redirect("account:sign-in")
