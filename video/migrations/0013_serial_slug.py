# Generated by Django 4.2.2 on 2023-07-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0012_remove_serial_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="serial",
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
