from django.core.exceptions import ValidationError
from django import forms
from .models import User



class SignUpForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            {'class': "email-input", "placeholder": "ایمیل خود را وارد کنید", 'maxlength': 50}),
    )
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "email-input",
                                                              "placeholder": "نام و نام خانوادگی خود را وارد کنید"}))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        "class": "password-input", "placeholder": "گذرواژه خود را وارد کنید"
    }))

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data.get("email")).exists():
            raise ValidationError("کاربر با این ایمیل در سایت وجود دارد")
        return self.cleaned_data.get("email")

    def clean_password(self):
        if len(self.cleaned_data.get("password")) < 8:
            raise ValidationError("طول گذرواژه باید حداقل ۸ کاراکتر باشد")
        return self.cleaned_data.get("password")


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder": "ایمیل خود را وارد کنید"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "گذرواژه خود را وارد کنید"}))


