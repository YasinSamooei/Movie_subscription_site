from django.shortcuts import redirect


class RequiredLoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:sign-in')
        return super().dispatch(request, *args, **kwargs)


class AuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:main")
        return super().dispatch(request, *args, **kwargs)


class AuthenticatedOrNotTokenMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated or not request.GET.get("token"):
            return redirect("home:main")
        return super().dispatch(request, *args, **kwargs)


class NotAuthenticatedOrNotTokenMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.GET.get("token"):
            return redirect("home:main")
        return super().dispatch(request, *args, **kwargs)
