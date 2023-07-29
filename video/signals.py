from django.db.models.signals import post_save
from django.dispatch import receiver
from video.models import *


@receiver(post_save, sender=Video)
def create_video_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when pusblish a new movie
    """
    if created:
        message = f'فیلم {instance.title} منتشر شد'
        image=instance.image
        Notification.objects.create(all_user=True, message=message,image=image)

@receiver(post_save, sender=Serial)
def create_video_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when pusblish a new serial
    """
    if created:
        message = f'سریال {instance.name} منتشر شد'
        image=instance.image
        Notification.objects.create(all_user=True, message=message,image=image)

@receiver(post_save, sender=Season)
def create_season_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when pusblish a new season
    """      
    message = f' فصل جدید سریال {instance.season.name} منتشر شد'
    image=instance.image
    Notification.objects.create(all_user=True, message=message,image=image)