# Generated by Django 4.2.2 on 2023-07-29 11:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0021_remove_notification_image_remove_notification_url_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notification",
            old_name="Video",
            new_name="video",
        ),
    ]
