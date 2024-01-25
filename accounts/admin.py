from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, Subscription, Otp, SelectedSubscription

from .forms import SignUpForm, UserChangeForm

admin.site.site_header = "مدیریت سایت"
admin.site.site_title = "صفحه مدیریت"
admin.site.index_title = "سایت اشتراک ویدئو"


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = SignUpForm
    form = UserChangeForm

    list_display = (
        "email",
        "full_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "get_jalali_date",
    )
    list_filter = ("is_active", "is_superuser", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("اطلاعات شخصی", {"fields": ("full_name", "image", "gender", "language")}),
        ("دسترسی‌ها", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("اطلاعات شخصی", {"fields": ("full_name", "image", "gender", "language")}),
        ("دسترسی‌ها", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    search_fields = ("email", "full_name")
    ordering = ("is_superuser", "is_staff", "is_active", "email")
    filter_horizontal = ()

    # Staff can only delete their own account
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            if obj is not None and obj.id != request.user.id:
                return False
        return True

    # Staff can only change their own account info
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            if obj is not None and obj.id != request.user.id:
                return False
        return True

    # Staff can't add new account
    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        return True

    # Field makes specified fields as read-only for staff
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return "is_superuser", "is_staff", "is_active"
        return super(UserAdmin, self).get_readonly_fields(request)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            return qs
        return qs.filter(id=user.id)


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


admin.site.register(Subscription)
admin.site.register(Otp)

admin.site.register(SelectedSubscription)
