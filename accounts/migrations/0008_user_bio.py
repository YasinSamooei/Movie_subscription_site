# Generated by Django 4.2.2 on 2023-07-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_subscription_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, null=True, verbose_name="بیوگرافی"),
        ),
    ]
