from django.contrib import admin
from .models import Contact,Question


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','last_name','email','content')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('question','answer')