# Generated by Django 4.2.2 on 2023-07-30 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_alter_blog_image"),
        ("video", "0025_season_subject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="all_user",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="season",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="serial",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="video",
        ),
        migrations.CreateModel(
            name="PublicNotification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد"),
                ),
                ("message", models.TextField()),
                (
                    "blog",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="public",
                        to="blog.blog",
                        verbose_name="مقاله",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="public",
                        to="video.season",
                        verbose_name="فصل",
                    ),
                ),
                (
                    "serial",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="public",
                        to="video.serial",
                        verbose_name="سریال",
                    ),
                ),
                (
                    "user",
                    models.ManyToManyField(
                        related_name="public",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="public",
                        to="video.video",
                        verbose_name="ویدئو",
                    ),
                ),
            ],
            options={
                "verbose_name": " خبر عمومی",
                "verbose_name_plural": "اخبار عمومی",
                "ordering": ("-created_at",),
            },
        ),
    ]
