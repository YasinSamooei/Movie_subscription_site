from django.utils.text import slugify
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
# Local apps
from blog.models import Blog


class FieldsMixin():
    """
    mixin that return fields of
    blog model
    """

    def dispatch(self, request, *args, **kwargs):
        self.fields = [
            "title", "tag",
            "description", "image",
            "age", "meta_description",
        ]
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    """
    mixin that validates on 
    the blog creation form
    """

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.slug = slugify(self.obj.title, allow_unicode=True)
        return super().form_valid(form)

class UpdateFormMixin():
    """
    mixin that validates on 
    the blog update 
    """

    def form_valid(self, form):
        return super().form_valid(form)


class AuthorAccessMixin():
    """
    mixin that validates on 
    the request.user for
    update blog
    """

    def dispatch(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=pk)
        if blog.author == request.user or \
                request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما نمی توانید این صفحه را مشاهده کنید.")



class AuthorsAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser or request.user.is_staff:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("account:manage-profile")
		else:
			return redirect("account:login")