from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Comment
from video.models import Notification


@receiver(post_save, sender=Comment)
def create_article_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when user reply comment 
    """
    if created and instance.parent_id:
        url = instance.blog.slug
        image=instance.blog.image
        message = f'کاربری به کامنت شما در مقاله {instance.blog.title} پاسخ داد'
        Notification.objects.create(user=instance.parent.user, message=message, url=url,image=image)

@receiver(post_save, sender=Comment)
def create_blog_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when add new article
    """
    if created:
        url = instance.blog.slug
        image=instance.blog.image
        message = f'مقاله {instance.blog.title}  منتشرشد'
        Notification.objects.create(all_user=True, message=message, url=url,image=image)
