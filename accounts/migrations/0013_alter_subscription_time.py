# Generated by Django 4.2.2 on 2023-08-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0012_alter_selectedsubscription_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="مدت زمان"),
        ),
    ]
