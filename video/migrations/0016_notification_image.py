# Generated by Django 4.2.2 on 2023-07-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0015_merge_20230728_1413"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="عکس"
            ),
        ),
    ]
