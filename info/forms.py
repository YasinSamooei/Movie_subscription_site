from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"email-input","placeholder": "نام خود را وارد کنید"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "email-input", "placeholder": "نام خانوادگی خود را وارد کنید"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "email-input", "placeholder": " ایمیل خود را وارد کنید"}))
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "email-input", "placeholder": " پیام خود را وارد کنید"}))

    class Meta:
        model = Contact
        fields = ('name', 'last_name', 'email','content')    