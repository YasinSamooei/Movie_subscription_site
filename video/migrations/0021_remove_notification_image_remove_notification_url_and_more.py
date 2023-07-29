# Generated by Django 4.2.2 on 2023-07-29 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_image'),
        ('video', '0020_alter_notification_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='image',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='url',
        ),
        migrations.AddField(
            model_name='notification',
            name='Video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifs', to='video.video', verbose_name='ویدئو'),
        ),
        migrations.AddField(
            model_name='notification',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifs', to='blog.blog', verbose_name='مقاله'),
        ),
    ]