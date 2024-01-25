from django import forms
from accounts.models import User


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")

        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["email"].required = False
        if not user.is_superuser:
            self.fields["is_staff"].disabled = True

    class Meta:
        model = User
        fields = ["email", "full_name", "is_staff", "bio", "gender", "image"]
