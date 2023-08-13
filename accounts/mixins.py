from django.shortcuts import redirect
import datetime

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
             'full_name','image','bio'
		]
		return super().dispatch(request, *args, **kwargs)


class PricingFieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
			'Subscription_plan'
		]
		return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    """
    mixin that validates on 
    the Subscription_plan creation form
    """

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user=self.request.user
        month=self.obj.Subscription_plan.month*30
        day=self.obj.Subscription_plan.day
        week=self.obj.Subscription_plan.week*7
        total=month+day+week
        self.obj.expiration=datetime.datetime.now()+datetime.timedelta(days=total)
        return super().form_valid(form)