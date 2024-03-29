# Generated by Django 4.2.2 on 2023-07-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0002_alter_video_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="age",
            field=models.CharField(
                blank=True,
                choices=[("بزرگسال", "20"), ("نوجوان", "14"), ("کودک", "10")],
                max_length=10,
                null=True,
                verbose_name="رده سنی",
            ),
        ),
    ]
