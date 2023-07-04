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

class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
			'language', 'gender',
             'full_name','image'
		]
		return super().dispatch(request, *args, **kwargs)
