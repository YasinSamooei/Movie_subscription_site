from django.db import models

class Contact(models.Model):
    name=models.CharField("نام",max_length=30)
    last_name=models.CharField("نام خانوادگی",max_length=30)
    email=models.EmailField("ایمیل")
    content=models.TextField("متن پیام")

    class Meta:
        verbose_name_plural = "پیام"
        verbose_name = "پیام ها"

    def __str__(self):
        return str(self.email)
