# Generated by Django 4.2.2 on 2023-07-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_user_birth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="birth",
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("مرد", "مرد"), ("زن", "زن")],
                max_length=10,
                null=True,
                verbose_name="جنسیت",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[
                    ("فارسی", "فارسی"),
                    ("انگلیسی", "انگلیسی"),
                    ("آلمانی", "آلمانی"),
                ],
                max_length=10,
                null=True,
                verbose_name="زبان",
            ),
        ),
    ]
