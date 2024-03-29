# Generated by Django 4.2.2 on 2023-07-29 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0022_rename_video_notification_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="season",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifs",
                to="video.season",
                verbose_name="فصل",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="serial",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifs",
                to="video.serial",
                verbose_name="سریال",
            ),
        ),
    ]
