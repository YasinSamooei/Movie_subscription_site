# Generated by Django 4.2.2 on 2023-07-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0006_actors_video_actors"),
    ]

    operations = [
        migrations.AddField(
            model_name="actors",
            name="slug",
            field=models.SlugField(
                allow_unicode=True,
                blank=True,
                null=True,
                unique=True,
                verbose_name="اسلاگ",
            ),
        ),
    ]
