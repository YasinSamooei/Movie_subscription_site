# Generated by Django 4.2.2 on 2023-07-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0018_remove_serial_season_season_serial_season"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serial",
            name="video",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="playes",
                to="video.video",
                verbose_name="ویدیوها",
            ),
        ),
    ]
