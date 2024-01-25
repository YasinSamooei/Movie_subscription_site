from django.db import models


class Contact(models.Model):
    name = models.CharField("نام", max_length=30)
    last_name = models.CharField("نام خانوادگی", max_length=30)
    email = models.EmailField("ایمیل")
    content = models.TextField("متن پیام")

    class Meta:
        verbose_name_plural = "پیام"
        verbose_name = "پیام ها"

    def __str__(self):
        return str(self.email)


class Question(models.Model):
    question = models.CharField("سوال", max_length=500)
    answer = models.TextField("پاسخ")

    class Meta:
        verbose_name_plural = "سوال متداول"
        verbose_name = "سوالات متداول"

    def __str__(self):
        return str(self.question)
